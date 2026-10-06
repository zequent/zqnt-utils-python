import datetime

from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from zqnt_utils.generated.zqnt.common.v3 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NodeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NODE_TYPE_UNSPECIFIED: _ClassVar[NodeType]
    NODE_TYPE_COMMAND: _ClassVar[NodeType]
    NODE_TYPE_SKILL: _ClassVar[NodeType]
    NODE_TYPE_CONDITION: _ClassVar[NodeType]
    NODE_TYPE_PARALLEL_GATEWAY: _ClassVar[NodeType]
    NODE_TYPE_JOIN_GATEWAY: _ClassVar[NodeType]
    NODE_TYPE_WAIT: _ClassVar[NodeType]
    NODE_TYPE_EVENT_WAIT: _ClassVar[NodeType]
    NODE_TYPE_HUMAN_APPROVAL: _ClassVar[NodeType]
    NODE_TYPE_END: _ClassVar[NodeType]

class EdgeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EDGE_TYPE_UNSPECIFIED: _ClassVar[EdgeType]
    EDGE_TYPE_NORMAL: _ClassVar[EdgeType]
    EDGE_TYPE_SUCCESS: _ClassVar[EdgeType]
    EDGE_TYPE_FAILURE: _ClassVar[EdgeType]
    EDGE_TYPE_TIMEOUT: _ClassVar[EdgeType]
    EDGE_TYPE_COMPENSATION: _ClassVar[EdgeType]

class ConditionOperator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONDITION_OPERATOR_UNSPECIFIED: _ClassVar[ConditionOperator]
    CONDITION_OPERATOR_EQUALS: _ClassVar[ConditionOperator]
    CONDITION_OPERATOR_NOT_EQUALS: _ClassVar[ConditionOperator]
    CONDITION_OPERATOR_GREATER_THAN: _ClassVar[ConditionOperator]
    CONDITION_OPERATOR_GREATER_THAN_OR_EQUAL: _ClassVar[ConditionOperator]
    CONDITION_OPERATOR_LESS_THAN: _ClassVar[ConditionOperator]
    CONDITION_OPERATOR_LESS_THAN_OR_EQUAL: _ClassVar[ConditionOperator]
    CONDITION_OPERATOR_IN: _ClassVar[ConditionOperator]
    CONDITION_OPERATOR_CONTAINS: _ClassVar[ConditionOperator]
    CONDITION_OPERATOR_EXISTS: _ClassVar[ConditionOperator]
    CONDITION_OPERATOR_MATCHES: _ClassVar[ConditionOperator]

class ConditionGroupOperator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONDITION_GROUP_OPERATOR_UNSPECIFIED: _ClassVar[ConditionGroupOperator]
    CONDITION_GROUP_OPERATOR_AND: _ClassVar[ConditionGroupOperator]
    CONDITION_GROUP_OPERATOR_OR: _ClassVar[ConditionGroupOperator]

class JoinMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    JOIN_MODE_UNSPECIFIED: _ClassVar[JoinMode]
    JOIN_MODE_ALL: _ClassVar[JoinMode]
    JOIN_MODE_ANY: _ClassVar[JoinMode]

class FailureStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FAILURE_STRATEGY_UNSPECIFIED: _ClassVar[FailureStrategy]
    FAILURE_STRATEGY_STOP: _ClassVar[FailureStrategy]
    FAILURE_STRATEGY_RETRY: _ClassVar[FailureStrategy]
    FAILURE_STRATEGY_CONTINUE: _ClassVar[FailureStrategy]
    FAILURE_STRATEGY_COMPENSATE: _ClassVar[FailureStrategy]

class ScopeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SCOPE_TYPE_UNSPECIFIED: _ClassVar[ScopeType]
    SCOPE_TYPE_GLOBAL: _ClassVar[ScopeType]
    SCOPE_TYPE_ORGANIZATION: _ClassVar[ScopeType]
    SCOPE_TYPE_ASSET: _ClassVar[ScopeType]
    SCOPE_TYPE_SITE: _ClassVar[ScopeType]

class Environment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENVIRONMENT_UNSPECIFIED: _ClassVar[Environment]
    ENVIRONMENT_STAGING: _ClassVar[Environment]
    ENVIRONMENT_PRODUCTION: _ClassVar[Environment]
