import datetime

from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from zqnt_utils.generated.zqnt.application.v3 import application_pb2 as _application_pb2
from zqnt_utils.generated.zqnt.capability.v3 import capability_pb2 as _capability_pb2
from zqnt_utils.generated.zqnt.common.v3 import common_pb2 as _common_pb2
from zqnt_utils.generated.zqnt.execution.v3 import execution_stats_pb2 as _execution_stats_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExecutionEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXECUTION_EVENT_TYPE_UNSPECIFIED: _ClassVar[ExecutionEventType]
    EXECUTION_EVENT_TYPE_CREATED: _ClassVar[ExecutionEventType]
    EXECUTION_EVENT_TYPE_PLANNED: _ClassVar[ExecutionEventType]
    EXECUTION_EVENT_TYPE_STARTED: _ClassVar[ExecutionEventType]
    EXECUTION_EVENT_TYPE_NODE_STARTED: _ClassVar[ExecutionEventType]
    EXECUTION_EVENT_TYPE_NODE_PROGRESS: _ClassVar[ExecutionEventType]
    EXECUTION_EVENT_TYPE_NODE_COMPLETED: _ClassVar[ExecutionEventType]
    EXECUTION_EVENT_TYPE_NODE_FAILED: _ClassVar[ExecutionEventType]
    EXECUTION_EVENT_TYPE_PAUSED: _ClassVar[ExecutionEventType]
    EXECUTION_EVENT_TYPE_RESUMED: _ClassVar[ExecutionEventType]
    EXECUTION_EVENT_TYPE_BLOCKED: _ClassVar[ExecutionEventType]
    EXECUTION_EVENT_TYPE_COMPLETED: _ClassVar[ExecutionEventType]
    EXECUTION_EVENT_TYPE_FAILED: _ClassVar[ExecutionEventType]
    EXECUTION_EVENT_TYPE_CANCELLED: _ClassVar[ExecutionEventType]
    EXECUTION_EVENT_TYPE_WARNING: _ClassVar[ExecutionEventType]
    EXECUTION_EVENT_TYPE_SAFETY_ALERT: _ClassVar[ExecutionEventType]
EXECUTION_EVENT_TYPE_UNSPECIFIED: ExecutionEventType
EXECUTION_EVENT_TYPE_CREATED: ExecutionEventType
EXECUTION_EVENT_TYPE_PLANNED: ExecutionEventType
EXECUTION_EVENT_TYPE_STARTED: ExecutionEventType
EXECUTION_EVENT_TYPE_NODE_STARTED: ExecutionEventType
EXECUTION_EVENT_TYPE_NODE_PROGRESS: ExecutionEventType
EXECUTION_EVENT_TYPE_NODE_COMPLETED: ExecutionEventType
EXECUTION_EVENT_TYPE_NODE_FAILED: ExecutionEventType
EXECUTION_EVENT_TYPE_PAUSED: ExecutionEventType
EXECUTION_EVENT_TYPE_RESUMED: ExecutionEventType
EXECUTION_EVENT_TYPE_BLOCKED: ExecutionEventType
EXECUTION_EVENT_TYPE_COMPLETED: ExecutionEventType
EXECUTION_EVENT_TYPE_FAILED: ExecutionEventType
EXECUTION_EVENT_TYPE_CANCELLED: ExecutionEventType
EXECUTION_EVENT_TYPE_WARNING: ExecutionEventType
EXECUTION_EVENT_TYPE_SAFETY_ALERT: ExecutionEventType

class CommandRun(_message.Message):
    __slots__ = ("command_id", "target", "parameters", "expected_schema_version")
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    command_id: str
    target: _capability_pb2.Target
    parameters: _struct_pb2.Struct
    expected_schema_version: str
    def __init__(self, command_id: _Optional[str] = ..., target: _Optional[_Union[_capability_pb2.Target, _Mapping]] = ..., parameters: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., expected_schema_version: _Optional[str] = ...) -> None: ...

