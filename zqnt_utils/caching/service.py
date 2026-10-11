"""
CachingService – async Redis client that mirrors the Java CachingService.

Supports both context-manager usage (short-lived) and persistent connections::

    # Short-lived (e.g. one-shot registration):
    async with CachingService(redis_url) as cache:
        await cache.register_edge_endpoint("DJI", dto)

    # Long-lived (adapter lifecycle):
    cache = CachingService.from_env()
    await cache.connect()
    await cache.set_current_asset_telemetry(sn, telemetry_json)
    await cache.close()
"""

import logging
import os
from typing import Any

import redis.asyncio

from .keys import CacheKeys
from zqnt_api.core import EdgeEndpointDTO

logger = logging.getLogger(__name__)


class CachingService:
    """
    Async Redis wrapper with the same operations as the Java CachingService.

    Args:
        redis_url: Redis connection URL (e.g. ``"redis://redis:6379"``).
    """

    def __init__(self, redis_url: str) -> None:
        self._redis_url = redis_url
        self._client = None

    @classmethod
    def from_env(
        cls, url_env: str = "REDIS_URL", default: str = "redis://localhost:6379"
    ) -> "CachingService":
        """Build from the ``REDIS_URL`` environment variable (or *url_env*)."""
        return cls(os.environ.get(url_env, default))

    # ------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------

    async def connect(self) -> None:
        """Open a persistent connection pool."""
        import redis.asyncio as aioredis

        self._client = aioredis.from_url(self._redis_url, decode_responses=True)
        logger.debug("CachingService connected to %s", self._redis_url)

    async def close(self) -> None:
        """Close the connection pool."""
        if self._client is not None:
            await self._client.aclose()
            self._client = None

    async def __aenter__(self) -> "CachingService":
        await self.connect()
        return self

    async def __aexit__(self, *_: Any) -> None:
        await self.close()

    # ------------------------------------------------------------------
    # Edge endpoint registration
    # ------------------------------------------------------------------

    async def register_edge_endpoint(self, vendor: str, dto: EdgeEndpointDTO) -> None:
        """
        Store the edge endpoint DTO under ``edge-endpoints:{vendor}``.

        Mirrors ``cachingService.registerEdgeEndpoint(vendor, dto)``.
        """
        key = CacheKeys.EDGE_ENDPOINTS.build(vendor=vendor)
        await self._safe_set(key, dto.to_json(), op=f"registerEdgeEndpoint[{vendor}]")

    async def get_edge_endpoint(self, vendor: str) -> EdgeEndpointDTO | None:
        """Retrieve the edge endpoint DTO for *vendor*, or ``None`` if absent."""
        key = CacheKeys.EDGE_ENDPOINTS.build(vendor=vendor)
        data = await self._safe_get(key, op=f"getEdgeEndpoint[{vendor}]")
        if data is None:
            return None
        try:
            return EdgeEndpointDTO.from_json(data)
        except Exception as exc:
            logger.error(
                "Failed to parse EdgeEndpointDTO for vendor %s: %s", vendor, exc
            )
            return None

    async def deregister_edge_endpoint(self, vendor: str) -> None:
        """
        Mark endpoint as offline (soft delete – keeps data for monitoring).

        Mirrors ``cachingService.deregisterEdgeEndpoint(vendor)``.
        """
        dto = await self.get_edge_endpoint(vendor)
        if dto is None:
            logger.warning(
                "Cannot deregister non-existent endpoint for vendor: %s", vendor
            )
            return
        dto.online = False
        key = CacheKeys.EDGE_ENDPOINTS.build(vendor=vendor)
        await self._safe_set(key, dto.to_json(), op=f"deregisterEdgeEndpoint[{vendor}]")

    async def delete_edge_endpoint(self, vendor: str) -> None:
        """Hard delete – removes the key entirely."""
        key = CacheKeys.EDGE_ENDPOINTS.build(vendor=vendor)
        await self._safe_delete(key, op=f"deleteEdgeEndpoint[{vendor}]")

    # ------------------------------------------------------------------
    # Asset vendor mapping  (SN → vendor for routing)
    # ------------------------------------------------------------------

    async def register_asset_vendor(self, sn: str, vendor: str) -> None:
        """Map *sn* → *vendor* under ``edge-vendor:{sn}``."""
        key = CacheKeys.EDGE_VENDOR.build(sn=sn)
        await self._safe_set(key, vendor, op=f"registerAssetVendor[{sn},{vendor}]")

    async def get_asset_vendor(self, sn: str) -> str | None:
        """Return the vendor name for *sn*, or ``None``."""
        key = CacheKeys.EDGE_VENDOR.build(sn=sn)
        return await self._safe_get(key, op=f"getAssetVendor[{sn}]")

    # ------------------------------------------------------------------
    # Generic key/value helpers (for adapter-specific use)
    # ------------------------------------------------------------------

    async def set(self, key: str, value: str) -> None:
        """Raw ``SET key value``."""
        await self._safe_set(key, value, op=f"set[{key}]")

    async def setex(self, key: str, ttl_seconds: int, value: str) -> None:
        """Raw ``SETEX key ttl value``."""
        try:
            client = await self._get_client()
            await client.setex(key, ttl_seconds, value)
        except Exception as exc:
            logger.error("Redis setex[%s] failed: %s", key, exc)

    async def get(self, key: str) -> str | None:
        """Raw ``GET key``."""
        return await self._safe_get(key, op=f"get[{key}]")

    async def delete(self, *keys: str) -> None:
        """Raw ``DEL key [key ...]``."""
        try:
            client = await self._get_client()
            await client.delete(*keys)
        except Exception as exc:
            logger.error("Redis delete%s failed: %s", keys, exc)

    # ------------------------------------------------------------------
    # Internal
    # ------------------------------------------------------------------

    async def _get_client(self) -> redis.asyncio.Redis | None:
        if self._client is None:
            await self.connect()
        return self._client

    async def _safe_set(self, key: str, value: str, *, op: str) -> None:
        try:
            client = await self._get_client()
            await client.set(key, value)
        except Exception as exc:
            logger.error("Redis operation '%s' failed: %s", op, exc)

    async def _safe_get(self, key: str, *, op: str) -> str | None:
        try:
            client = await self._get_client()
            return await client.get(key)
        except Exception as exc:
            logger.error("Redis operation '%s' failed: %s", op, exc)
            return None

    async def _safe_delete(self, key: str, *, op: str) -> None:
        try:
            client = await self._get_client()
            await client.delete(key)
        except Exception as exc:
            logger.error("Redis operation '%s' failed: %s", op, exc)