NODE_TYPE_UNSPECIFIED: NodeType
NODE_TYPE_COMMAND: NodeType
NODE_TYPE_SKILL: NodeType
NODE_TYPE_CONDITION: NodeType
NODE_TYPE_PARALLEL_GATEWAY: NodeType
NODE_TYPE_JOIN_GATEWAY: NodeType
NODE_TYPE_WAIT: NodeType
NODE_TYPE_EVENT_WAIT: NodeType
NODE_TYPE_HUMAN_APPROVAL: NodeType
NODE_TYPE_END: NodeType
EDGE_TYPE_UNSPECIFIED: EdgeType
EDGE_TYPE_NORMAL: EdgeType
EDGE_TYPE_SUCCESS: EdgeType
EDGE_TYPE_FAILURE: EdgeType
EDGE_TYPE_TIMEOUT: EdgeType
EDGE_TYPE_COMPENSATION: EdgeType
CONDITION_OPERATOR_UNSPECIFIED: ConditionOperator
CONDITION_OPERATOR_EQUALS: ConditionOperator
CONDITION_OPERATOR_NOT_EQUALS: ConditionOperator
CONDITION_OPERATOR_GREATER_THAN: ConditionOperator
CONDITION_OPERATOR_GREATER_THAN_OR_EQUAL: ConditionOperator
CONDITION_OPERATOR_LESS_THAN: ConditionOperator
CONDITION_OPERATOR_LESS_THAN_OR_EQUAL: ConditionOperator
CONDITION_OPERATOR_IN: ConditionOperator
CONDITION_OPERATOR_CONTAINS: ConditionOperator
CONDITION_OPERATOR_EXISTS: ConditionOperator
CONDITION_OPERATOR_MATCHES: ConditionOperator
CONDITION_GROUP_OPERATOR_UNSPECIFIED: ConditionGroupOperator
CONDITION_GROUP_OPERATOR_AND: ConditionGroupOperator
CONDITION_GROUP_OPERATOR_OR: ConditionGroupOperator
JOIN_MODE_UNSPECIFIED: JoinMode
JOIN_MODE_ALL: JoinMode
JOIN_MODE_ANY: JoinMode
FAILURE_STRATEGY_UNSPECIFIED: FailureStrategy
FAILURE_STRATEGY_STOP: FailureStrategy
FAILURE_STRATEGY_RETRY: FailureStrategy
FAILURE_STRATEGY_CONTINUE: FailureStrategy
FAILURE_STRATEGY_COMPENSATE: FailureStrategy
SCOPE_TYPE_UNSPECIFIED: ScopeType
SCOPE_TYPE_GLOBAL: ScopeType
SCOPE_TYPE_ORGANIZATION: ScopeType
SCOPE_TYPE_ASSET: ScopeType
SCOPE_TYPE_SITE: ScopeType
ENVIRONMENT_UNSPECIFIED: Environment
ENVIRONMENT_STAGING: Environment
ENVIRONMENT_PRODUCTION: Environment

