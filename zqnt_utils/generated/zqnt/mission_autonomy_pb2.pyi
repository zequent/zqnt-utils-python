import datetime

from . import common_pb2 as _common_pb2
from . import base_pb2 as _base_pb2
from . import asset_pb2 as _asset_pb2
from . import device_control_contracts_pb2 as _device_control_contracts_pb2
from . import detection_pb2 as _detection_pb2
from . import mission_autonomy_types_pb2 as _mission_autonomy_types_pb2
from . import mission_autonomy_dto_pb2 as _mission_autonomy_dto_pb2
from . import mission_autonomy_contracts_pb2 as _mission_autonomy_contracts_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EvaluateAutonomyRequest(_message.Message):
    __slots__ = ("base", "mission_id", "mission_context", "candidate_tasks", "trigger", "runtime_config", "runtime_context")
    BASE_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    MISSION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_TASKS_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    mission_id: str
    mission_context: _mission_autonomy_dto_pb2.MissionProtoDTO
    candidate_tasks: _containers.RepeatedCompositeFieldContainer[_mission_autonomy_dto_pb2.TaskProtoDTO]
    trigger: _mission_autonomy_types_pb2.DecisionTriggerProto
    runtime_config: _mission_autonomy_types_pb2.DynamicConfigProto
    runtime_context: _struct_pb2.Struct
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., mission_id: _Optional[str] = ..., mission_context: _Optional[_Union[_mission_autonomy_dto_pb2.MissionProtoDTO, _Mapping]] = ..., candidate_tasks: _Optional[_Iterable[_Union[_mission_autonomy_dto_pb2.TaskProtoDTO, _Mapping]]] = ..., trigger: _Optional[_Union[_mission_autonomy_types_pb2.DecisionTriggerProto, _Mapping]] = ..., runtime_config: _Optional[_Union[_mission_autonomy_types_pb2.DynamicConfigProto, _Mapping]] = ..., runtime_context: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class EvaluateDetectionRequest(_message.Message):
    __slots__ = ("base", "detection_id", "asset_sn", "object_type", "confidence", "detection_latitude", "detection_longitude", "detection_altitude", "mission_id", "organization_id", "mission_context", "task_context", "runtime_config")
    BASE_FIELD_NUMBER: _ClassVar[int]
    DETECTION_ID_FIELD_NUMBER: _ClassVar[int]
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    DETECTION_LATITUDE_FIELD_NUMBER: _ClassVar[int]
    DETECTION_LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    DETECTION_ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    MISSION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    TASK_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_CONFIG_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    detection_id: str
    asset_sn: str
    object_type: str
    confidence: float
    detection_latitude: float
    detection_longitude: float
    detection_altitude: float
    mission_id: str
    organization_id: str
    mission_context: _mission_autonomy_dto_pb2.MissionProtoDTO
    task_context: _mission_autonomy_dto_pb2.TaskProtoDTO
    runtime_config: _mission_autonomy_types_pb2.DynamicConfigProto
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., detection_id: _Optional[str] = ..., asset_sn: _Optional[str] = ..., object_type: _Optional[str] = ..., confidence: _Optional[float] = ..., detection_latitude: _Optional[float] = ..., detection_longitude: _Optional[float] = ..., detection_altitude: _Optional[float] = ..., mission_id: _Optional[str] = ..., organization_id: _Optional[str] = ..., mission_context: _Optional[_Union[_mission_autonomy_dto_pb2.MissionProtoDTO, _Mapping]] = ..., task_context: _Optional[_Union[_mission_autonomy_dto_pb2.TaskProtoDTO, _Mapping]] = ..., runtime_config: _Optional[_Union[_mission_autonomy_types_pb2.DynamicConfigProto, _Mapping]] = ...) -> None: ...

class AutonomyEvaluationResultProto(_message.Message):
    __slots__ = ("evaluation_id", "mission_id", "selected_task_id", "selected_actions", "resolved_mission_config", "resolved_task_config", "matched_rule_ids", "strategy_used", "status", "evaluated_at")
    EVALUATION_ID_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    SELECTED_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    SELECTED_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_MISSION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_TASK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MATCHED_RULE_IDS_FIELD_NUMBER: _ClassVar[int]
    STRATEGY_USED_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EVALUATED_AT_FIELD_NUMBER: _ClassVar[int]
    evaluation_id: str
    mission_id: str
    selected_task_id: str
    selected_actions: _containers.RepeatedCompositeFieldContainer[_mission_autonomy_types_pb2.DecisionActionProto]
    resolved_mission_config: _mission_autonomy_types_pb2.DynamicConfigProto
    resolved_task_config: _mission_autonomy_types_pb2.DynamicConfigProto
    matched_rule_ids: _containers.RepeatedScalarFieldContainer[str]
    strategy_used: str
    status: str
    evaluated_at: _timestamp_pb2.Timestamp
    def __init__(self, evaluation_id: _Optional[str] = ..., mission_id: _Optional[str] = ..., selected_task_id: _Optional[str] = ..., selected_actions: _Optional[_Iterable[_Union[_mission_autonomy_types_pb2.DecisionActionProto, _Mapping]]] = ..., resolved_mission_config: _Optional[_Union[_mission_autonomy_types_pb2.DynamicConfigProto, _Mapping]] = ..., resolved_task_config: _Optional[_Union[_mission_autonomy_types_pb2.DynamicConfigProto, _Mapping]] = ..., matched_rule_ids: _Optional[_Iterable[str]] = ..., strategy_used: _Optional[str] = ..., status: _Optional[str] = ..., evaluated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class DecisionResultProto(_message.Message):
    __slots__ = ("decision_id", "detection_id", "selected_asset_sn", "strategy_used", "status", "considered_asset_sns", "rejection_reasons", "decided_at", "selected_mission_id", "selected_task_id", "resolved_config", "selected_actions")
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
    SELECTED_MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    SELECTED_TASK_ID_FIELD_NUMBER: _ClassVar[int]
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
    selected_mission_id: str
    selected_task_id: str
    resolved_config: _mission_autonomy_types_pb2.DynamicConfigProto
    selected_actions: _containers.RepeatedCompositeFieldContainer[_mission_autonomy_types_pb2.DecisionActionProto]
    def __init__(self, decision_id: _Optional[str] = ..., detection_id: _Optional[str] = ..., selected_asset_sn: _Optional[str] = ..., strategy_used: _Optional[str] = ..., status: _Optional[str] = ..., considered_asset_sns: _Optional[_Iterable[str]] = ..., rejection_reasons: _Optional[_Mapping[str, str]] = ..., decided_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., selected_mission_id: _Optional[str] = ..., selected_task_id: _Optional[str] = ..., resolved_config: _Optional[_Union[_mission_autonomy_types_pb2.DynamicConfigProto, _Mapping]] = ..., selected_actions: _Optional[_Iterable[_Union[_mission_autonomy_types_pb2.DecisionActionProto, _Mapping]]] = ...) -> None: ...

class AutonomyEvaluationResponse(_message.Message):
    __slots__ = ("has_errors", "tid", "timestamp", "error", "evaluation_result")
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_RESULT_FIELD_NUMBER: _ClassVar[int]
    has_errors: bool
    tid: str
    timestamp: _timestamp_pb2.Timestamp
    error: _base_pb2.GlobalErrorMessage
    evaluation_result: AutonomyEvaluationResultProto
    def __init__(self, has_errors: bool = ..., tid: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ..., evaluation_result: _Optional[_Union[AutonomyEvaluationResultProto, _Mapping]] = ...) -> None: ...

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