class SkillRun(_message.Message):
    __slots__ = ("application_id", "skill_id", "application_version", "parameters")
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_VERSION_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    application_id: str
    skill_id: str
    application_version: str
    parameters: _struct_pb2.Struct
    def __init__(self, application_id: _Optional[str] = ..., skill_id: _Optional[str] = ..., application_version: _Optional[str] = ..., parameters: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class ExecutionSpec(_message.Message):
    __slots__ = ("command", "skill")
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    SKILL_FIELD_NUMBER: _ClassVar[int]
    command: CommandRun
    skill: SkillRun
    def __init__(self, command: _Optional[_Union[CommandRun, _Mapping]] = ..., skill: _Optional[_Union[SkillRun, _Mapping]] = ...) -> None: ...

class ExecutionOptions(_message.Message):
    __slots__ = ("dry_run", "validate_only", "auto_start", "priority", "timeout_seconds", "failure_strategy", "retry_policy", "config_overrides", "no_fly_zone_override")
    DRY_RUN_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    AUTO_START_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    RETRY_POLICY_FIELD_NUMBER: _ClassVar[int]
    CONFIG_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    NO_FLY_ZONE_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    dry_run: bool
    validate_only: bool
    auto_start: bool
    priority: int
    timeout_seconds: int
    failure_strategy: _application_pb2.FailureStrategy
    retry_policy: _application_pb2.RetryPolicy
    config_overrides: _struct_pb2.Struct
    no_fly_zone_override: bool
    def __init__(self, dry_run: bool = ..., validate_only: bool = ..., auto_start: bool = ..., priority: _Optional[int] = ..., timeout_seconds: _Optional[int] = ..., failure_strategy: _Optional[_Union[_application_pb2.FailureStrategy, str]] = ..., retry_policy: _Optional[_Union[_application_pb2.RetryPolicy, _Mapping]] = ..., config_overrides: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., no_fly_zone_override: bool = ...) -> None: ...

class NodeState(_message.Message):
    __slots__ = ("id", "node_id", "command_id", "target", "parameters", "status", "attempt", "progress", "external_execution_id", "started_at", "completed_at", "error", "output", "dispatched_asset_sn", "dispatch_reason", "warnings")
    ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    DISPATCHED_ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    DISPATCH_REASON_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    id: str
    node_id: str
    command_id: str
    target: _capability_pb2.Target
    parameters: _struct_pb2.Struct
    status: _execution_stats_pb2.NodeStatus
    attempt: int
    progress: float
    external_execution_id: str
    started_at: _timestamp_pb2.Timestamp
    completed_at: _timestamp_pb2.Timestamp
    error: _common_pb2.Error
    output: _struct_pb2.Struct
    dispatched_asset_sn: str
    dispatch_reason: str
    warnings: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., node_id: _Optional[str] = ..., command_id: _Optional[str] = ..., target: _Optional[_Union[_capability_pb2.Target, _Mapping]] = ..., parameters: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., status: _Optional[_Union[_execution_stats_pb2.NodeStatus, str]] = ..., attempt: _Optional[int] = ..., progress: _Optional[float] = ..., external_execution_id: _Optional[str] = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., completed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ..., output: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., dispatched_asset_sn: _Optional[str] = ..., dispatch_reason: _Optional[str] = ..., warnings: _Optional[_Iterable[str]] = ...) -> None: ...

class Execution(_message.Message):
    __slots__ = ("id", "asset", "organization_id", "site_id", "spec", "options", "status", "node_states", "active_node_ids", "progress", "idempotency_key", "requested_by", "created_at", "started_at", "completed_at", "modified_at", "error", "output", "resolved_config", "graph", "application_revision")
    ID_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NODE_STATES_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_NODE_IDS_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_CONFIG_FIELD_NUMBER: _ClassVar[int]
    GRAPH_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_REVISION_FIELD_NUMBER: _ClassVar[int]
    id: str
    asset: _common_pb2.AssetRef
    organization_id: str
    site_id: str
    spec: ExecutionSpec
    options: ExecutionOptions
    status: _execution_stats_pb2.ExecutionStatus
    node_states: _containers.RepeatedCompositeFieldContainer[NodeState]
    active_node_ids: _containers.RepeatedScalarFieldContainer[str]
    progress: float
    idempotency_key: str
    requested_by: str
    created_at: _timestamp_pb2.Timestamp
    started_at: _timestamp_pb2.Timestamp
    completed_at: _timestamp_pb2.Timestamp
    modified_at: _timestamp_pb2.Timestamp
    error: _common_pb2.Error
    output: _struct_pb2.Struct
    resolved_config: _struct_pb2.Struct
    graph: _application_pb2.Graph
    application_revision: str
    def __init__(self, id: _Optional[str] = ..., asset: _Optional[_Union[_common_pb2.AssetRef, _Mapping]] = ..., organization_id: _Optional[str] = ..., site_id: _Optional[str] = ..., spec: _Optional[_Union[ExecutionSpec, _Mapping]] = ..., options: _Optional[_Union[ExecutionOptions, _Mapping]] = ..., status: _Optional[_Union[_execution_stats_pb2.ExecutionStatus, str]] = ..., node_states: _Optional[_Iterable[_Union[NodeState, _Mapping]]] = ..., active_node_ids: _Optional[_Iterable[str]] = ..., progress: _Optional[float] = ..., idempotency_key: _Optional[str] = ..., requested_by: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., completed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ..., output: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., resolved_config: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., graph: _Optional[_Union[_application_pb2.Graph, _Mapping]] = ..., application_revision: _Optional[str] = ...) -> None: ...

