from zqnt_utils.generated.zqnt.airspace.v3 import no_fly_zone_pb2 as _no_fly_zone_pb2
from zqnt_utils.generated.zqnt.common.v3 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Verdict(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VERDICT_UNSPECIFIED: _ClassVar[Verdict]
    VERDICT_CLEAR: _ClassVar[Verdict]
    VERDICT_ADVISORY: _ClassVar[Verdict]
    VERDICT_REQUIRES_APPROVAL: _ClassVar[Verdict]
    VERDICT_BLOCKED: _ClassVar[Verdict]
VERDICT_UNSPECIFIED: Verdict
VERDICT_CLEAR: Verdict
VERDICT_ADVISORY: Verdict
VERDICT_REQUIRES_APPROVAL: Verdict
VERDICT_BLOCKED: Verdict

class CheckFlightPathRequest(_message.Message):
    __slots__ = ("context", "asset", "command_id", "destination")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    asset: _common_pb2.AssetRef
    command_id: str
    destination: _common_pb2.GeoPoint
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., asset: _Optional[_Union[_common_pb2.AssetRef, _Mapping]] = ..., command_id: _Optional[str] = ..., destination: _Optional[_Union[_common_pb2.GeoPoint, _Mapping]] = ...) -> None: ...

class ZoneHit(_message.Message):
    __slots__ = ("zone_id", "zone_name", "enforcement", "destination_inside")
    ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_NAME_FIELD_NUMBER: _ClassVar[int]
    ENFORCEMENT_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_INSIDE_FIELD_NUMBER: _ClassVar[int]
    zone_id: str
    zone_name: str
    enforcement: _no_fly_zone_pb2.Enforcement
    destination_inside: bool
    def __init__(self, zone_id: _Optional[str] = ..., zone_name: _Optional[str] = ..., enforcement: _Optional[_Union[_no_fly_zone_pb2.Enforcement, str]] = ..., destination_inside: bool = ...) -> None: ...

class CheckFlightPathResponse(_message.Message):
    __slots__ = ("verdict", "summary", "zones", "reroute", "position_known")
    VERDICT_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    ZONES_FIELD_NUMBER: _ClassVar[int]
    REROUTE_FIELD_NUMBER: _ClassVar[int]
    POSITION_KNOWN_FIELD_NUMBER: _ClassVar[int]
    verdict: Verdict
    summary: str
    zones: _containers.RepeatedCompositeFieldContainer[ZoneHit]
    reroute: _containers.RepeatedCompositeFieldContainer[_common_pb2.GeoPoint]
    position_known: bool
    def __init__(self, verdict: _Optional[_Union[Verdict, str]] = ..., summary: _Optional[str] = ..., zones: _Optional[_Iterable[_Union[ZoneHit, _Mapping]]] = ..., reroute: _Optional[_Iterable[_Union[_common_pb2.GeoPoint, _Mapping]]] = ..., position_known: bool = ...) -> None: ...
