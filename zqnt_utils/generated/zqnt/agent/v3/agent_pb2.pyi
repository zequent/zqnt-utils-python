import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from zqnt_utils.generated.zqnt.capability.v3 import capability_pb2 as _capability_pb2
from zqnt_utils.generated.zqnt.common.v3 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ModelProvider(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MODEL_PROVIDER_UNSPECIFIED: _ClassVar[ModelProvider]
    MODEL_PROVIDER_ANTHROPIC: _ClassVar[ModelProvider]
    MODEL_PROVIDER_OPENAI: _ClassVar[ModelProvider]
    MODEL_PROVIDER_OPENAI_COMPATIBLE: _ClassVar[ModelProvider]

class DataResidency(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATA_RESIDENCY_UNSPECIFIED: _ClassVar[DataResidency]
    DATA_RESIDENCY_ANY: _ClassVar[DataResidency]
    DATA_RESIDENCY_EU_ONLY: _ClassVar[DataResidency]
    DATA_RESIDENCY_LOCAL_ONLY: _ClassVar[DataResidency]

class MessageRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MESSAGE_ROLE_UNSPECIFIED: _ClassVar[MessageRole]
    MESSAGE_ROLE_USER: _ClassVar[MessageRole]
    MESSAGE_ROLE_ASSISTANT: _ClassVar[MessageRole]
    MESSAGE_ROLE_TOOL: _ClassVar[MessageRole]
    MESSAGE_ROLE_EVENT: _ClassVar[MessageRole]

class ApprovalState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    APPROVAL_STATE_UNSPECIFIED: _ClassVar[ApprovalState]
    APPROVAL_STATE_PENDING: _ClassVar[ApprovalState]
    APPROVAL_STATE_APPROVED: _ClassVar[ApprovalState]
    APPROVAL_STATE_REJECTED: _ClassVar[ApprovalState]
    APPROVAL_STATE_EXPIRED: _ClassVar[ApprovalState]
MODEL_PROVIDER_UNSPECIFIED: ModelProvider
MODEL_PROVIDER_ANTHROPIC: ModelProvider
MODEL_PROVIDER_OPENAI: ModelProvider
MODEL_PROVIDER_OPENAI_COMPATIBLE: ModelProvider
DATA_RESIDENCY_UNSPECIFIED: DataResidency
DATA_RESIDENCY_ANY: DataResidency
DATA_RESIDENCY_EU_ONLY: DataResidency
DATA_RESIDENCY_LOCAL_ONLY: DataResidency
MESSAGE_ROLE_UNSPECIFIED: MessageRole
MESSAGE_ROLE_USER: MessageRole
MESSAGE_ROLE_ASSISTANT: MessageRole
MESSAGE_ROLE_TOOL: MessageRole
MESSAGE_ROLE_EVENT: MessageRole
APPROVAL_STATE_UNSPECIFIED: ApprovalState
APPROVAL_STATE_PENDING: ApprovalState
APPROVAL_STATE_APPROVED: ApprovalState
APPROVAL_STATE_REJECTED: ApprovalState
APPROVAL_STATE_EXPIRED: ApprovalState

class ModelEndpoint(_message.Message):
    __slots__ = ("id", "provider", "model", "base_url", "eu_hosted", "local", "api_key", "api_key_set")
    ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    BASE_URL_FIELD_NUMBER: _ClassVar[int]
    EU_HOSTED_FIELD_NUMBER: _ClassVar[int]
    LOCAL_FIELD_NUMBER: _ClassVar[int]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    API_KEY_SET_FIELD_NUMBER: _ClassVar[int]
    id: str
    provider: ModelProvider
    model: str
    base_url: str
    eu_hosted: bool
    local: bool
    api_key: str
    api_key_set: bool
    def __init__(self, id: _Optional[str] = ..., provider: _Optional[_Union[ModelProvider, str]] = ..., model: _Optional[str] = ..., base_url: _Optional[str] = ..., eu_hosted: bool = ..., local: bool = ..., api_key: _Optional[str] = ..., api_key_set: bool = ...) -> None: ...

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

class AgentPolicy(_message.Message):
    __slots__ = ("organization_id", "site_id", "enabled", "allowed_role_ids", "max_command_risk", "may_save_changes", "may_start_executions", "allowed_tool_categories", "allowed_site_ids", "allowed_asset_sns", "simulator_first", "four_eyes", "data_residency", "endpoints", "default_endpoint_id", "data_sharing", "conversation_retention", "monthly_token_budget", "per_user_daily_token_limit", "suspended", "suspended_reason", "revision", "updated_at", "updated_by")
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_ROLE_IDS_FIELD_NUMBER: _ClassVar[int]
    MAX_COMMAND_RISK_FIELD_NUMBER: _ClassVar[int]
    MAY_SAVE_CHANGES_FIELD_NUMBER: _ClassVar[int]
    MAY_START_EXECUTIONS_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_TOOL_CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_SITE_IDS_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_ASSET_SNS_FIELD_NUMBER: _ClassVar[int]
    SIMULATOR_FIRST_FIELD_NUMBER: _ClassVar[int]
    FOUR_EYES_FIELD_NUMBER: _ClassVar[int]
    DATA_RESIDENCY_FIELD_NUMBER: _ClassVar[int]
    ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_SHARING_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_RETENTION_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_TOKEN_BUDGET_FIELD_NUMBER: _ClassVar[int]
    PER_USER_DAILY_TOKEN_LIMIT_FIELD_NUMBER: _ClassVar[int]
    SUSPENDED_FIELD_NUMBER: _ClassVar[int]
    SUSPENDED_REASON_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_BY_FIELD_NUMBER: _ClassVar[int]
    organization_id: str
    site_id: str
    enabled: bool
    allowed_role_ids: _containers.RepeatedScalarFieldContainer[str]
    max_command_risk: _capability_pb2.CommandRisk
    may_save_changes: bool
    may_start_executions: bool
    allowed_tool_categories: _containers.RepeatedScalarFieldContainer[str]
    allowed_site_ids: _containers.RepeatedScalarFieldContainer[str]
    allowed_asset_sns: _containers.RepeatedScalarFieldContainer[str]
    simulator_first: bool
    four_eyes: bool
    data_residency: DataResidency
    endpoints: _containers.RepeatedCompositeFieldContainer[ModelEndpoint]
    default_endpoint_id: str
    data_sharing: DataSharing
    conversation_retention: _duration_pb2.Duration
    monthly_token_budget: int
    per_user_daily_token_limit: int
    suspended: bool
    suspended_reason: str
    revision: str
    updated_at: _timestamp_pb2.Timestamp
    updated_by: str
    def __init__(self, organization_id: _Optional[str] = ..., site_id: _Optional[str] = ..., enabled: bool = ..., allowed_role_ids: _Optional[_Iterable[str]] = ..., max_command_risk: _Optional[_Union[_capability_pb2.CommandRisk, str]] = ..., may_save_changes: bool = ..., may_start_executions: bool = ..., allowed_tool_categories: _Optional[_Iterable[str]] = ..., allowed_site_ids: _Optional[_Iterable[str]] = ..., allowed_asset_sns: _Optional[_Iterable[str]] = ..., simulator_first: bool = ..., four_eyes: bool = ..., data_residency: _Optional[_Union[DataResidency, str]] = ..., endpoints: _Optional[_Iterable[_Union[ModelEndpoint, _Mapping]]] = ..., default_endpoint_id: _Optional[str] = ..., data_sharing: _Optional[_Union[DataSharing, _Mapping]] = ..., conversation_retention: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., monthly_token_budget: _Optional[int] = ..., per_user_daily_token_limit: _Optional[int] = ..., suspended: bool = ..., suspended_reason: _Optional[str] = ..., revision: _Optional[str] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_by: _Optional[str] = ...) -> None: ...

class ToolCall(_message.Message):
    __slots__ = ("id", "tool", "arguments", "risk", "approval", "decided_by", "result", "error", "audit_event_ids")
    ID_FIELD_NUMBER: _ClassVar[int]
    TOOL_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    RISK_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_FIELD_NUMBER: _ClassVar[int]
    DECIDED_BY_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    AUDIT_EVENT_IDS_FIELD_NUMBER: _ClassVar[int]
    id: str
    tool: str
    arguments: _struct_pb2.Struct
    risk: _capability_pb2.CommandRisk
    approval: ApprovalState
    decided_by: str
    result: _struct_pb2.Struct
    error: _common_pb2.Error
    audit_event_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., tool: _Optional[str] = ..., arguments: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., risk: _Optional[_Union[_capability_pb2.CommandRisk, str]] = ..., approval: _Optional[_Union[ApprovalState, str]] = ..., decided_by: _Optional[str] = ..., result: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ..., audit_event_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class Message(_message.Message):
    __slots__ = ("id", "session_id", "role", "text", "tool_calls", "input_tokens", "output_tokens", "model_endpoint_id", "ai_generated", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALLS_FIELD_NUMBER: _ClassVar[int]
    INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    MODEL_ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    AI_GENERATED_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    session_id: str
    role: MessageRole
    text: str
    tool_calls: _containers.RepeatedCompositeFieldContainer[ToolCall]
    input_tokens: int
    output_tokens: int
    model_endpoint_id: str
    ai_generated: bool
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., session_id: _Optional[str] = ..., role: _Optional[_Union[MessageRole, str]] = ..., text: _Optional[str] = ..., tool_calls: _Optional[_Iterable[_Union[ToolCall, _Mapping]]] = ..., input_tokens: _Optional[int] = ..., output_tokens: _Optional[int] = ..., model_endpoint_id: _Optional[str] = ..., ai_generated: bool = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class PageContext(_message.Message):
    __slots__ = ("screen", "selection")
    SCREEN_FIELD_NUMBER: _ClassVar[int]
    SELECTION_FIELD_NUMBER: _ClassVar[int]
    screen: str
    selection: _struct_pb2.Struct
    def __init__(self, screen: _Optional[str] = ..., selection: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class Session(_message.Message):
    __slots__ = ("id", "organization_id", "user_id", "title", "context", "archived", "created_at", "updated_at", "expires_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    organization_id: str
    user_id: str
    title: str
    context: PageContext
    archived: bool
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    expires_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., organization_id: _Optional[str] = ..., user_id: _Optional[str] = ..., title: _Optional[str] = ..., context: _Optional[_Union[PageContext, _Mapping]] = ..., archived: bool = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class UsageDay(_message.Message):
    __slots__ = ("day", "user_id", "input_tokens", "output_tokens", "requests", "cost_estimate")
    DAY_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    COST_ESTIMATE_FIELD_NUMBER: _ClassVar[int]
    day: str
    user_id: str
    input_tokens: int
    output_tokens: int
    requests: int
    cost_estimate: float
    def __init__(self, day: _Optional[str] = ..., user_id: _Optional[str] = ..., input_tokens: _Optional[int] = ..., output_tokens: _Optional[int] = ..., requests: _Optional[int] = ..., cost_estimate: _Optional[float] = ...) -> None: ...

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

class PreviewAgentToolsRequest(_message.Message):
    __slots__ = ("role_id", "site_id")
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    role_id: str
    site_id: str
    def __init__(self, role_id: _Optional[str] = ..., site_id: _Optional[str] = ...) -> None: ...

class PreviewAgentToolsResponse(_message.Message):
    __slots__ = ("tools", "refused_tools")
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    REFUSED_TOOLS_FIELD_NUMBER: _ClassVar[int]
    tools: _containers.RepeatedScalarFieldContainer[str]
    refused_tools: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, tools: _Optional[_Iterable[str]] = ..., refused_tools: _Optional[_Iterable[str]] = ...) -> None: ...

class GetAgentUsageRequest(_message.Message):
    __slots__ = ("from_day", "to_day", "user_id")
    FROM_DAY_FIELD_NUMBER: _ClassVar[int]
    TO_DAY_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    from_day: str
    to_day: str
    user_id: str
    def __init__(self, from_day: _Optional[str] = ..., to_day: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class GetAgentUsageResponse(_message.Message):
    __slots__ = ("days", "month_tokens", "monthly_token_budget")
    DAYS_FIELD_NUMBER: _ClassVar[int]
    MONTH_TOKENS_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_TOKEN_BUDGET_FIELD_NUMBER: _ClassVar[int]
    days: _containers.RepeatedCompositeFieldContainer[UsageDay]
    month_tokens: int
    monthly_token_budget: int
    def __init__(self, days: _Optional[_Iterable[_Union[UsageDay, _Mapping]]] = ..., month_tokens: _Optional[int] = ..., monthly_token_budget: _Optional[int] = ...) -> None: ...

class CreateSessionRequest(_message.Message):
    __slots__ = ("context", "title", "page_context")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    PAGE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    title: str
    page_context: PageContext
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., title: _Optional[str] = ..., page_context: _Optional[_Union[PageContext, _Mapping]] = ...) -> None: ...

class CreateSessionResponse(_message.Message):
    __slots__ = ("session",)
    SESSION_FIELD_NUMBER: _ClassVar[int]
    session: Session
    def __init__(self, session: _Optional[_Union[Session, _Mapping]] = ...) -> None: ...

class GetSessionRequest(_message.Message):
    __slots__ = ("session_id",)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    def __init__(self, session_id: _Optional[str] = ...) -> None: ...

class GetSessionResponse(_message.Message):
    __slots__ = ("session",)
    SESSION_FIELD_NUMBER: _ClassVar[int]
    session: Session
    def __init__(self, session: _Optional[_Union[Session, _Mapping]] = ...) -> None: ...

class ListSessionsRequest(_message.Message):
    __slots__ = ("include_archived", "page")
    INCLUDE_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    include_archived: bool
    page: _common_pb2.PageRequest
    def __init__(self, include_archived: bool = ..., page: _Optional[_Union[_common_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class ListSessionsResponse(_message.Message):
    __slots__ = ("sessions", "page")
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    sessions: _containers.RepeatedCompositeFieldContainer[Session]
    page: _common_pb2.PageResponse
    def __init__(self, sessions: _Optional[_Iterable[_Union[Session, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class UpdateSessionRequest(_message.Message):
    __slots__ = ("session_id", "title", "archived")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    title: str
    archived: bool
    def __init__(self, session_id: _Optional[str] = ..., title: _Optional[str] = ..., archived: bool = ...) -> None: ...

class UpdateSessionResponse(_message.Message):
    __slots__ = ("session",)
    SESSION_FIELD_NUMBER: _ClassVar[int]
    session: Session
    def __init__(self, session: _Optional[_Union[Session, _Mapping]] = ...) -> None: ...

class DeleteSessionRequest(_message.Message):
    __slots__ = ("session_id",)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    def __init__(self, session_id: _Optional[str] = ...) -> None: ...

class DeleteSessionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AppendMessageRequest(_message.Message):
    __slots__ = ("context", "message")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    message: Message
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., message: _Optional[_Union[Message, _Mapping]] = ...) -> None: ...

class AppendMessageResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: Message
    def __init__(self, message: _Optional[_Union[Message, _Mapping]] = ...) -> None: ...

class ListMessagesRequest(_message.Message):
    __slots__ = ("session_id", "page")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    page: _common_pb2.PageRequest
    def __init__(self, session_id: _Optional[str] = ..., page: _Optional[_Union[_common_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class ListMessagesResponse(_message.Message):
    __slots__ = ("messages", "page")
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[Message]
    page: _common_pb2.PageResponse
    def __init__(self, messages: _Optional[_Iterable[_Union[Message, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class DecideToolCallRequest(_message.Message):
    __slots__ = ("context", "session_id", "tool_call_id", "approved", "reason")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    APPROVED_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    session_id: str
    tool_call_id: str
    approved: bool
    reason: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., session_id: _Optional[str] = ..., tool_call_id: _Optional[str] = ..., approved: bool = ..., reason: _Optional[str] = ...) -> None: ...

class DecideToolCallResponse(_message.Message):
    __slots__ = ("tool_call",)
    TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    tool_call: ToolCall
    def __init__(self, tool_call: _Optional[_Union[ToolCall, _Mapping]] = ...) -> None: ...

class ExportSessionsRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class ExportSessionsResponse(_message.Message):
    __slots__ = ("chunk",)
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    chunk: bytes
    def __init__(self, chunk: _Optional[bytes] = ...) -> None: ...
