import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from zqnt_utils.generated.zqnt.common.v3 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Enforcement(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENFORCEMENT_UNSPECIFIED: _ClassVar[Enforcement]
    ENFORCEMENT_ADVISORY: _ClassVar[Enforcement]
    ENFORCEMENT_REQUIRE_APPROVAL: _ClassVar[Enforcement]
    ENFORCEMENT_HARD_BLOCK: _ClassVar[Enforcement]
ENFORCEMENT_UNSPECIFIED: Enforcement
ENFORCEMENT_ADVISORY: Enforcement
ENFORCEMENT_REQUIRE_APPROVAL: Enforcement
ENFORCEMENT_HARD_BLOCK: Enforcement

class NoFlyZone(_message.Message):
    __slots__ = ("id", "organization_id", "name", "vertices", "enforcement", "active", "priority", "site_id", "min_altitude_meters", "max_altitude_meters", "created_at", "modified_at", "modified_by")
    ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERTICES_FIELD_NUMBER: _ClassVar[int]
    ENFORCEMENT_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    MIN_ALTITUDE_METERS_FIELD_NUMBER: _ClassVar[int]
    MAX_ALTITUDE_METERS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_BY_FIELD_NUMBER: _ClassVar[int]
    id: str
    organization_id: str
    name: str
    vertices: _containers.RepeatedCompositeFieldContainer[_common_pb2.GeoPoint]
    enforcement: Enforcement
    active: bool
    priority: int
    site_id: str
    min_altitude_meters: float
    max_altitude_meters: float
    created_at: _timestamp_pb2.Timestamp
    modified_at: _timestamp_pb2.Timestamp
    modified_by: str
    def __init__(self, id: _Optional[str] = ..., organization_id: _Optional[str] = ..., name: _Optional[str] = ..., vertices: _Optional[_Iterable[_Union[_common_pb2.GeoPoint, _Mapping]]] = ..., enforcement: _Optional[_Union[Enforcement, str]] = ..., active: bool = ..., priority: _Optional[int] = ..., site_id: _Optional[str] = ..., min_altitude_meters: _Optional[float] = ..., max_altitude_meters: _Optional[float] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., modified_by: _Optional[str] = ...) -> None: ...

class ListNoFlyZonesRequest(_message.Message):
    __slots__ = ("context", "organization_id", "active_only")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_ONLY_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    organization_id: str
    active_only: bool
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., organization_id: _Optional[str] = ..., active_only: bool = ...) -> None: ...

class ListNoFlyZonesResponse(_message.Message):
    __slots__ = ("zones",)
    ZONES_FIELD_NUMBER: _ClassVar[int]
    zones: _containers.RepeatedCompositeFieldContainer[NoFlyZone]
    def __init__(self, zones: _Optional[_Iterable[_Union[NoFlyZone, _Mapping]]] = ...) -> None: ...

class UpsertNoFlyZoneRequest(_message.Message):
    __slots__ = ("context", "zone")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    zone: NoFlyZone
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., zone: _Optional[_Union[NoFlyZone, _Mapping]] = ...) -> None: ...

class UpsertNoFlyZoneResponse(_message.Message):
    __slots__ = ("zone",)
    ZONE_FIELD_NUMBER: _ClassVar[int]
    zone: NoFlyZone
    def __init__(self, zone: _Optional[_Union[NoFlyZone, _Mapping]] = ...) -> None: ...

class DeleteNoFlyZoneRequest(_message.Message):
    __slots__ = ("context", "id", "organization_id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    id: str
    organization_id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., id: _Optional[str] = ..., organization_id: _Optional[str] = ...) -> None: ...

class DeleteNoFlyZoneResponse(_message.Message):
    __slots__ = ("deleted",)
    DELETED_FIELD_NUMBER: _ClassVar[int]
    deleted: bool
    def __init__(self, deleted: bool = ...) -> None: ...
