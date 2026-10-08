import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from zqnt_utils.generated.zqnt.agent.v3 import agent_pb2 as _agent_pb2
from zqnt_utils.generated.zqnt.application.v3 import application_pb2 as _application_pb2
from zqnt_utils.generated.zqnt.capability.v3 import capability_pb2 as _capability_pb2
from zqnt_utils.generated.zqnt.common.v3 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SessionKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SESSION_KIND_UNSPECIFIED: _ClassVar[SessionKind]
    SESSION_KIND_CHAT: _ClassVar[SessionKind]
    SESSION_KIND_RUN: _ClassVar[SessionKind]

class EntityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENTITY_TYPE_UNSPECIFIED: _ClassVar[EntityType]
    ENTITY_TYPE_ASSET: _ClassVar[EntityType]
    ENTITY_TYPE_SITE: _ClassVar[EntityType]
    ENTITY_TYPE_APPLICATION: _ClassVar[EntityType]
    ENTITY_TYPE_SKILL: _ClassVar[EntityType]
    ENTITY_TYPE_EXECUTION: _ClassVar[EntityType]
    ENTITY_TYPE_TRIGGER: _ClassVar[EntityType]
    ENTITY_TYPE_SCHEDULE: _ClassVar[EntityType]
    ENTITY_TYPE_NO_FLY_ZONE: _ClassVar[EntityType]
    ENTITY_TYPE_DETECTION: _ClassVar[EntityType]
SESSION_KIND_UNSPECIFIED: SessionKind
SESSION_KIND_CHAT: SessionKind
SESSION_KIND_RUN: SessionKind
ENTITY_TYPE_UNSPECIFIED: EntityType
ENTITY_TYPE_ASSET: EntityType
ENTITY_TYPE_SITE: EntityType
ENTITY_TYPE_APPLICATION: EntityType
ENTITY_TYPE_SKILL: EntityType
ENTITY_TYPE_EXECUTION: EntityType
ENTITY_TYPE_TRIGGER: EntityType
ENTITY_TYPE_SCHEDULE: EntityType
ENTITY_TYPE_NO_FLY_ZONE: EntityType
ENTITY_TYPE_DETECTION: EntityType

