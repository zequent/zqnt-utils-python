import datetime

from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
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

class GeoPosition(_message.Message):
    __slots__ = ("latitude", "longitude", "altitude_meters")
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    ALTITUDE_METERS_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float
    altitude_meters: float
    def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., altitude_meters: _Optional[float] = ...) -> None: ...

class Device(_message.Message):
    __slots__ = ("sn", "home", "position", "heading_degrees", "battery_percent", "mode", "manual_control_active", "added_at", "kind", "sensor", "running", "name", "link_connected", "sensor_mode", "organization_id")
    SN_FIELD_NUMBER: _ClassVar[int]
    HOME_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    HEADING_DEGREES_FIELD_NUMBER: _ClassVar[int]
    BATTERY_PERCENT_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    MANUAL_CONTROL_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    ADDED_AT_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    SENSOR_FIELD_NUMBER: _ClassVar[int]
    RUNNING_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LINK_CONNECTED_FIELD_NUMBER: _ClassVar[int]
    SENSOR_MODE_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    sn: str
    home: GeoPosition
    position: GeoPosition
    heading_degrees: float
    battery_percent: float
    mode: DeviceMode
    manual_control_active: bool
    added_at: _timestamp_pb2.Timestamp
    kind: DeviceKind
    sensor: SensorSettings
    running: bool
    name: str
    link_connected: bool
    sensor_mode: str
    organization_id: str
    def __init__(self, sn: _Optional[str] = ..., home: _Optional[_Union[GeoPosition, _Mapping]] = ..., position: _Optional[_Union[GeoPosition, _Mapping]] = ..., heading_degrees: _Optional[float] = ..., battery_percent: _Optional[float] = ..., mode: _Optional[_Union[DeviceMode, str]] = ..., manual_control_active: bool = ..., added_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., kind: _Optional[_Union[DeviceKind, str]] = ..., sensor: _Optional[_Union[SensorSettings, _Mapping]] = ..., running: bool = ..., name: _Optional[str] = ..., link_connected: bool = ..., sensor_mode: _Optional[str] = ..., organization_id: _Optional[str] = ...) -> None: ...

class AddDeviceRequest(_message.Message):
    __slots__ = ("sn", "home", "kind", "sensor", "name", "start", "organization_id")
    SN_FIELD_NUMBER: _ClassVar[int]
    HOME_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    SENSOR_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    sn: str
    home: GeoPosition
    kind: DeviceKind
    sensor: SensorSettings
    name: str
    start: bool
    organization_id: str
    def __init__(self, sn: _Optional[str] = ..., home: _Optional[_Union[GeoPosition, _Mapping]] = ..., kind: _Optional[_Union[DeviceKind, str]] = ..., sensor: _Optional[_Union[SensorSettings, _Mapping]] = ..., name: _Optional[str] = ..., start: bool = ..., organization_id: _Optional[str] = ...) -> None: ...

class StartDeviceRequest(_message.Message):
    __slots__ = ("sn",)
    SN_FIELD_NUMBER: _ClassVar[int]
    sn: str
    def __init__(self, sn: _Optional[str] = ...) -> None: ...

class StopDeviceRequest(_message.Message):
    __slots__ = ("sn",)
    SN_FIELD_NUMBER: _ClassVar[int]
    sn: str
    def __init__(self, sn: _Optional[str] = ...) -> None: ...

class Preset(_message.Message):
    __slots__ = ("id", "name", "description", "devices")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    devices: _containers.RepeatedCompositeFieldContainer[AddDeviceRequest]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., devices: _Optional[_Iterable[_Union[AddDeviceRequest, _Mapping]]] = ...) -> None: ...

class ListPresetsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListPresetsResponse(_message.Message):
    __slots__ = ("presets",)
    PRESETS_FIELD_NUMBER: _ClassVar[int]
    presets: _containers.RepeatedCompositeFieldContainer[Preset]
    def __init__(self, presets: _Optional[_Iterable[_Union[Preset, _Mapping]]] = ...) -> None: ...

class LoadPresetRequest(_message.Message):
    __slots__ = ("id", "organization_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    organization_id: str
    def __init__(self, id: _Optional[str] = ..., organization_id: _Optional[str] = ...) -> None: ...

class RemoveDeviceRequest(_message.Message):
    __slots__ = ("sn",)
    SN_FIELD_NUMBER: _ClassVar[int]
    sn: str
    def __init__(self, sn: _Optional[str] = ...) -> None: ...

class GetDeviceRequest(_message.Message):
    __slots__ = ("sn",)
    SN_FIELD_NUMBER: _ClassVar[int]
    sn: str
    def __init__(self, sn: _Optional[str] = ...) -> None: ...

class ListDevicesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListDevicesResponse(_message.Message):
    __slots__ = ("devices",)
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    devices: _containers.RepeatedCompositeFieldContainer[Device]
    def __init__(self, devices: _Optional[_Iterable[_Union[Device, _Mapping]]] = ...) -> None: ...