class Comparison(_message.Message):
    __slots__ = ("field_path", "operator", "expected_value")
    FIELD_PATH_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_VALUE_FIELD_NUMBER: _ClassVar[int]
    field_path: str
    operator: ConditionOperator
    expected_value: _struct_pb2.Value
    def __init__(self, field_path: _Optional[str] = ..., operator: _Optional[_Union[ConditionOperator, str]] = ..., expected_value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...

class ConditionGroup(_message.Message):
    __slots__ = ("operator", "conditions", "negate")
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    NEGATE_FIELD_NUMBER: _ClassVar[int]
    operator: ConditionGroupOperator
    conditions: _containers.RepeatedCompositeFieldContainer[Condition]
    negate: bool
    def __init__(self, operator: _Optional[_Union[ConditionGroupOperator, str]] = ..., conditions: _Optional[_Iterable[_Union[Condition, _Mapping]]] = ..., negate: bool = ...) -> None: ...

class Condition(_message.Message):
    __slots__ = ("comparison", "group", "constant", "result_when_missing")
    COMPARISON_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    CONSTANT_FIELD_NUMBER: _ClassVar[int]
    RESULT_WHEN_MISSING_FIELD_NUMBER: _ClassVar[int]
    comparison: Comparison
    group: ConditionGroup
    constant: bool
    result_when_missing: bool
    def __init__(self, comparison: _Optional[_Union[Comparison, _Mapping]] = ..., group: _Optional[_Union[ConditionGroup, _Mapping]] = ..., constant: bool = ..., result_when_missing: bool = ...) -> None: ...

class CommandNodeConfig(_message.Message):
    __slots__ = ("command_id", "required_parameters", "parameter_defaults", "parameter_mapping", "command_schema_version")
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_DEFAULTS_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_MAPPING_FIELD_NUMBER: _ClassVar[int]
    COMMAND_SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    command_id: str
    required_parameters: _containers.RepeatedScalarFieldContainer[str]
    parameter_defaults: _struct_pb2.Struct
    parameter_mapping: _struct_pb2.Struct
    command_schema_version: str
    def __init__(self, command_id: _Optional[str] = ..., required_parameters: _Optional[_Iterable[str]] = ..., parameter_defaults: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., parameter_mapping: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., command_schema_version: _Optional[str] = ...) -> None: ...

class SkillNodeConfig(_message.Message):
    __slots__ = ("skill_id", "parameter_mapping", "skill_version", "follow_latest")
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_MAPPING_FIELD_NUMBER: _ClassVar[int]
    SKILL_VERSION_FIELD_NUMBER: _ClassVar[int]
    FOLLOW_LATEST_FIELD_NUMBER: _ClassVar[int]
    skill_id: str
    parameter_mapping: _struct_pb2.Struct
    skill_version: str
    follow_latest: bool
    def __init__(self, skill_id: _Optional[str] = ..., parameter_mapping: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., skill_version: _Optional[str] = ..., follow_latest: bool = ...) -> None: ...

class GatewayNodeConfig(_message.Message):
    __slots__ = ("join_mode", "output_mapping")
    JOIN_MODE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_MAPPING_FIELD_NUMBER: _ClassVar[int]
    join_mode: JoinMode
    output_mapping: _struct_pb2.Struct
    def __init__(self, join_mode: _Optional[_Union[JoinMode, str]] = ..., output_mapping: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class WaitNodeConfig(_message.Message):
    __slots__ = ("duration_seconds", "until")
    DURATION_SECONDS_FIELD_NUMBER: _ClassVar[int]
    UNTIL_FIELD_NUMBER: _ClassVar[int]
    duration_seconds: int
    until: _timestamp_pb2.Timestamp
    def __init__(self, duration_seconds: _Optional[int] = ..., until: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class EventWaitNodeConfig(_message.Message):
    __slots__ = ("event_type", "filter", "timeout_seconds")
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    event_type: str
    filter: Condition
    timeout_seconds: int
    def __init__(self, event_type: _Optional[str] = ..., filter: _Optional[_Union[Condition, _Mapping]] = ..., timeout_seconds: _Optional[int] = ...) -> None: ...

class HumanApprovalNodeConfig(_message.Message):
    __slots__ = ("approval_type", "approval_group", "timeout_seconds")
    APPROVAL_TYPE_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_GROUP_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    approval_type: str
    approval_group: str
    timeout_seconds: int
    def __init__(self, approval_type: _Optional[str] = ..., approval_group: _Optional[str] = ..., timeout_seconds: _Optional[int] = ...) -> None: ...

class RetryPolicy(_message.Message):
    __slots__ = ("max_attempts", "retry_delay_seconds", "backoff_multiplier")
    MAX_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    RETRY_DELAY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    BACKOFF_MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    max_attempts: int
    retry_delay_seconds: int
    backoff_multiplier: float
    def __init__(self, max_attempts: _Optional[int] = ..., retry_delay_seconds: _Optional[int] = ..., backoff_multiplier: _Optional[float] = ...) -> None: ...

class Node(_message.Message):
    __slots__ = ("id", "name", "type", "command", "skill", "condition", "gateway", "wait", "event_wait", "human_approval", "timeout_seconds", "failure_strategy", "retry_policy", "enabled")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    SKILL_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    WAIT_FIELD_NUMBER: _ClassVar[int]
    EVENT_WAIT_FIELD_NUMBER: _ClassVar[int]
    HUMAN_APPROVAL_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    RETRY_POLICY_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    type: NodeType
    command: CommandNodeConfig
    skill: SkillNodeConfig
    condition: Condition
    gateway: GatewayNodeConfig
    wait: WaitNodeConfig
    event_wait: EventWaitNodeConfig
    human_approval: HumanApprovalNodeConfig
    timeout_seconds: int
    failure_strategy: FailureStrategy
    retry_policy: RetryPolicy
    enabled: bool
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[_Union[NodeType, str]] = ..., command: _Optional[_Union[CommandNodeConfig, _Mapping]] = ..., skill: _Optional[_Union[SkillNodeConfig, _Mapping]] = ..., condition: _Optional[_Union[Condition, _Mapping]] = ..., gateway: _Optional[_Union[GatewayNodeConfig, _Mapping]] = ..., wait: _Optional[_Union[WaitNodeConfig, _Mapping]] = ..., event_wait: _Optional[_Union[EventWaitNodeConfig, _Mapping]] = ..., human_approval: _Optional[_Union[HumanApprovalNodeConfig, _Mapping]] = ..., timeout_seconds: _Optional[int] = ..., failure_strategy: _Optional[_Union[FailureStrategy, str]] = ..., retry_policy: _Optional[_Union[RetryPolicy, _Mapping]] = ..., enabled: bool = ...) -> None: ...

class Edge(_message.Message):
    __slots__ = ("id", "source_node_id", "target_node_id", "type", "condition", "priority", "label")
    ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    id: str
    source_node_id: str
    target_node_id: str
    type: EdgeType
    condition: Condition
    priority: int
    label: str
    def __init__(self, id: _Optional[str] = ..., source_node_id: _Optional[str] = ..., target_node_id: _Optional[str] = ..., type: _Optional[_Union[EdgeType, str]] = ..., condition: _Optional[_Union[Condition, _Mapping]] = ..., priority: _Optional[int] = ..., label: _Optional[str] = ...) -> None: ...

class NodeLayout(_message.Message):
    __slots__ = ("node_id", "x", "y", "color", "collapsed", "editor_metadata")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    COLLAPSED_FIELD_NUMBER: _ClassVar[int]
    EDITOR_METADATA_FIELD_NUMBER: _ClassVar[int]
    node_id: str
    x: float
    y: float
    color: str
    collapsed: bool
    editor_metadata: _struct_pb2.Struct
    def __init__(self, node_id: _Optional[str] = ..., x: _Optional[float] = ..., y: _Optional[float] = ..., color: _Optional[str] = ..., collapsed: bool = ..., editor_metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class GraphLayout(_message.Message):
    __slots__ = ("nodes", "zoom", "viewport_x", "viewport_y")
    NODES_FIELD_NUMBER: _ClassVar[int]
    ZOOM_FIELD_NUMBER: _ClassVar[int]
    VIEWPORT_X_FIELD_NUMBER: _ClassVar[int]
    VIEWPORT_Y_FIELD_NUMBER: _ClassVar[int]
    nodes: _containers.RepeatedCompositeFieldContainer[NodeLayout]
    zoom: float
    viewport_x: float
    viewport_y: float
    def __init__(self, nodes: _Optional[_Iterable[_Union[NodeLayout, _Mapping]]] = ..., zoom: _Optional[float] = ..., viewport_x: _Optional[float] = ..., viewport_y: _Optional[float] = ...) -> None: ...

class Graph(_message.Message):
    __slots__ = ("start_node_id", "nodes", "edges", "layout")
    START_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    EDGES_FIELD_NUMBER: _ClassVar[int]
    LAYOUT_FIELD_NUMBER: _ClassVar[int]
    start_node_id: str
    nodes: _containers.RepeatedCompositeFieldContainer[Node]
    edges: _containers.RepeatedCompositeFieldContainer[Edge]
    layout: GraphLayout
    def __init__(self, start_node_id: _Optional[str] = ..., nodes: _Optional[_Iterable[_Union[Node, _Mapping]]] = ..., edges: _Optional[_Iterable[_Union[Edge, _Mapping]]] = ..., layout: _Optional[_Union[GraphLayout, _Mapping]] = ...) -> None: ...

class Scope(_message.Message):
    __slots__ = ("type", "target_id")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    type: ScopeType
    target_id: str
    def __init__(self, type: _Optional[_Union[ScopeType, str]] = ..., target_id: _Optional[str] = ...) -> None: ...

class Skill(_message.Message):
    __slots__ = ("id", "name", "description", "graph", "input_schema", "output_schema", "default_config", "enabled", "required_asset_capabilities", "output_mapping", "source_application_id", "source_version")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    GRAPH_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_ASSET_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_MAPPING_FIELD_NUMBER: _ClassVar[int]
    SOURCE_APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_VERSION_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    graph: Graph
    input_schema: _struct_pb2.Struct
    output_schema: _struct_pb2.Struct
    default_config: _struct_pb2.Struct
    enabled: bool
    required_asset_capabilities: _containers.RepeatedScalarFieldContainer[str]
    output_mapping: _struct_pb2.Struct
    source_application_id: str
    source_version: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., graph: _Optional[_Union[Graph, _Mapping]] = ..., input_schema: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., output_schema: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., default_config: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., enabled: bool = ..., required_asset_capabilities: _Optional[_Iterable[str]] = ..., output_mapping: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., source_application_id: _Optional[str] = ..., source_version: _Optional[str] = ...) -> None: ...

class Change(_message.Message):
    __slots__ = ("at", "author", "note", "automatic")
    AT_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    AUTOMATIC_FIELD_NUMBER: _ClassVar[int]
    at: _timestamp_pb2.Timestamp
    author: str
    note: str
    automatic: bool
    def __init__(self, at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., author: _Optional[str] = ..., note: _Optional[str] = ..., automatic: bool = ...) -> None: ...

class Application(_message.Message):
    __slots__ = ("id", "version", "name", "description", "skills", "scopes", "default_config", "enabled", "revision", "created_at", "modified_at", "organization_id", "changelog", "change_note")
    ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    CHANGELOG_FIELD_NUMBER: _ClassVar[int]
    CHANGE_NOTE_FIELD_NUMBER: _ClassVar[int]
    id: str
    version: str
    name: str
    description: str
    skills: _containers.RepeatedCompositeFieldContainer[Skill]
    scopes: _containers.RepeatedCompositeFieldContainer[Scope]
    default_config: _struct_pb2.Struct
    enabled: bool
    revision: str
    created_at: _timestamp_pb2.Timestamp
    modified_at: _timestamp_pb2.Timestamp
    organization_id: str
    changelog: _containers.RepeatedCompositeFieldContainer[Change]
    change_note: str
    def __init__(self, id: _Optional[str] = ..., version: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., skills: _Optional[_Iterable[_Union[Skill, _Mapping]]] = ..., scopes: _Optional[_Iterable[_Union[Scope, _Mapping]]] = ..., default_config: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., enabled: bool = ..., revision: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., organization_id: _Optional[str] = ..., changelog: _Optional[_Iterable[_Union[Change, _Mapping]]] = ..., change_note: _Optional[str] = ...) -> None: ...

class Pause(_message.Message):
    __slots__ = ("application_id", "skill_id", "paused_by", "paused_at", "reason", "organization_id")
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    PAUSED_BY_FIELD_NUMBER: _ClassVar[int]
    PAUSED_AT_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    application_id: str
    skill_id: str
    paused_by: str
    paused_at: _timestamp_pb2.Timestamp
    reason: str
    organization_id: str
    def __init__(self, application_id: _Optional[str] = ..., skill_id: _Optional[str] = ..., paused_by: _Optional[str] = ..., paused_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., reason: _Optional[str] = ..., organization_id: _Optional[str] = ...) -> None: ...

class EnvironmentPointer(_message.Message):
    __slots__ = ("application_id", "environment", "version", "updated_at", "updated_by")
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_BY_FIELD_NUMBER: _ClassVar[int]
    application_id: str
    environment: Environment
    version: str
    updated_at: _timestamp_pb2.Timestamp
    updated_by: str
    def __init__(self, application_id: _Optional[str] = ..., environment: _Optional[_Union[Environment, str]] = ..., version: _Optional[str] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_by: _Optional[str] = ...) -> None: ...

class ListApplicationsRequest(_message.Message):
    __slots__ = ("context", "scope", "enabled_only", "page")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    ENABLED_ONLY_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    scope: Scope
    enabled_only: bool
    page: _common_pb2.PageRequest
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., scope: _Optional[_Union[Scope, _Mapping]] = ..., enabled_only: bool = ..., page: _Optional[_Union[_common_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class ListApplicationsResponse(_message.Message):
    __slots__ = ("applications", "page")
    APPLICATIONS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    applications: _containers.RepeatedCompositeFieldContainer[Application]
    page: _common_pb2.PageResponse
    def __init__(self, applications: _Optional[_Iterable[_Union[Application, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class GetApplicationRequest(_message.Message):
    __slots__ = ("context", "application_id", "version")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    application_id: str
    version: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., application_id: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...

class GetApplicationResponse(_message.Message):
    __slots__ = ("application",)
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    application: Application
    def __init__(self, application: _Optional[_Union[Application, _Mapping]] = ...) -> None: ...

class SaveApplicationRequest(_message.Message):
    __slots__ = ("context", "application", "expected_revision")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_REVISION_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    application: Application
    expected_revision: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., application: _Optional[_Union[Application, _Mapping]] = ..., expected_revision: _Optional[str] = ...) -> None: ...

class SaveApplicationResponse(_message.Message):
    __slots__ = ("application", "warnings")
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    application: Application
    warnings: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, application: _Optional[_Union[Application, _Mapping]] = ..., warnings: _Optional[_Iterable[str]] = ...) -> None: ...

class DeleteApplicationRequest(_message.Message):
    __slots__ = ("context", "application_id", "version", "expected_revision")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_REVISION_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    application_id: str
    version: str
    expected_revision: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., application_id: _Optional[str] = ..., version: _Optional[str] = ..., expected_revision: _Optional[str] = ...) -> None: ...

class DeleteApplicationResponse(_message.Message):
    __slots__ = ("deleted",)
    DELETED_FIELD_NUMBER: _ClassVar[int]
    deleted: bool
    def __init__(self, deleted: bool = ...) -> None: ...

class ListEnvironmentsRequest(_message.Message):
    __slots__ = ("context", "application_id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    application_id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., application_id: _Optional[str] = ...) -> None: ...

class ListEnvironmentsResponse(_message.Message):
    __slots__ = ("pointers",)
    POINTERS_FIELD_NUMBER: _ClassVar[int]
    pointers: _containers.RepeatedCompositeFieldContainer[EnvironmentPointer]
    def __init__(self, pointers: _Optional[_Iterable[_Union[EnvironmentPointer, _Mapping]]] = ...) -> None: ...

class PromoteVersionRequest(_message.Message):
    __slots__ = ("context", "application_id", "version", "environment")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    application_id: str
    version: str
    environment: Environment
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., application_id: _Optional[str] = ..., version: _Optional[str] = ..., environment: _Optional[_Union[Environment, str]] = ...) -> None: ...

class PromoteVersionResponse(_message.Message):
    __slots__ = ("pointers",)
    POINTERS_FIELD_NUMBER: _ClassVar[int]
    pointers: _containers.RepeatedCompositeFieldContainer[EnvironmentPointer]
    def __init__(self, pointers: _Optional[_Iterable[_Union[EnvironmentPointer, _Mapping]]] = ...) -> None: ...

class SetPauseRequest(_message.Message):
    __slots__ = ("context", "application_id", "skill_id", "paused", "reason")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    PAUSED_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    application_id: str
    skill_id: str
    paused: bool
    reason: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., application_id: _Optional[str] = ..., skill_id: _Optional[str] = ..., paused: bool = ..., reason: _Optional[str] = ...) -> None: ...

class SetPauseResponse(_message.Message):
    __slots__ = ("pauses",)
    PAUSES_FIELD_NUMBER: _ClassVar[int]
    pauses: _containers.RepeatedCompositeFieldContainer[Pause]
    def __init__(self, pauses: _Optional[_Iterable[_Union[Pause, _Mapping]]] = ...) -> None: ...

class ListPausesRequest(_message.Message):
    __slots__ = ("context", "application_id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    application_id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., application_id: _Optional[str] = ...) -> None: ...

class ListPausesResponse(_message.Message):
    __slots__ = ("pauses",)
    PAUSES_FIELD_NUMBER: _ClassVar[int]
    pauses: _containers.RepeatedCompositeFieldContainer[Pause]
    def __init__(self, pauses: _Optional[_Iterable[_Union[Pause, _Mapping]]] = ...) -> None: ...
