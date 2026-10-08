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

class ToolCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TOOL_CATEGORY_UNSPECIFIED: _ClassVar[ToolCategory]
    TOOL_CATEGORY_READ: _ClassVar[ToolCategory]
    TOOL_CATEGORY_DRAFT: _ClassVar[ToolCategory]
    TOOL_CATEGORY_CHANGE: _ClassVar[ToolCategory]
    TOOL_CATEGORY_ACT_ON_DEVICE: _ClassVar[ToolCategory]

class ModelProvider(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MODEL_PROVIDER_UNSPECIFIED: _ClassVar[ModelProvider]
    MODEL_PROVIDER_ANTHROPIC: _ClassVar[ModelProvider]
    MODEL_PROVIDER_OPENAI: _ClassVar[ModelProvider]
    MODEL_PROVIDER_XAI: _ClassVar[ModelProvider]
    MODEL_PROVIDER_MISTRAL: _ClassVar[ModelProvider]
    MODEL_PROVIDER_AWS_BEDROCK: _ClassVar[ModelProvider]
    MODEL_PROVIDER_GOOGLE_VERTEX: _ClassVar[ModelProvider]
    MODEL_PROVIDER_OPENAI_COMPATIBLE: _ClassVar[ModelProvider]

class DataResidency(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATA_RESIDENCY_UNSPECIFIED: _ClassVar[DataResidency]
    DATA_RESIDENCY_ANY: _ClassVar[DataResidency]
    DATA_RESIDENCY_EU_ONLY: _ClassVar[DataResidency]
    DATA_RESIDENCY_LOCAL_ONLY: _ClassVar[DataResidency]

class ActorKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACTOR_KIND_UNSPECIFIED: _ClassVar[ActorKind]
    ACTOR_KIND_USER: _ClassVar[ActorKind]
    ACTOR_KIND_AUTOMATION: _ClassVar[ActorKind]

class TurnRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TURN_ROLE_UNSPECIFIED: _ClassVar[TurnRole]
    TURN_ROLE_USER: _ClassVar[TurnRole]
    TURN_ROLE_ASSISTANT: _ClassVar[TurnRole]
    TURN_ROLE_TOOL: _ClassVar[TurnRole]
    TURN_ROLE_EVENT: _ClassVar[TurnRole]
    TURN_ROLE_SUMMARY: _ClassVar[TurnRole]

class ApprovalState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    APPROVAL_STATE_UNSPECIFIED: _ClassVar[ApprovalState]
    APPROVAL_STATE_PENDING: _ClassVar[ApprovalState]
    APPROVAL_STATE_APPROVED: _ClassVar[ApprovalState]
    APPROVAL_STATE_REJECTED: _ClassVar[ApprovalState]
    APPROVAL_STATE_EXPIRED: _ClassVar[ApprovalState]
TOOL_CATEGORY_UNSPECIFIED: ToolCategory
TOOL_CATEGORY_READ: ToolCategory
TOOL_CATEGORY_DRAFT: ToolCategory
TOOL_CATEGORY_CHANGE: ToolCategory
TOOL_CATEGORY_ACT_ON_DEVICE: ToolCategory
MODEL_PROVIDER_UNSPECIFIED: ModelProvider
MODEL_PROVIDER_ANTHROPIC: ModelProvider
MODEL_PROVIDER_OPENAI: ModelProvider
MODEL_PROVIDER_XAI: ModelProvider
MODEL_PROVIDER_MISTRAL: ModelProvider
MODEL_PROVIDER_AWS_BEDROCK: ModelProvider
MODEL_PROVIDER_GOOGLE_VERTEX: ModelProvider
MODEL_PROVIDER_OPENAI_COMPATIBLE: ModelProvider
DATA_RESIDENCY_UNSPECIFIED: DataResidency
DATA_RESIDENCY_ANY: DataResidency
DATA_RESIDENCY_EU_ONLY: DataResidency
DATA_RESIDENCY_LOCAL_ONLY: DataResidency
ACTOR_KIND_UNSPECIFIED: ActorKind
ACTOR_KIND_USER: ActorKind
ACTOR_KIND_AUTOMATION: ActorKind
TURN_ROLE_UNSPECIFIED: TurnRole
TURN_ROLE_USER: TurnRole
TURN_ROLE_ASSISTANT: TurnRole
TURN_ROLE_TOOL: TurnRole
TURN_ROLE_EVENT: TurnRole
TURN_ROLE_SUMMARY: TurnRole
APPROVAL_STATE_UNSPECIFIED: ApprovalState
APPROVAL_STATE_PENDING: ApprovalState
APPROVAL_STATE_APPROVED: ApprovalState
APPROVAL_STATE_REJECTED: ApprovalState
APPROVAL_STATE_EXPIRED: ApprovalState

class Model(_message.Message):
    __slots__ = ("id", "display_name", "provider", "model_name", "endpoint", "eu_hosted", "local", "vision", "context_tokens", "input_price_micro_eur_per_mtok", "output_price_micro_eur_per_mtok", "enabled", "updated_at", "updated_by")
    ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    EU_HOSTED_FIELD_NUMBER: _ClassVar[int]
    LOCAL_FIELD_NUMBER: _ClassVar[int]
    VISION_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    INPUT_PRICE_MICRO_EUR_PER_MTOK_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_PRICE_MICRO_EUR_PER_MTOK_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_BY_FIELD_NUMBER: _ClassVar[int]
    id: str
    display_name: str
    provider: ModelProvider
    model_name: str
    endpoint: str
    eu_hosted: bool
    local: bool
    vision: bool
    context_tokens: int
    input_price_micro_eur_per_mtok: int
    output_price_micro_eur_per_mtok: int
    enabled: bool
    updated_at: _timestamp_pb2.Timestamp
    updated_by: str
    def __init__(self, id: _Optional[str] = ..., display_name: _Optional[str] = ..., provider: _Optional[_Union[ModelProvider, str]] = ..., model_name: _Optional[str] = ..., endpoint: _Optional[str] = ..., eu_hosted: bool = ..., local: bool = ..., vision: bool = ..., context_tokens: _Optional[int] = ..., input_price_micro_eur_per_mtok: _Optional[int] = ..., output_price_micro_eur_per_mtok: _Optional[int] = ..., enabled: bool = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_by: _Optional[str] = ...) -> None: ...

class OrganizationModelKey(_message.Message):
    __slots__ = ("provider", "api_key", "api_key_set", "api_key_hint", "updated_at", "updated_by")
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    API_KEY_SET_FIELD_NUMBER: _ClassVar[int]
    API_KEY_HINT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_BY_FIELD_NUMBER: _ClassVar[int]
    provider: ModelProvider
    api_key: str
    api_key_set: bool
    api_key_hint: str
    updated_at: _timestamp_pb2.Timestamp
    updated_by: str
    def __init__(self, provider: _Optional[_Union[ModelProvider, str]] = ..., api_key: _Optional[str] = ..., api_key_set: bool = ..., api_key_hint: _Optional[str] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_by: _Optional[str] = ...) -> None: ...

class ListModelsRequest(_message.Message):
    __slots__ = ("include_disabled",)
    INCLUDE_DISABLED_FIELD_NUMBER: _ClassVar[int]
    include_disabled: bool
    def __init__(self, include_disabled: bool = ...) -> None: ...

class ListModelsResponse(_message.Message):
    __slots__ = ("models",)
    MODELS_FIELD_NUMBER: _ClassVar[int]
    models: _containers.RepeatedCompositeFieldContainer[Model]
    def __init__(self, models: _Optional[_Iterable[_Union[Model, _Mapping]]] = ...) -> None: ...

class SaveModelRequest(_message.Message):
    __slots__ = ("context", "model")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    model: Model
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., model: _Optional[_Union[Model, _Mapping]] = ...) -> None: ...

class SaveModelResponse(_message.Message):
    __slots__ = ("model",)
    MODEL_FIELD_NUMBER: _ClassVar[int]
    model: Model
    def __init__(self, model: _Optional[_Union[Model, _Mapping]] = ...) -> None: ...

class DeleteModelRequest(_message.Message):
    __slots__ = ("context", "model_id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    model_id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., model_id: _Optional[str] = ...) -> None: ...

class DeleteModelResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListOrganizationModelKeysRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListOrganizationModelKeysResponse(_message.Message):
    __slots__ = ("keys",)
    KEYS_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedCompositeFieldContainer[OrganizationModelKey]
    def __init__(self, keys: _Optional[_Iterable[_Union[OrganizationModelKey, _Mapping]]] = ...) -> None: ...

class SetOrganizationModelKeyRequest(_message.Message):
    __slots__ = ("context", "key")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    key: OrganizationModelKey
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., key: _Optional[_Union[OrganizationModelKey, _Mapping]] = ...) -> None: ...

class SetOrganizationModelKeyResponse(_message.Message):
    __slots__ = ("key",)
    KEY_FIELD_NUMBER: _ClassVar[int]
    key: OrganizationModelKey
    def __init__(self, key: _Optional[_Union[OrganizationModelKey, _Mapping]] = ...) -> None: ...

class DeleteOrganizationModelKeyRequest(_message.Message):
    __slots__ = ("context", "provider")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    provider: ModelProvider
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., provider: _Optional[_Union[ModelProvider, str]] = ...) -> None: ...

class DeleteOrganizationModelKeyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ResolveOrganizationModelKeyRequest(_message.Message):
    __slots__ = ("organization_id", "provider")
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    organization_id: str
    provider: ModelProvider
    def __init__(self, organization_id: _Optional[str] = ..., provider: _Optional[_Union[ModelProvider, str]] = ...) -> None: ...

class ResolveOrganizationModelKeyResponse(_message.Message):
    __slots__ = ("api_key",)
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    api_key: str
    def __init__(self, api_key: _Optional[str] = ...) -> None: ...

class DataSharing(_message.Message):
    __slots__ = ("telemetry", "positions", "video_frames", "personal_names")
    TELEMETRY_FIELD_NUMBER: _ClassVar[int]
    POSITIONS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FRAMES_FIELD_NUMBER: _ClassVar[int]
    PERSONAL_NAMES_FIELD_NUMBER: _ClassVar[int]
    telemetry: bool
    positions: bool
    video_frames: bool
    personal_names: bool
    def __init__(self, telemetry: bool = ..., positions: bool = ..., video_frames: bool = ..., personal_names: bool = ...) -> None: ...

class RoleAgentPolicy(_message.Message):
    __slots__ = ("role_id", "allowed_model_ids", "default_model_id", "daily_limit_micro_eur", "monthly_limit_micro_eur", "allowed_categories", "approval_required_categories")
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_MODEL_IDS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    DAILY_LIMIT_MICRO_EUR_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_LIMIT_MICRO_EUR_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_REQUIRED_CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    role_id: str
    allowed_model_ids: _containers.RepeatedScalarFieldContainer[str]
    default_model_id: str
    daily_limit_micro_eur: int
    monthly_limit_micro_eur: int
    allowed_categories: _containers.RepeatedScalarFieldContainer[ToolCategory]
    approval_required_categories: _containers.RepeatedScalarFieldContainer[ToolCategory]
    def __init__(self, role_id: _Optional[str] = ..., allowed_model_ids: _Optional[_Iterable[str]] = ..., default_model_id: _Optional[str] = ..., daily_limit_micro_eur: _Optional[int] = ..., monthly_limit_micro_eur: _Optional[int] = ..., allowed_categories: _Optional[_Iterable[_Union[ToolCategory, str]]] = ..., approval_required_categories: _Optional[_Iterable[_Union[ToolCategory, str]]] = ...) -> None: ...