class SessionGrant(_message.Message):
    __slots__ = ("session_id", "kind", "organization_id", "actor_kind", "actor_id", "actor_display_name", "role_id", "role_name", "conversation_id", "context", "allowed_categories", "approval_required_categories", "allowed_models", "default_model_id", "data_sharing", "remaining_micro_eur", "expires_at")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    ACTOR_KIND_FIELD_NUMBER: _ClassVar[int]
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    ACTOR_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_REQUIRED_CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_MODELS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_SHARING_FIELD_NUMBER: _ClassVar[int]
    REMAINING_MICRO_EUR_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    kind: SessionKind
    organization_id: str
    actor_kind: _agent_pb2.ActorKind
    actor_id: str
    actor_display_name: str
    role_id: str
    role_name: str
    conversation_id: str
    context: _agent_pb2.ConversationContext
    allowed_categories: _containers.RepeatedScalarFieldContainer[_agent_pb2.ToolCategory]
    approval_required_categories: _containers.RepeatedScalarFieldContainer[_agent_pb2.ToolCategory]
    allowed_models: _containers.RepeatedCompositeFieldContainer[_agent_pb2.Model]
    default_model_id: str
    data_sharing: _agent_pb2.DataSharing
    remaining_micro_eur: int
    expires_at: _timestamp_pb2.Timestamp
    def __init__(self, session_id: _Optional[str] = ..., kind: _Optional[_Union[SessionKind, str]] = ..., organization_id: _Optional[str] = ..., actor_kind: _Optional[_Union[_agent_pb2.ActorKind, str]] = ..., actor_id: _Optional[str] = ..., actor_display_name: _Optional[str] = ..., role_id: _Optional[str] = ..., role_name: _Optional[str] = ..., conversation_id: _Optional[str] = ..., context: _Optional[_Union[_agent_pb2.ConversationContext, _Mapping]] = ..., allowed_categories: _Optional[_Iterable[_Union[_agent_pb2.ToolCategory, str]]] = ..., approval_required_categories: _Optional[_Iterable[_Union[_agent_pb2.ToolCategory, str]]] = ..., allowed_models: _Optional[_Iterable[_Union[_agent_pb2.Model, _Mapping]]] = ..., default_model_id: _Optional[str] = ..., data_sharing: _Optional[_Union[_agent_pb2.DataSharing, _Mapping]] = ..., remaining_micro_eur: _Optional[int] = ..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class EntityRef(_message.Message):
    __slots__ = ("type", "id")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    type: EntityType
    id: str
    def __init__(self, type: _Optional[_Union[EntityType, str]] = ..., id: _Optional[str] = ...) -> None: ...

class EntitySummary(_message.Message):
    __slots__ = ("ref", "name", "summary", "facts")
    REF_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    FACTS_FIELD_NUMBER: _ClassVar[int]
    ref: EntityRef
    name: str
    summary: str
    facts: _struct_pb2.Struct
    def __init__(self, ref: _Optional[_Union[EntityRef, _Mapping]] = ..., name: _Optional[str] = ..., summary: _Optional[str] = ..., facts: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class ToolCallContext(_message.Message):
    __slots__ = ("session_id", "tool_call_id", "tool", "approval_id")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    TOOL_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    tool_call_id: str
    tool: str
    approval_id: str
    def __init__(self, session_id: _Optional[str] = ..., tool_call_id: _Optional[str] = ..., tool: _Optional[str] = ..., approval_id: _Optional[str] = ...) -> None: ...

class GetSessionGrantRequest(_message.Message):
    __slots__ = ("session_id",)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    def __init__(self, session_id: _Optional[str] = ...) -> None: ...

class GetSessionGrantResponse(_message.Message):
    __slots__ = ("grant",)
    GRANT_FIELD_NUMBER: _ClassVar[int]
    grant: SessionGrant
    def __init__(self, grant: _Optional[_Union[SessionGrant, _Mapping]] = ...) -> None: ...

class GetModelAccessRequest(_message.Message):
    __slots__ = ("session_id", "model_id")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    model_id: str
    def __init__(self, session_id: _Optional[str] = ..., model_id: _Optional[str] = ...) -> None: ...

class GetModelAccessResponse(_message.Message):
    __slots__ = ("model", "api_key")
    MODEL_FIELD_NUMBER: _ClassVar[int]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    model: _agent_pb2.Model
    api_key: str
    def __init__(self, model: _Optional[_Union[_agent_pb2.Model, _Mapping]] = ..., api_key: _Optional[str] = ...) -> None: ...

class ReserveBudgetRequest(_message.Message):
    __slots__ = ("session_id", "model_id", "estimated_input_tokens", "max_output_tokens")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    MAX_OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    model_id: str
    estimated_input_tokens: int
    max_output_tokens: int
    def __init__(self, session_id: _Optional[str] = ..., model_id: _Optional[str] = ..., estimated_input_tokens: _Optional[int] = ..., max_output_tokens: _Optional[int] = ...) -> None: ...

class ReserveBudgetResponse(_message.Message):
    __slots__ = ("reservation_id", "reserved_micro_eur", "expires_at")
    RESERVATION_ID_FIELD_NUMBER: _ClassVar[int]
    RESERVED_MICRO_EUR_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    reservation_id: str
    reserved_micro_eur: int
    expires_at: _timestamp_pb2.Timestamp
    def __init__(self, reservation_id: _Optional[str] = ..., reserved_micro_eur: _Optional[int] = ..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SettleUsageRequest(_message.Message):
    __slots__ = ("reservation_id", "input_tokens", "output_tokens")
    RESERVATION_ID_FIELD_NUMBER: _ClassVar[int]
    INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    reservation_id: str
    input_tokens: int
    output_tokens: int
    def __init__(self, reservation_id: _Optional[str] = ..., input_tokens: _Optional[int] = ..., output_tokens: _Optional[int] = ...) -> None: ...

class SettleUsageResponse(_message.Message):
    __slots__ = ("cost_micro_eur", "remaining_micro_eur")
    COST_MICRO_EUR_FIELD_NUMBER: _ClassVar[int]
    REMAINING_MICRO_EUR_FIELD_NUMBER: _ClassVar[int]
    cost_micro_eur: int
    remaining_micro_eur: int
    def __init__(self, cost_micro_eur: _Optional[int] = ..., remaining_micro_eur: _Optional[int] = ...) -> None: ...

class ListConversationTurnsRequest(_message.Message):
    __slots__ = ("session_id", "after_sequence", "page")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    AFTER_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    after_sequence: int
    page: _common_pb2.PageRequest
    def __init__(self, session_id: _Optional[str] = ..., after_sequence: _Optional[int] = ..., page: _Optional[_Union[_common_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class ListConversationTurnsResponse(_message.Message):
    __slots__ = ("turns", "last_sequence", "page")
    TURNS_FIELD_NUMBER: _ClassVar[int]
    LAST_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    turns: _containers.RepeatedCompositeFieldContainer[_agent_pb2.Turn]
    last_sequence: int
    page: _common_pb2.PageResponse
    def __init__(self, turns: _Optional[_Iterable[_Union[_agent_pb2.Turn, _Mapping]]] = ..., last_sequence: _Optional[int] = ..., page: _Optional[_Union[_common_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class AppendConversationTurnsRequest(_message.Message):
    __slots__ = ("session_id", "expected_last_sequence", "turns")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_LAST_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    TURNS_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    expected_last_sequence: int
    turns: _containers.RepeatedCompositeFieldContainer[_agent_pb2.Turn]
    def __init__(self, session_id: _Optional[str] = ..., expected_last_sequence: _Optional[int] = ..., turns: _Optional[_Iterable[_Union[_agent_pb2.Turn, _Mapping]]] = ...) -> None: ...

class AppendConversationTurnsResponse(_message.Message):
    __slots__ = ("last_sequence",)
    LAST_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    last_sequence: int
    def __init__(self, last_sequence: _Optional[int] = ...) -> None: ...

class RecallRequest(_message.Message):
    __slots__ = ("call", "query", "limit")
    CALL_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    call: ToolCallContext
    query: str
    limit: int
    def __init__(self, call: _Optional[_Union[ToolCallContext, _Mapping]] = ..., query: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class RecallResponse(_message.Message):
    __slots__ = ("facts",)
    FACTS_FIELD_NUMBER: _ClassVar[int]
    facts: _containers.RepeatedCompositeFieldContainer[_agent_pb2.MemoryFact]
    def __init__(self, facts: _Optional[_Iterable[_Union[_agent_pb2.MemoryFact, _Mapping]]] = ...) -> None: ...

class RememberRequest(_message.Message):
    __slots__ = ("call", "text", "site_id")
    CALL_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    call: ToolCallContext
    text: str
    site_id: str
    def __init__(self, call: _Optional[_Union[ToolCallContext, _Mapping]] = ..., text: _Optional[str] = ..., site_id: _Optional[str] = ...) -> None: ...

class RememberResponse(_message.Message):
    __slots__ = ("fact",)
    FACT_FIELD_NUMBER: _ClassVar[int]
    fact: _agent_pb2.MemoryFact
    def __init__(self, fact: _Optional[_Union[_agent_pb2.MemoryFact, _Mapping]] = ...) -> None: ...

class ListEntitiesRequest(_message.Message):
    __slots__ = ("call", "type", "query", "site_id", "limit")
    CALL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    call: ToolCallContext
    type: EntityType
    query: str
    site_id: str
    limit: int
    def __init__(self, call: _Optional[_Union[ToolCallContext, _Mapping]] = ..., type: _Optional[_Union[EntityType, str]] = ..., query: _Optional[str] = ..., site_id: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class ListEntitiesResponse(_message.Message):
    __slots__ = ("entities", "truncated")
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    entities: _containers.RepeatedCompositeFieldContainer[EntitySummary]
    truncated: bool
    def __init__(self, entities: _Optional[_Iterable[_Union[EntitySummary, _Mapping]]] = ..., truncated: bool = ...) -> None: ...

class GetEntitySummaryRequest(_message.Message):
    __slots__ = ("call", "ref")
    CALL_FIELD_NUMBER: _ClassVar[int]
    REF_FIELD_NUMBER: _ClassVar[int]
    call: ToolCallContext
    ref: EntityRef
    def __init__(self, call: _Optional[_Union[ToolCallContext, _Mapping]] = ..., ref: _Optional[_Union[EntityRef, _Mapping]] = ...) -> None: ...

class GetEntitySummaryResponse(_message.Message):
    __slots__ = ("entity",)
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    entity: EntitySummary
    def __init__(self, entity: _Optional[_Union[EntitySummary, _Mapping]] = ...) -> None: ...

class GetAssetLiveStateRequest(_message.Message):
    __slots__ = ("call", "asset_sn")
    CALL_FIELD_NUMBER: _ClassVar[int]
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    call: ToolCallContext
    asset_sn: str
    def __init__(self, call: _Optional[_Union[ToolCallContext, _Mapping]] = ..., asset_sn: _Optional[str] = ...) -> None: ...

class GetAssetLiveStateResponse(_message.Message):
    __slots__ = ("asset", "online", "telemetry_age")
    ASSET_FIELD_NUMBER: _ClassVar[int]
    ONLINE_FIELD_NUMBER: _ClassVar[int]
    TELEMETRY_AGE_FIELD_NUMBER: _ClassVar[int]
    asset: EntitySummary
    online: bool
    telemetry_age: _duration_pb2.Duration
    def __init__(self, asset: _Optional[_Union[EntitySummary, _Mapping]] = ..., online: bool = ..., telemetry_age: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class GetAssetSnapshotRequest(_message.Message):
    __slots__ = ("call", "asset_sn", "camera_id")
    CALL_FIELD_NUMBER: _ClassVar[int]
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    CAMERA_ID_FIELD_NUMBER: _ClassVar[int]
    call: ToolCallContext
    asset_sn: str
    camera_id: str
    def __init__(self, call: _Optional[_Union[ToolCallContext, _Mapping]] = ..., asset_sn: _Optional[str] = ..., camera_id: _Optional[str] = ...) -> None: ...

class GetAssetSnapshotResponse(_message.Message):
    __slots__ = ("image_url", "captured_at")
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    CAPTURED_AT_FIELD_NUMBER: _ClassVar[int]
    image_url: str
    captured_at: _timestamp_pb2.Timestamp
    def __init__(self, image_url: _Optional[str] = ..., captured_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AgentCapability(_message.Message):
    __slots__ = ("capability", "category", "asset_sns")
    CAPABILITY_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    ASSET_SNS_FIELD_NUMBER: _ClassVar[int]
    capability: _capability_pb2.Capability
    category: _agent_pb2.ToolCategory
    asset_sns: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, capability: _Optional[_Union[_capability_pb2.Capability, _Mapping]] = ..., category: _Optional[_Union[_agent_pb2.ToolCategory, str]] = ..., asset_sns: _Optional[_Iterable[str]] = ...) -> None: ...

class ListAgentCapabilitiesRequest(_message.Message):
    __slots__ = ("call", "asset_sn")
    CALL_FIELD_NUMBER: _ClassVar[int]
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    call: ToolCallContext
    asset_sn: str
    def __init__(self, call: _Optional[_Union[ToolCallContext, _Mapping]] = ..., asset_sn: _Optional[str] = ...) -> None: ...

class ListAgentCapabilitiesResponse(_message.Message):
    __slots__ = ("capabilities",)
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    capabilities: _containers.RepeatedCompositeFieldContainer[AgentCapability]
    def __init__(self, capabilities: _Optional[_Iterable[_Union[AgentCapability, _Mapping]]] = ...) -> None: ...

class GetApplicationDefinitionRequest(_message.Message):
    __slots__ = ("call", "application_id", "version")
    CALL_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    call: ToolCallContext
    application_id: str
    version: int
    def __init__(self, call: _Optional[_Union[ToolCallContext, _Mapping]] = ..., application_id: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

class GetApplicationDefinitionResponse(_message.Message):
    __slots__ = ("application",)
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    application: _application_pb2.Application
    def __init__(self, application: _Optional[_Union[_application_pb2.Application, _Mapping]] = ...) -> None: ...

class ValidateApplicationDraftRequest(_message.Message):
    __slots__ = ("call", "application")
    CALL_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    call: ToolCallContext
    application: _application_pb2.Application
    def __init__(self, call: _Optional[_Union[ToolCallContext, _Mapping]] = ..., application: _Optional[_Union[_application_pb2.Application, _Mapping]] = ...) -> None: ...

class ValidateApplicationDraftResponse(_message.Message):
    __slots__ = ("valid", "issues")
    VALID_FIELD_NUMBER: _ClassVar[int]
    ISSUES_FIELD_NUMBER: _ClassVar[int]
    valid: bool
    issues: _containers.RepeatedCompositeFieldContainer[_application_pb2.ValidationIssue]
    def __init__(self, valid: bool = ..., issues: _Optional[_Iterable[_Union[_application_pb2.ValidationIssue, _Mapping]]] = ...) -> None: ...

class SaveApplicationDraftRequest(_message.Message):
    __slots__ = ("call", "application", "expected_revision")
    CALL_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_REVISION_FIELD_NUMBER: _ClassVar[int]
    call: ToolCallContext
    application: _application_pb2.Application
    expected_revision: str
    def __init__(self, call: _Optional[_Union[ToolCallContext, _Mapping]] = ..., application: _Optional[_Union[_application_pb2.Application, _Mapping]] = ..., expected_revision: _Optional[str] = ...) -> None: ...

class SaveApplicationDraftResponse(_message.Message):
    __slots__ = ("application", "warnings")
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    application: _application_pb2.Application
    warnings: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, application: _Optional[_Union[_application_pb2.Application, _Mapping]] = ..., warnings: _Optional[_Iterable[str]] = ...) -> None: ...

class SetAutomationEnabledRequest(_message.Message):
    __slots__ = ("call", "ref", "enabled")
    CALL_FIELD_NUMBER: _ClassVar[int]
    REF_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    call: ToolCallContext
    ref: EntityRef
    enabled: bool
    def __init__(self, call: _Optional[_Union[ToolCallContext, _Mapping]] = ..., ref: _Optional[_Union[EntityRef, _Mapping]] = ..., enabled: bool = ...) -> None: ...

class SetAutomationEnabledResponse(_message.Message):
    __slots__ = ("entity",)
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    entity: EntitySummary
    def __init__(self, entity: _Optional[_Union[EntitySummary, _Mapping]] = ...) -> None: ...

class ExecuteAssetCommandRequest(_message.Message):
    __slots__ = ("call", "asset_sn", "command_id", "params", "target")
    CALL_FIELD_NUMBER: _ClassVar[int]
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    call: ToolCallContext
    asset_sn: str
    command_id: str
    params: _struct_pb2.Struct
    target: _capability_pb2.Target
    def __init__(self, call: _Optional[_Union[ToolCallContext, _Mapping]] = ..., asset_sn: _Optional[str] = ..., command_id: _Optional[str] = ..., params: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., target: _Optional[_Union[_capability_pb2.Target, _Mapping]] = ...) -> None: ...

class ExecuteAssetCommandResponse(_message.Message):
    __slots__ = ("command_execution_id", "state", "result", "error")
    COMMAND_EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    command_execution_id: str
    state: str
    result: _struct_pb2.Struct
    error: _common_pb2.Error
    def __init__(self, command_execution_id: _Optional[str] = ..., state: _Optional[str] = ..., result: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ...) -> None: ...

class StartApplicationRunRequest(_message.Message):
    __slots__ = ("call", "application_id", "asset_sn", "site_id", "inputs")
    CALL_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    call: ToolCallContext
    application_id: str
    asset_sn: str
    site_id: str
    inputs: _struct_pb2.Struct
    def __init__(self, call: _Optional[_Union[ToolCallContext, _Mapping]] = ..., application_id: _Optional[str] = ..., asset_sn: _Optional[str] = ..., site_id: _Optional[str] = ..., inputs: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class StartApplicationRunResponse(_message.Message):
    __slots__ = ("execution_id",)
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    execution_id: str
    def __init__(self, execution_id: _Optional[str] = ...) -> None: ...

class OpenRunSessionRequest(_message.Message):
    __slots__ = ("organization_id", "execution_id", "started_by_user_id", "ttl")
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    STARTED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    organization_id: str
    execution_id: str
    started_by_user_id: str
    ttl: _duration_pb2.Duration
    def __init__(self, organization_id: _Optional[str] = ..., execution_id: _Optional[str] = ..., started_by_user_id: _Optional[str] = ..., ttl: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class OpenRunSessionResponse(_message.Message):
    __slots__ = ("grant",)
    GRANT_FIELD_NUMBER: _ClassVar[int]
    grant: SessionGrant
    def __init__(self, grant: _Optional[_Union[SessionGrant, _Mapping]] = ...) -> None: ...

class CloseRunSessionRequest(_message.Message):
    __slots__ = ("session_id",)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    def __init__(self, session_id: _Optional[str] = ...) -> None: ...

class CloseRunSessionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
