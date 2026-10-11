# zqnt-utils

Shared utilities for ZQNT services and adapters. Published to GitHub Packages (private registry).

Since the public/internal split of the contracts, `zqnt_utils.generated` holds only the
**internal** contracts. The public contracts (`zqnt_api.generated...`), the telemetry mapping
(`zqnt_api.telemetry`), `zqnt_api.proto_utils` and `EdgeEndpointDTO` (`zqnt_api.core`, re-exported by
`zqnt_utils.core`) come from [`zqnt-api`](https://github.com/Zequent/zqnt-api-python), a dependency
of this package. Never import the same contract from both packages.

## Installation

Das Package wird als `.whl`-Datei über [GitHub Releases](https://github.com/ZEQUENT_ORG/zqnt-utils-python/releases) verteilt. Kein Package-Registry-Token nötig — nur Zugriff auf das Repository.

### Stable Release

```bash
uv add "zqnt-utils @ https://github.com/ZEQUENT_ORG/zqnt-utils-python/releases/download/v0.1.0/zqnt_utils-0.1.0-py3-none-any.whl"
```

### Als Abhängigkeit im Projekt (`pyproject.toml`)

```toml
[project]
dependencies = [
    "zqnt-utils @ https://github.com/ZEQUENT_ORG/zqnt-utils-python/releases/download/v0.1.0/zqnt_utils-0.1.0-py3-none-any.whl",
]
```

### Pre-release (aus PR)

Der PR-Kommentar enthält den genauen Install-Befehl, z.B.:

```bash
uv add "zqnt-utils @ https://github.com/ZEQUENT_ORG/zqnt-utils-python/releases/download/v0.1.0.post42.devABC123/zqnt_utils-0.1.0.post42.devABC123-py3-none-any.whl"
```

---

## Verwendung

```python
from zqnt_utils.caching import CachingService, CacheKeys
from zqnt_utils.core import EdgeEndpointDTO
```

### CachingService

Async Redis-Client, der den Java `CachingService` spiegelt.

**Kurzlebig (context manager):**

```python
async with CachingService("redis://localhost:6379") as cache:
    await cache.register_edge_endpoint("DJI", dto)
```

**Langlebig (Adapter-Lifecycle):**

```python
cache = CachingService.from_env()   # liest REDIS_URL aus der Umgebung
await cache.connect()

await cache.register_edge_endpoint("DJI", dto)
await cache.register_asset_vendor("SN-001", "DJI")

await cache.close()
```

### EdgeEndpointDTO

Spiegelt das Java `EdgeEndpointDTO` und serialisiert in dasselbe JSON-Format:

```python
dto = EdgeEndpointDTO(
    endpoint="grpc://adapter.internal:50051",
    online=True,
    asset_type="DOCK",
    asset_vendor="DJI",
)

json_str = dto.to_json()
dto2 = EdgeEndpointDTO.from_json(json_str)
```

### Verfügbare Operationen

| Methode | Beschreibung |
|---|---|
| `register_edge_endpoint(vendor, dto)` | Edge-Endpoint registrieren |
| `get_edge_endpoint(vendor)` | Edge-Endpoint abrufen |
| `deregister_edge_endpoint(vendor)` | Endpoint als offline markieren |
| `delete_edge_endpoint(vendor)` | Endpoint vollständig löschen |
| `register_asset_vendor(sn, vendor)` | Asset-SN → Vendor mappen |
| `get_asset_vendor(sn)` | Vendor für eine Asset-SN abrufen |
| `set(key, value)` | Generisches Redis SET |
| `setex(key, ttl, value)` | Redis SET mit TTL |
| `get(key)` | Generisches Redis GET |
| `delete(*keys)` | Redis DEL |

---

## Umgebungsvariablen

| Variable | Standard | Beschreibung |
|---|---|---|
| `REDIS_URL` | `redis://localhost:6379` | Redis-Verbindungs-URL |