class AgentPolicy(_message.Message):
    __slots__ = ("organization_id", "site_id", "enabled", "suspended", "suspended_reason", "data_residency", "allowed_model_ids", "default_model_id", "data_sharing", "monthly_budget_micro_eur", "roles", "allowed_site_ids", "allowed_asset_sns", "simulator_first", "four_eyes", "conversation_retention_days", "audit_retention_days", "revision", "updated_at", "updated_by")
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    SUSPENDED_FIELD_NUMBER: _ClassVar[int]
    SUSPENDED_REASON_FIELD_NUMBER: _ClassVar[int]
    DATA_RESIDENCY_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_MODEL_IDS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_SHARING_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_BUDGET_MICRO_EUR_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_SITE_IDS_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_ASSET_SNS_FIELD_NUMBER: _ClassVar[int]
    SIMULATOR_FIRST_FIELD_NUMBER: _ClassVar[int]
    FOUR_EYES_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_RETENTION_DAYS_FIELD_NUMBER: _ClassVar[int]
    AUDIT_RETENTION_DAYS_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_BY_FIELD_NUMBER: _ClassVar[int]
    organization_id: str
    site_id: str
    enabled: bool
    suspended: bool
    suspended_reason: str
    data_residency: DataResidency
    allowed_model_ids: _containers.RepeatedScalarFieldContainer[str]
    default_model_id: str
    data_sharing: DataSharing
    monthly_budget_micro_eur: int
    roles: _containers.RepeatedCompositeFieldContainer[RoleAgentPolicy]
    allowed_site_ids: _containers.RepeatedScalarFieldContainer[str]
    allowed_asset_sns: _containers.RepeatedScalarFieldContainer[str]
    simulator_first: bool
    four_eyes: bool
    conversation_retention_days: int
    audit_retention_days: int
    revision: str
    updated_at: _timestamp_pb2.Timestamp
    updated_by: str
    def __init__(self, organization_id: _Optional[str] = ..., site_id: _Optional[str] = ..., enabled: bool = ..., suspended: bool = ..., suspended_reason: _Optional[str] = ..., data_residency: _Optional[_Union[DataResidency, str]] = ..., allowed_model_ids: _Optional[_Iterable[str]] = ..., default_model_id: _Optional[str] = ..., data_sharing: _Optional[_Union[DataSharing, _Mapping]] = ..., monthly_budget_micro_eur: _Optional[int] = ..., roles: _Optional[_Iterable[_Union[RoleAgentPolicy, _Mapping]]] = ..., allowed_site_ids: _Optional[_Iterable[str]] = ..., allowed_asset_sns: _Optional[_Iterable[str]] = ..., simulator_first: bool = ..., four_eyes: bool = ..., conversation_retention_days: _Optional[int] = ..., audit_retention_days: _Optional[int] = ..., revision: _Optional[str] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_by: _Optional[str] = ...) -> None: ...

