import datetime

from . import common_pb2 as _common_pb2
from . import base_pb2 as _base_pb2
from . import asset_pb2 as _asset_pb2
from . import device_control_contracts_pb2 as _device_control_contracts_pb2
from . import detection_pb2 as _detection_pb2
from . import mission_autonomy_types_pb2 as _mission_autonomy_types_pb2
from . import mission_autonomy_dto_pb2 as _mission_autonomy_dto_pb2
from . import capability_execution_contracts_pb2 as _capability_execution_contracts_pb2
from . import mission_autonomy_contracts_pb2 as _mission_autonomy_contracts_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EvaluateDetectionRequest(_message.Message):
    __slots__ = ("base", "detection_id", "asset_sn", "object_type", "confidence", "detection_latitude", "detection_longitude", "detection_altitude", "organization_id", "runtime_config", "theatre_id", "capability_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    DETECTION_ID_FIELD_NUMBER: _ClassVar[int]
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    DETECTION_LATITUDE_FIELD_NUMBER: _ClassVar[int]
    DETECTION_LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    DETECTION_ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_CONFIG_FIELD_NUMBER: _ClassVar[int]
    THEATRE_ID_FIELD_NUMBER: _ClassVar[int]
    CAPABILITY_ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    detection_id: str
    asset_sn: str
    object_type: str
    confidence: float
    detection_latitude: float
    detection_longitude: float
    detection_altitude: float
    organization_id: str
    runtime_config: _mission_autonomy_types_pb2.DynamicConfigProto
    theatre_id: str
    capability_id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., detection_id: _Optional[str] = ..., asset_sn: _Optional[str] = ..., object_type: _Optional[str] = ..., confidence: _Optional[float] = ..., detection_latitude: _Optional[float] = ..., detection_longitude: _Optional[float] = ..., detection_altitude: _Optional[float] = ..., organization_id: _Optional[str] = ..., runtime_config: _Optional[_Union[_mission_autonomy_types_pb2.DynamicConfigProto, _Mapping]] = ..., theatre_id: _Optional[str] = ..., capability_id: _Optional[str] = ...) -> None: ...

class DecisionResultProto(_message.Message):
    __slots__ = ("decision_id", "detection_id", "selected_asset_sn", "strategy_used", "status", "considered_asset_sns", "rejection_reasons", "decided_at", "resolved_config", "selected_actions")
    class RejectionReasonsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    DECISION_ID_FIELD_NUMBER: _ClassVar[int]
    DETECTION_ID_FIELD_NUMBER: _ClassVar[int]
    SELECTED_ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    STRATEGY_USED_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CONSIDERED_ASSET_SNS_FIELD_NUMBER: _ClassVar[int]
    REJECTION_REASONS_FIELD_NUMBER: _ClassVar[int]
    DECIDED_AT_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SELECTED_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    decision_id: str
    detection_id: str
    selected_asset_sn: str
    strategy_used: str
    status: str
    considered_asset_sns: _containers.RepeatedScalarFieldContainer[str]
    rejection_reasons: _containers.ScalarMap[str, str]
    decided_at: _timestamp_pb2.Timestamp
    resolved_config: _mission_autonomy_types_pb2.DynamicConfigProto
    selected_actions: _containers.RepeatedCompositeFieldContainer[_mission_autonomy_types_pb2.DecisionActionProto]
    def __init__(self, decision_id: _Optional[str] = ..., detection_id: _Optional[str] = ..., selected_asset_sn: _Optional[str] = ..., strategy_used: _Optional[str] = ..., status: _Optional[str] = ..., considered_asset_sns: _Optional[_Iterable[str]] = ..., rejection_reasons: _Optional[_Mapping[str, str]] = ..., decided_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., resolved_config: _Optional[_Union[_mission_autonomy_types_pb2.DynamicConfigProto, _Mapping]] = ..., selected_actions: _Optional[_Iterable[_Union[_mission_autonomy_types_pb2.DecisionActionProto, _Mapping]]] = ...) -> None: ...

class DecisionResponse(_message.Message):
    __slots__ = ("has_errors", "tid", "timestamp", "error", "decision_result")
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DECISION_RESULT_FIELD_NUMBER: _ClassVar[int]
    has_errors: bool
    tid: str
    timestamp: _timestamp_pb2.Timestamp
    error: _base_pb2.GlobalErrorMessage
    decision_result: DecisionResultProto
    def __init__(self, has_errors: bool = ..., tid: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ..., decision_result: _Optional[_Union[DecisionResultProto, _Mapping]] = ...) -> None: ...
