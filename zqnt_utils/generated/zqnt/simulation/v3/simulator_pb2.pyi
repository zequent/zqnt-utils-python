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

class DeviceKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEVICE_KIND_UNSPECIFIED: _ClassVar[DeviceKind]
    DEVICE_KIND_DRONE: _ClassVar[DeviceKind]
    DEVICE_KIND_RADAR: _ClassVar[DeviceKind]
    DEVICE_KIND_JAMMER: _ClassVar[DeviceKind]

class DeviceMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEVICE_MODE_UNSPECIFIED: _ClassVar[DeviceMode]
    DEVICE_MODE_DOCKED: _ClassVar[DeviceMode]
    DEVICE_MODE_FLYING: _ClassVar[DeviceMode]
    DEVICE_MODE_RETURNING: _ClassVar[DeviceMode]
DEVICE_KIND_UNSPECIFIED: DeviceKind
DEVICE_KIND_DRONE: DeviceKind
DEVICE_KIND_RADAR: DeviceKind
DEVICE_KIND_JAMMER: DeviceKind
DEVICE_MODE_UNSPECIFIED: DeviceMode
DEVICE_MODE_DOCKED: DeviceMode
DEVICE_MODE_FLYING: DeviceMode
DEVICE_MODE_RETURNING: DeviceMode

class SensorSettings(_message.Message):
    __slots__ = ("azimuth_degrees", "sector_width_degrees", "beamwidth_degrees", "range_meters", "bands", "synthetic_detections")
    AZIMUTH_DEGREES_FIELD_NUMBER: _ClassVar[int]
    SECTOR_WIDTH_DEGREES_FIELD_NUMBER: _ClassVar[int]
    BEAMWIDTH_DEGREES_FIELD_NUMBER: _ClassVar[int]
    RANGE_METERS_FIELD_NUMBER: _ClassVar[int]
    BANDS_FIELD_NUMBER: _ClassVar[int]
    SYNTHETIC_DETECTIONS_FIELD_NUMBER: _ClassVar[int]
    azimuth_degrees: float
    sector_width_degrees: float
    beamwidth_degrees: float
    range_meters: float
    bands: _containers.RepeatedScalarFieldContainer[str]
    synthetic_detections: bool
    def __init__(self, azimuth_degrees: _Optional[float] = ..., sector_width_degrees: _Optional[float] = ..., beamwidth_degrees: _Optional[float] = ..., range_meters: _Optional[float] = ..., bands: _Optional[_Iterable[str]] = ..., synthetic_detections: bool = ...) -> None: ...

class DeviceSpec(_message.Message):
    __slots__ = ("sn", "name", "kind", "home", "sensor", "organization_id", "start")
    SN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    HOME_FIELD_NUMBER: _ClassVar[int]
    SENSOR_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    sn: str
    name: str
    kind: DeviceKind
    home: _common_pb2.GeoPoint
    sensor: SensorSettings
    organization_id: str
    start: bool
    def __init__(self, sn: _Optional[str] = ..., name: _Optional[str] = ..., kind: _Optional[_Union[DeviceKind, str]] = ..., home: _Optional[_Union[_common_pb2.GeoPoint, _Mapping]] = ..., sensor: _Optional[_Union[SensorSettings, _Mapping]] = ..., organization_id: _Optional[str] = ..., start: bool = ...) -> None: ...