class UsageEntry(_message.Message):
    __slots__ = ("day", "user_id", "role_id", "model_id", "input_tokens", "output_tokens", "requests", "cost_micro_eur")
    DAY_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    COST_MICRO_EUR_FIELD_NUMBER: _ClassVar[int]
    day: str
    user_id: str
    role_id: str
    model_id: str
    input_tokens: int
    output_tokens: int
    requests: int
    cost_micro_eur: int
    def __init__(self, day: _Optional[str] = ..., user_id: _Optional[str] = ..., role_id: _Optional[str] = ..., model_id: _Optional[str] = ..., input_tokens: _Optional[int] = ..., output_tokens: _Optional[int] = ..., requests: _Optional[int] = ..., cost_micro_eur: _Optional[int] = ...) -> None: ...

class GetAgentPolicyRequest(_message.Message):
    __slots__ = ("site_id",)
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    site_id: str
    def __init__(self, site_id: _Optional[str] = ...) -> None: ...

class GetAgentPolicyResponse(_message.Message):
    __slots__ = ("policy",)
    POLICY_FIELD_NUMBER: _ClassVar[int]
    policy: AgentPolicy
    def __init__(self, policy: _Optional[_Union[AgentPolicy, _Mapping]] = ...) -> None: ...

class UpdateAgentPolicyRequest(_message.Message):
    __slots__ = ("context", "policy", "expected_revision")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_REVISION_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    policy: AgentPolicy
    expected_revision: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., policy: _Optional[_Union[AgentPolicy, _Mapping]] = ..., expected_revision: _Optional[str] = ...) -> None: ...

