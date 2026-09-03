import datetime

from . import common_pb2 as _common_pb2
from . import base_pb2 as _base_pb2
from . import asset_pb2 as _asset_pb2
from . import device_control_contracts_pb2 as _device_control_contracts_pb2
from . import detection_pb2 as _detection_pb2
from . import mission_autonomy_types_pb2 as _mission_autonomy_types_pb2
from . import mission_autonomy_dto_pb2 as _mission_autonomy_dto_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotificationEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NOTIFICATION_EVENT_UNSPECIFIED: _ClassVar[NotificationEventType]
    NOTIFICATION_EVENT_ASSET_STATUS: _ClassVar[NotificationEventType]
    NOTIFICATION_EVENT_TASK: _ClassVar[NotificationEventType]
    NOTIFICATION_EVENT_MISSION: _ClassVar[NotificationEventType]
    NOTIFICATION_EVENT_ASSET_RUNTIME: _ClassVar[NotificationEventType]

class NotificationSeverity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NOTIFICATION_SEVERITY_INFO: _ClassVar[NotificationSeverity]
    NOTIFICATION_SEVERITY_WARN: _ClassVar[NotificationSeverity]
    NOTIFICATION_SEVERITY_CRITICAL: _ClassVar[NotificationSeverity]

class NotificationSourceState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NOTIFICATION_SOURCE_STATE_UNSPECIFIED: _ClassVar[NotificationSourceState]
    NOTIFICATION_SOURCE_STATE_ONLINE: _ClassVar[NotificationSourceState]
    NOTIFICATION_SOURCE_STATE_STALE: _ClassVar[NotificationSourceState]
    NOTIFICATION_SOURCE_STATE_NO_DATA: _ClassVar[NotificationSourceState]
NOTIFICATION_EVENT_UNSPECIFIED: NotificationEventType
NOTIFICATION_EVENT_ASSET_STATUS: NotificationEventType
NOTIFICATION_EVENT_TASK: NotificationEventType
NOTIFICATION_EVENT_MISSION: NotificationEventType
NOTIFICATION_EVENT_ASSET_RUNTIME: NotificationEventType
NOTIFICATION_SEVERITY_INFO: NotificationSeverity
NOTIFICATION_SEVERITY_WARN: NotificationSeverity
NOTIFICATION_SEVERITY_CRITICAL: NotificationSeverity
NOTIFICATION_SOURCE_STATE_UNSPECIFIED: NotificationSourceState
NOTIFICATION_SOURCE_STATE_ONLINE: NotificationSourceState
NOTIFICATION_SOURCE_STATE_STALE: NotificationSourceState
NOTIFICATION_SOURCE_STATE_NO_DATA: NotificationSourceState