class ExecutionEvent(_message.Message):
    __slots__ = ("event_id", "execution_id", "asset_sn", "type", "execution_status", "node_id", "node_status", "progress", "occurred_at", "error", "data")
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_STATUS_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    OCCURRED_AT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    event_id: str
    execution_id: str
    asset_sn: str
    type: ExecutionEventType
    execution_status: _execution_stats_pb2.ExecutionStatus
    node_id: str
    node_status: _execution_stats_pb2.NodeStatus
    progress: float
    occurred_at: _timestamp_pb2.Timestamp
    error: _common_pb2.Error
    data: _struct_pb2.Struct
    def __init__(self, event_id: _Optional[str] = ..., execution_id: _Optional[str] = ..., asset_sn: _Optional[str] = ..., type: _Optional[_Union[ExecutionEventType, str]] = ..., execution_status: _Optional[_Union[_execution_stats_pb2.ExecutionStatus, str]] = ..., node_id: _Optional[str] = ..., node_status: _Optional[_Union[_execution_stats_pb2.NodeStatus, str]] = ..., progress: _Optional[float] = ..., occurred_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ..., data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class CreateExecutionRequest(_message.Message):
    __slots__ = ("context", "spec", "options", "asset", "site_id", "organization_id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    spec: ExecutionSpec
    options: ExecutionOptions
    asset: _common_pb2.AssetRef
    site_id: str
    organization_id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., spec: _Optional[_Union[ExecutionSpec, _Mapping]] = ..., options: _Optional[_Union[ExecutionOptions, _Mapping]] = ..., asset: _Optional[_Union[_common_pb2.AssetRef, _Mapping]] = ..., site_id: _Optional[str] = ..., organization_id: _Optional[str] = ...) -> None: ...

class CreateExecutionResponse(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: Execution
    def __init__(self, execution: _Optional[_Union[Execution, _Mapping]] = ...) -> None: ...

class GetExecutionRequest(_message.Message):
    __slots__ = ("context", "execution_id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    execution_id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., execution_id: _Optional[str] = ...) -> None: ...

class GetExecutionResponse(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: Execution
    def __init__(self, execution: _Optional[_Union[Execution, _Mapping]] = ...) -> None: ...

class ListExecutionsRequest(_message.Message):
    __slots__ = ("context", "asset_sn", "status", "application_id", "skill_id", "site_id", "organization_id", "page")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    asset_sn: str
    status: _execution_stats_pb2.ExecutionStatus
    application_id: str
    skill_id: str
    site_id: str
    organization_id: str
    page: _common_pb2.PageRequest
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., asset_sn: _Optional[str] = ..., status: _Optional[_Union[_execution_stats_pb2.ExecutionStatus, str]] = ..., application_id: _Optional[str] = ..., skill_id: _Optional[str] = ..., site_id: _Optional[str] = ..., organization_id: _Optional[str] = ..., page: _Optional[_Union[_common_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class ListExecutionsResponse(_message.Message):
    __slots__ = ("executions", "page")
    EXECUTIONS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    executions: _containers.RepeatedCompositeFieldContainer[Execution]
    page: _common_pb2.PageResponse
    def __init__(self, executions: _Optional[_Iterable[_Union[Execution, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class StartExecutionRequest(_message.Message):
    __slots__ = ("context", "execution_id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    execution_id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., execution_id: _Optional[str] = ...) -> None: ...

class StartExecutionResponse(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: Execution
    def __init__(self, execution: _Optional[_Union[Execution, _Mapping]] = ...) -> None: ...

class PauseExecutionRequest(_message.Message):
    __slots__ = ("context", "execution_id", "reason")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    execution_id: str
    reason: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., execution_id: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class PauseExecutionResponse(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: Execution
    def __init__(self, execution: _Optional[_Union[Execution, _Mapping]] = ...) -> None: ...

class ResumeExecutionRequest(_message.Message):
    __slots__ = ("context", "execution_id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    execution_id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., execution_id: _Optional[str] = ...) -> None: ...

class ResumeExecutionResponse(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: Execution
    def __init__(self, execution: _Optional[_Union[Execution, _Mapping]] = ...) -> None: ...

class CancelExecutionRequest(_message.Message):
    __slots__ = ("context", "execution_id", "reason")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    execution_id: str
    reason: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., execution_id: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class CancelExecutionResponse(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: Execution
    def __init__(self, execution: _Optional[_Union[Execution, _Mapping]] = ...) -> None: ...

class SignalExecutionRequest(_message.Message):
    __slots__ = ("context", "execution_id", "node_id", "event_type", "data", "approved")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    APPROVED_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    execution_id: str
    node_id: str
    event_type: str
    data: _struct_pb2.Struct
    approved: bool
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., execution_id: _Optional[str] = ..., node_id: _Optional[str] = ..., event_type: _Optional[str] = ..., data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., approved: bool = ...) -> None: ...

class SignalExecutionResponse(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: Execution
    def __init__(self, execution: _Optional[_Union[Execution, _Mapping]] = ...) -> None: ...

class WatchExecutionEventsRequest(_message.Message):
    __slots__ = ("context", "execution_id", "asset_sn", "organization_id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    execution_id: str
    asset_sn: str
    organization_id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., execution_id: _Optional[str] = ..., asset_sn: _Optional[str] = ..., organization_id: _Optional[str] = ...) -> None: ...

class WatchExecutionEventsResponse(_message.Message):
    __slots__ = ("event",)
    EVENT_FIELD_NUMBER: _ClassVar[int]
    event: ExecutionEvent
    def __init__(self, event: _Optional[_Union[ExecutionEvent, _Mapping]] = ...) -> None: ...