class UpdateAgentPolicyResponse(_message.Message):
    __slots__ = ("policy",)
    POLICY_FIELD_NUMBER: _ClassVar[int]
    policy: AgentPolicy
    def __init__(self, policy: _Optional[_Union[AgentPolicy, _Mapping]] = ...) -> None: ...

class GetAgentUsageRequest(_message.Message):
    __slots__ = ("from_day", "to_day", "user_id", "role_id")
    FROM_DAY_FIELD_NUMBER: _ClassVar[int]
    TO_DAY_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    from_day: str
    to_day: str
    user_id: str
    role_id: str
    def __init__(self, from_day: _Optional[str] = ..., to_day: _Optional[str] = ..., user_id: _Optional[str] = ..., role_id: _Optional[str] = ...) -> None: ...

class GetAgentUsageResponse(_message.Message):
    __slots__ = ("entries", "month_cost_micro_eur", "monthly_budget_micro_eur")
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    MONTH_COST_MICRO_EUR_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_BUDGET_MICRO_EUR_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[UsageEntry]
    month_cost_micro_eur: int
    monthly_budget_micro_eur: int
    def __init__(self, entries: _Optional[_Iterable[_Union[UsageEntry, _Mapping]]] = ..., month_cost_micro_eur: _Optional[int] = ..., monthly_budget_micro_eur: _Optional[int] = ...) -> None: ...

class RecordAgentUsageRequest(_message.Message):
    __slots__ = ("organization_id", "entries")
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    organization_id: str
    entries: _containers.RepeatedCompositeFieldContainer[UsageEntry]
    def __init__(self, organization_id: _Optional[str] = ..., entries: _Optional[_Iterable[_Union[UsageEntry, _Mapping]]] = ...) -> None: ...

class RecordAgentUsageResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ConversationContext(_message.Message):
    __slots__ = ("asset_sn", "application_id", "site_id", "screen")
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    SCREEN_FIELD_NUMBER: _ClassVar[int]
    asset_sn: str
    application_id: str
    site_id: str
    screen: str
    def __init__(self, asset_sn: _Optional[str] = ..., application_id: _Optional[str] = ..., site_id: _Optional[str] = ..., screen: _Optional[str] = ...) -> None: ...