class NotificationStreamHeartbeat(_message.Message):
    __slots__ = ("timestamp",)
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class NotificationSourceStatus(_message.Message):
    __slots__ = ("sn", "state", "observed_at", "last_notification_at")
    SN_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_NOTIFICATION_AT_FIELD_NUMBER: _ClassVar[int]
    sn: str
    state: NotificationSourceState
    observed_at: _timestamp_pb2.Timestamp
    last_notification_at: _timestamp_pb2.Timestamp
    def __init__(self, sn: _Optional[str] = ..., state: _Optional[_Union[NotificationSourceState, str]] = ..., observed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_notification_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AssetStatusEvent(_message.Message):
    __slots__ = ("sn", "asset_id", "online", "message")
    SN_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    ONLINE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    sn: str
    asset_id: str
    online: bool
    message: str
    def __init__(self, sn: _Optional[str] = ..., asset_id: _Optional[str] = ..., online: bool = ..., message: _Optional[str] = ...) -> None: ...

class TaskEvent(_message.Message):
    __slots__ = ("task_id", "task_type", "status", "progress", "message", "external_task_type")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_TASK_TYPE_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    task_type: _mission_autonomy_types_pb2.TaskTypeProto
    status: _mission_autonomy_types_pb2.TaskStatus
    progress: float
    message: str
    external_task_type: str
    def __init__(self, task_id: _Optional[str] = ..., task_type: _Optional[_Union[_mission_autonomy_types_pb2.TaskTypeProto, str]] = ..., status: _Optional[_Union[_mission_autonomy_types_pb2.TaskStatus, str]] = ..., progress: _Optional[float] = ..., message: _Optional[str] = ..., external_task_type: _Optional[str] = ...) -> None: ...

class MissionEvent(_message.Message):
    __slots__ = ("mission_id", "mission_type", "status", "message")
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    MISSION_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    mission_id: str
    mission_type: _mission_autonomy_types_pb2.MissionType
    status: _mission_autonomy_types_pb2.MissionStatus
    message: str
    def __init__(self, mission_id: _Optional[str] = ..., mission_type: _Optional[_Union[_mission_autonomy_types_pb2.MissionType, str]] = ..., status: _Optional[_Union[_mission_autonomy_types_pb2.MissionStatus, str]] = ..., message: _Optional[str] = ...) -> None: ...

class AssetRuntimeEvent(_message.Message):
    __slots__ = ("sn", "asset_id", "revision", "observed_at", "valid_until", "snapshot_state")
    SN_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_AT_FIELD_NUMBER: _ClassVar[int]
    VALID_UNTIL_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_STATE_FIELD_NUMBER: _ClassVar[int]
    sn: str
    asset_id: str
    revision: str
    observed_at: _timestamp_pb2.Timestamp
    valid_until: _timestamp_pb2.Timestamp
    snapshot_state: _device_control_contracts_pb2.CapabilitySnapshotState
    def __init__(self, sn: _Optional[str] = ..., asset_id: _Optional[str] = ..., revision: _Optional[str] = ..., observed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., valid_until: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., snapshot_state: _Optional[_Union[_device_control_contracts_pb2.CapabilitySnapshotState, str]] = ...) -> None: ...

class NotificationEvent(_message.Message):
    __slots__ = ("asset_status", "task", "mission", "error", "asset_runtime")
    ASSET_STATUS_FIELD_NUMBER: _ClassVar[int]
    TASK_FIELD_NUMBER: _ClassVar[int]
    MISSION_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ASSET_RUNTIME_FIELD_NUMBER: _ClassVar[int]
    asset_status: AssetStatusEvent
    task: TaskEvent
    mission: MissionEvent
    error: _base_pb2.GlobalErrorMessage
    asset_runtime: AssetRuntimeEvent
    def __init__(self, asset_status: _Optional[_Union[AssetStatusEvent, _Mapping]] = ..., task: _Optional[_Union[TaskEvent, _Mapping]] = ..., mission: _Optional[_Union[MissionEvent, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ..., asset_runtime: _Optional[_Union[AssetRuntimeEvent, _Mapping]] = ...) -> None: ...

class StreamNotificationsRequest(_message.Message):
    __slots__ = ("base", "event_types")
    BASE_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPES_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    event_types: _containers.RepeatedScalarFieldContainer[NotificationEventType]
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., event_types: _Optional[_Iterable[_Union[NotificationEventType, str]]] = ...) -> None: ...

class ProduceNotificationRequest(_message.Message):
    __slots__ = ("base", "event", "severity", "event_type")
    BASE_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    event: NotificationEvent
    severity: NotificationSeverity
    event_type: NotificationEventType
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., event: _Optional[_Union[NotificationEvent, _Mapping]] = ..., severity: _Optional[_Union[NotificationSeverity, str]] = ..., event_type: _Optional[_Union[NotificationEventType, str]] = ...) -> None: ...

class NotificationResponse(_message.Message):
    __slots__ = ("tid", "timestamp", "has_errors", "sn", "asset_id", "event", "stream_heartbeat", "source_status", "error")
    TID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    SN_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    STREAM_HEARTBEAT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    tid: str
    timestamp: _timestamp_pb2.Timestamp
    has_errors: bool
    sn: str
    asset_id: str
    event: NotificationEvent
    stream_heartbeat: NotificationStreamHeartbeat
    source_status: NotificationSourceStatus
    error: _base_pb2.GlobalErrorMessage
    def __init__(self, tid: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., has_errors: bool = ..., sn: _Optional[str] = ..., asset_id: _Optional[str] = ..., event: _Optional[_Union[NotificationEvent, _Mapping]] = ..., stream_heartbeat: _Optional[_Union[NotificationStreamHeartbeat, _Mapping]] = ..., source_status: _Optional[_Union[NotificationSourceStatus, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ...) -> None: ...
