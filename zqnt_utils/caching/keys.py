"""
CacheKeys – mirrors com.zqnt.utils.caching.CacheKeys.

Key patterns use ``{placeholder}`` syntax; call ``.build(**kwargs)`` to
substitute placeholders::

    key = CacheKeys.EDGE_ENDPOINTS.build(vendor="DJI")
    # → "zqnt:edge-endpoints:DJI"

    key = CacheKeys.ASSET_ACTIVE_TASKS.build(sn="DOCK001", taskId="task-1")
    # → "zqnt:asset-active-tasks:DOCK001:task-1"
"""

from enum import Enum


class CacheKeys(Enum):
    # All keys live under the "zqnt:" namespace so a shared/multi-tenant Redis instance can tell
    # our keys apart at a glance (SCAN zqnt:*, ACL patterns, etc.) — matches every other Redis key
    # in the platform and the Java CacheKeys this mirrors. Was missing here until 2026-09-02: a
    # real, live bug, not just a naming nicety — every Python-based edge adapter (mavlink,
    # betaflight, sapient, rns) registers itself via CachingService.register_edge_endpoint()/
    # register_asset_vendor(), which write under these unprefixed keys; the Java-side
    # GrpcEndpointRouter that actually dispatches SendCustomCommand only ever reads
    # "zqnt:edge-vendor:{sn}"/"zqnt:edge-endpoints:{vendor}", so it could never find them.
    ASSET_ONLINE = "zqnt:asset-online:"
    ASSET_MODE = "zqnt:asset-mode:"
    # Renamed from ASSET_TELEMETRY ("asset-telemetry:") to TELEMETRY ("zqnt:telemetry:{sn}") to
    # match the Java enum member and value exactly — the old name/value pair didn't correspond to
    # anything Java-side at all (Java's own key is "zqnt:telemetry:{sn}"), so
    # sapient-adapter's telemetry cache writes were invisible to every core/ service. The old
    # SUBASSET_TELEMETRY ("subasset-telemetry:") had no Java equivalent and no callers anywhere in
    # this repo — dropped rather than carried forward as more dead drift; sub-asset telemetry is
    # just TELEMETRY keyed by the sub-asset's own SN (see edge_ai/telemetry_watcher.py's docstring).
    TELEMETRY = "zqnt:telemetry:{sn}"
    ASSET_LINK_TELEMETRY = "zqnt:asset-link-telemetry:"
    ASSET_EXTENDED_TELEMTRY = "zqnt:asset-extended-telemetry:"  # intentional typo – matches Java
    ASSET_MANUAL_CONTROL_STATE = "zqnt:drc-state:"
    ASSET_LIVE_STREAM_STATE = "zqnt:live-stream-state:"
    ASSET_SERVICES_REPLY_WAIT = "zqnt:asset-task-reply-wait:{tid}:{method}"
    ASSET_ACTIVE_TASKS = "zqnt:asset-active-tasks:{sn}:{taskId}"
    ASSET_COMPLETED_TASKS = "zqnt:asset-completed-tasks:{sn}:{taskId}"
    ASSET_TASK_EXTERNAL_ID_REFERENCE = (
        "zqnt:asset-task-external-id-reference:{externalId}:{sn}"
    )
    ASSET_MANUAL_CONTROL_REQUEST = "zqnt:asset-manual-control-request:"
    SUBASSET_AT_HOME = "zqnt:subaset-at-home:"  # intentional typo – matches Java
    ASSET_SUBASSET_REFERENCE = "zqnt:asset-subasset-reference:"
    ASSET_PROPERTIES = "zqnt:asset-properties:"
    ASSET_DTO = "zqnt:asset-dto:{sn}"
    SUBASSET_DTO = "zqnt:subasset-dto:{subAssetSn}"
    EDGE_ENDPOINTS = "zqnt:edge-endpoints:{vendor}"
    EDGE_VENDOR = "zqnt:edge-vendor:{sn}"
    ASSET_CURRENT_TASK = "zqnt:asset-current-task:{sn}"

    def build(self, **kwargs: str) -> str:
        """
        Return the final Redis key with all placeholders replaced.

        Simple keys (no placeholders) can be called without arguments;
        the trailing ``:`` is kept intentionally — append the id yourself::

            CacheKeys.ASSET_ONLINE.build() + device_sn
            # → "zqnt:asset-online:DOCK001"
        """
        return self.value.format(**kwargs)