class ToolCallRecord(_message.Message):
    __slots__ = ("id", "tool", "category", "arguments", "approval", "approval_id", "decided_by", "result", "error", "duration_ms", "audit_event_ids")
    ID_FIELD_NUMBER: _ClassVar[int]
    TOOL_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_ID_FIELD_NUMBER: _ClassVar[int]
    DECIDED_BY_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    AUDIT_EVENT_IDS_FIELD_NUMBER: _ClassVar[int]
    id: str
    tool: str
    category: ToolCategory
    arguments: _struct_pb2.Struct
    approval: ApprovalState
    approval_id: str
    decided_by: str
    result: _struct_pb2.Struct
    error: _common_pb2.Error
    duration_ms: int
    audit_event_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., tool: _Optional[str] = ..., category: _Optional[_Union[ToolCategory, str]] = ..., arguments: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., approval: _Optional[_Union[ApprovalState, str]] = ..., approval_id: _Optional[str] = ..., decided_by: _Optional[str] = ..., result: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ..., duration_ms: _Optional[int] = ..., audit_event_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class Turn(_message.Message):
    __slots__ = ("id", "conversation_id", "sequence", "role", "text", "tool_calls", "model_id", "input_tokens", "output_tokens", "cost_micro_eur", "ai_generated", "summarizes_until_sequence", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALLS_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    COST_MICRO_EUR_FIELD_NUMBER: _ClassVar[int]
    AI_GENERATED_FIELD_NUMBER: _ClassVar[int]
    SUMMARIZES_UNTIL_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    conversation_id: str
    sequence: int
    role: TurnRole
    text: str
    tool_calls: _containers.RepeatedCompositeFieldContainer[ToolCallRecord]
    model_id: str
    input_tokens: int
    output_tokens: int
    cost_micro_eur: int
    ai_generated: bool
    summarizes_until_sequence: int
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., conversation_id: _Optional[str] = ..., sequence: _Optional[int] = ..., role: _Optional[_Union[TurnRole, str]] = ..., text: _Optional[str] = ..., tool_calls: _Optional[_Iterable[_Union[ToolCallRecord, _Mapping]]] = ..., model_id: _Optional[str] = ..., input_tokens: _Optional[int] = ..., output_tokens: _Optional[int] = ..., cost_micro_eur: _Optional[int] = ..., ai_generated: bool = ..., summarizes_until_sequence: _Optional[int] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Conversation(_message.Message):
    __slots__ = ("id", "organization_id", "actor_kind", "actor_id", "execution_id", "node_id", "title", "context", "archived", "created_at", "updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    ACTOR_KIND_FIELD_NUMBER: _ClassVar[int]
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    organization_id: str
    actor_kind: ActorKind
    actor_id: str
    execution_id: str
    node_id: str
    title: str
    context: ConversationContext
    archived: bool
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., organization_id: _Optional[str] = ..., actor_kind: _Optional[_Union[ActorKind, str]] = ..., actor_id: _Optional[str] = ..., execution_id: _Optional[str] = ..., node_id: _Optional[str] = ..., title: _Optional[str] = ..., context: _Optional[_Union[ConversationContext, _Mapping]] = ..., archived: bool = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class MemoryFact(_message.Message):
    __slots__ = ("id", "organization_id", "site_id", "text", "source_conversation_id", "created_by", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    organization_id: str
    site_id: str
    text: str
    source_conversation_id: str
    created_by: str
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., organization_id: _Optional[str] = ..., site_id: _Optional[str] = ..., text: _Optional[str] = ..., source_conversation_id: _Optional[str] = ..., created_by: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateConversationRequest(_message.Message):
    __slots__ = ("context", "conversation")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    conversation: Conversation
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., conversation: _Optional[_Union[Conversation, _Mapping]] = ...) -> None: ...

class CreateConversationResponse(_message.Message):
    __slots__ = ("conversation",)
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    conversation: Conversation
    def __init__(self, conversation: _Optional[_Union[Conversation, _Mapping]] = ...) -> None: ...

class GetConversationRequest(_message.Message):
    __slots__ = ("conversation_id",)
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    conversation_id: str
    def __init__(self, conversation_id: _Optional[str] = ...) -> None: ...

class GetConversationResponse(_message.Message):
    __slots__ = ("conversation", "last_sequence")
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    LAST_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    conversation: Conversation
    last_sequence: int
    def __init__(self, conversation: _Optional[_Union[Conversation, _Mapping]] = ..., last_sequence: _Optional[int] = ...) -> None: ...

class ListConversationsRequest(_message.Message):
    __slots__ = ("include_archived", "actor_id", "page")
    INCLUDE_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    include_archived: bool
    actor_id: str
    page: _common_pb2.PageRequest
    def __init__(self, include_archived: bool = ..., actor_id: _Optional[str] = ..., page: _Optional[_Union[_common_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class ListConversationsResponse(_message.Message):
    __slots__ = ("conversations", "page")
    CONVERSATIONS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    conversations: _containers.RepeatedCompositeFieldContainer[Conversation]
    page: _common_pb2.PageResponse
    def __init__(self, conversations: _Optional[_Iterable[_Union[Conversation, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class UpdateConversationRequest(_message.Message):
    __slots__ = ("context", "conversation_id", "title", "archived")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    conversation_id: str
    title: str
    archived: bool
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., conversation_id: _Optional[str] = ..., title: _Optional[str] = ..., archived: bool = ...) -> None: ...

class UpdateConversationResponse(_message.Message):
    __slots__ = ("conversation",)
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    conversation: Conversation
    def __init__(self, conversation: _Optional[_Union[Conversation, _Mapping]] = ...) -> None: ...

class DeleteConversationRequest(_message.Message):
    __slots__ = ("context", "conversation_id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    conversation_id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., conversation_id: _Optional[str] = ...) -> None: ...

class DeleteConversationResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AppendTurnsRequest(_message.Message):
    __slots__ = ("context", "conversation_id", "expected_last_sequence", "turns")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_LAST_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    TURNS_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    conversation_id: str
    expected_last_sequence: int
    turns: _containers.RepeatedCompositeFieldContainer[Turn]
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., conversation_id: _Optional[str] = ..., expected_last_sequence: _Optional[int] = ..., turns: _Optional[_Iterable[_Union[Turn, _Mapping]]] = ...) -> None: ...

class AppendTurnsResponse(_message.Message):
    __slots__ = ("turns", "last_sequence")
    TURNS_FIELD_NUMBER: _ClassVar[int]
    LAST_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    turns: _containers.RepeatedCompositeFieldContainer[Turn]
    last_sequence: int
    def __init__(self, turns: _Optional[_Iterable[_Union[Turn, _Mapping]]] = ..., last_sequence: _Optional[int] = ...) -> None: ...

class ListTurnsRequest(_message.Message):
    __slots__ = ("conversation_id", "after_sequence", "page")
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    AFTER_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    conversation_id: str
    after_sequence: int
    page: _common_pb2.PageRequest
    def __init__(self, conversation_id: _Optional[str] = ..., after_sequence: _Optional[int] = ..., page: _Optional[_Union[_common_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class ListTurnsResponse(_message.Message):
    __slots__ = ("turns", "page")
    TURNS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    turns: _containers.RepeatedCompositeFieldContainer[Turn]
    page: _common_pb2.PageResponse
    def __init__(self, turns: _Optional[_Iterable[_Union[Turn, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class ExportConversationsRequest(_message.Message):
    __slots__ = ("actor_id",)
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    actor_id: str
    def __init__(self, actor_id: _Optional[str] = ...) -> None: ...

class ExportConversationsResponse(_message.Message):
    __slots__ = ("chunk",)
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    chunk: bytes
    def __init__(self, chunk: _Optional[bytes] = ...) -> None: ...

class ListMemoryFactsRequest(_message.Message):
    __slots__ = ("site_id", "page")
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    site_id: str
    page: _common_pb2.PageRequest
    def __init__(self, site_id: _Optional[str] = ..., page: _Optional[_Union[_common_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class ListMemoryFactsResponse(_message.Message):
    __slots__ = ("facts", "page")
    FACTS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    facts: _containers.RepeatedCompositeFieldContainer[MemoryFact]
    page: _common_pb2.PageResponse
    def __init__(self, facts: _Optional[_Iterable[_Union[MemoryFact, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class SaveMemoryFactRequest(_message.Message):
    __slots__ = ("context", "fact")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    FACT_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    fact: MemoryFact
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., fact: _Optional[_Union[MemoryFact, _Mapping]] = ...) -> None: ...

class SaveMemoryFactResponse(_message.Message):
    __slots__ = ("fact",)
    FACT_FIELD_NUMBER: _ClassVar[int]
    fact: MemoryFact
    def __init__(self, fact: _Optional[_Union[MemoryFact, _Mapping]] = ...) -> None: ...

class DeleteMemoryFactRequest(_message.Message):
    __slots__ = ("context", "fact_id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    FACT_ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    fact_id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., fact_id: _Optional[str] = ...) -> None: ...

class DeleteMemoryFactResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