class Device(_message.Message):
    __slots__ = ("spec", "position", "heading_degrees", "battery_percent", "mode", "manual_control_active", "running", "link_connected", "sensor_mode", "added_at")
    SPEC_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    HEADING_DEGREES_FIELD_NUMBER: _ClassVar[int]
    BATTERY_PERCENT_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    MANUAL_CONTROL_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    RUNNING_FIELD_NUMBER: _ClassVar[int]
    LINK_CONNECTED_FIELD_NUMBER: _ClassVar[int]
    SENSOR_MODE_FIELD_NUMBER: _ClassVar[int]
    ADDED_AT_FIELD_NUMBER: _ClassVar[int]
    spec: DeviceSpec
    position: _common_pb2.GeoPoint
    heading_degrees: float
    battery_percent: float
    mode: DeviceMode
    manual_control_active: bool
    running: bool
    link_connected: bool
    sensor_mode: str
    added_at: _timestamp_pb2.Timestamp
    def __init__(self, spec: _Optional[_Union[DeviceSpec, _Mapping]] = ..., position: _Optional[_Union[_common_pb2.GeoPoint, _Mapping]] = ..., heading_degrees: _Optional[float] = ..., battery_percent: _Optional[float] = ..., mode: _Optional[_Union[DeviceMode, str]] = ..., manual_control_active: bool = ..., running: bool = ..., link_connected: bool = ..., sensor_mode: _Optional[str] = ..., added_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Preset(_message.Message):
    __slots__ = ("id", "name", "description", "devices")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    devices: _containers.RepeatedCompositeFieldContainer[DeviceSpec]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., devices: _Optional[_Iterable[_Union[DeviceSpec, _Mapping]]] = ...) -> None: ...

class AddDeviceRequest(_message.Message):
    __slots__ = ("context", "device")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    device: DeviceSpec
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., device: _Optional[_Union[DeviceSpec, _Mapping]] = ...) -> None: ...

class AddDeviceResponse(_message.Message):
    __slots__ = ("device",)
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    device: Device
    def __init__(self, device: _Optional[_Union[Device, _Mapping]] = ...) -> None: ...

class RemoveDeviceRequest(_message.Message):
    __slots__ = ("context", "sn")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SN_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    sn: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., sn: _Optional[str] = ...) -> None: ...

class RemoveDeviceResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetDeviceRequest(_message.Message):
    __slots__ = ("context", "sn")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SN_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    sn: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., sn: _Optional[str] = ...) -> None: ...

class GetDeviceResponse(_message.Message):
    __slots__ = ("device",)
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    device: Device
    def __init__(self, device: _Optional[_Union[Device, _Mapping]] = ...) -> None: ...

class ListDevicesRequest(_message.Message):
    __slots__ = ("context",)
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ...) -> None: ...

class ListDevicesResponse(_message.Message):
    __slots__ = ("devices",)
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    devices: _containers.RepeatedCompositeFieldContainer[Device]
    def __init__(self, devices: _Optional[_Iterable[_Union[Device, _Mapping]]] = ...) -> None: ...

class StartDeviceRequest(_message.Message):
    __slots__ = ("context", "sn")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SN_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    sn: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., sn: _Optional[str] = ...) -> None: ...

class StartDeviceResponse(_message.Message):
    __slots__ = ("device",)
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    device: Device
    def __init__(self, device: _Optional[_Union[Device, _Mapping]] = ...) -> None: ...

class StopDeviceRequest(_message.Message):
    __slots__ = ("context", "sn")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SN_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    sn: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., sn: _Optional[str] = ...) -> None: ...

class StopDeviceResponse(_message.Message):
    __slots__ = ("device",)
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    device: Device
    def __init__(self, device: _Optional[_Union[Device, _Mapping]] = ...) -> None: ...

class ListPresetsRequest(_message.Message):
    __slots__ = ("context",)
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ...) -> None: ...

class ListPresetsResponse(_message.Message):
    __slots__ = ("presets",)
    PRESETS_FIELD_NUMBER: _ClassVar[int]
    presets: _containers.RepeatedCompositeFieldContainer[Preset]
    def __init__(self, presets: _Optional[_Iterable[_Union[Preset, _Mapping]]] = ...) -> None: ...

class LoadPresetRequest(_message.Message):
    __slots__ = ("context", "id", "organization_id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    id: str
    organization_id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., id: _Optional[str] = ..., organization_id: _Optional[str] = ...) -> None: ...

class LoadPresetResponse(_message.Message):
    __slots__ = ("devices",)
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    devices: _containers.RepeatedCompositeFieldContainer[Device]
    def __init__(self, devices: _Optional[_Iterable[_Union[Device, _Mapping]]] = ...) -> None: ...
