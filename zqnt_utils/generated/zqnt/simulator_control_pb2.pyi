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

class DeviceMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEVICE_MODE_UNSPECIFIED: _ClassVar[DeviceMode]
    DEVICE_MODE_DOCKED: _ClassVar[DeviceMode]
    DEVICE_MODE_FLYING: _ClassVar[DeviceMode]
    DEVICE_MODE_RETURNING: _ClassVar[DeviceMode]
DEVICE_MODE_UNSPECIFIED: DeviceMode
DEVICE_MODE_DOCKED: DeviceMode
DEVICE_MODE_FLYING: DeviceMode
DEVICE_MODE_RETURNING: DeviceMode

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
    __slots__ = ("sn", "home", "position", "heading_degrees", "battery_percent", "mode", "manual_control_active", "added_at")
    SN_FIELD_NUMBER: _ClassVar[int]
    HOME_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    HEADING_DEGREES_FIELD_NUMBER: _ClassVar[int]
    BATTERY_PERCENT_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    MANUAL_CONTROL_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    ADDED_AT_FIELD_NUMBER: _ClassVar[int]
    sn: str
    home: GeoPosition
    position: GeoPosition
    heading_degrees: float
    battery_percent: float
    mode: DeviceMode
    manual_control_active: bool
    added_at: _timestamp_pb2.Timestamp
    def __init__(self, sn: _Optional[str] = ..., home: _Optional[_Union[GeoPosition, _Mapping]] = ..., position: _Optional[_Union[GeoPosition, _Mapping]] = ..., heading_degrees: _Optional[float] = ..., battery_percent: _Optional[float] = ..., mode: _Optional[_Union[DeviceMode, str]] = ..., manual_control_active: bool = ..., added_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AddDeviceRequest(_message.Message):
    __slots__ = ("sn", "home")
    SN_FIELD_NUMBER: _ClassVar[int]
    HOME_FIELD_NUMBER: _ClassVar[int]
    sn: str
    home: GeoPosition
    def __init__(self, sn: _Optional[str] = ..., home: _Optional[_Union[GeoPosition, _Mapping]] = ...) -> None: ...

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
