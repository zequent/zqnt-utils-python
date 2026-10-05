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

class ActorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACTOR_TYPE_UNSPECIFIED: _ClassVar[ActorType]
    ACTOR_TYPE_USER: _ClassVar[ActorType]
    ACTOR_TYPE_AGENT: _ClassVar[ActorType]
    ACTOR_TYPE_SERVICE: _ClassVar[ActorType]
    ACTOR_TYPE_EDGE: _ClassVar[ActorType]
    ACTOR_TYPE_SYSTEM: _ClassVar[ActorType]

class AuditAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUDIT_ACTION_UNSPECIFIED: _ClassVar[AuditAction]
    AUDIT_ACTION_CREATE: _ClassVar[AuditAction]
    AUDIT_ACTION_UPDATE: _ClassVar[AuditAction]
    AUDIT_ACTION_DELETE: _ClassVar[AuditAction]
    AUDIT_ACTION_ENABLE: _ClassVar[AuditAction]
    AUDIT_ACTION_DISABLE: _ClassVar[AuditAction]
    AUDIT_ACTION_START: _ClassVar[AuditAction]
    AUDIT_ACTION_CANCEL: _ClassVar[AuditAction]
    AUDIT_ACTION_APPROVE: _ClassVar[AuditAction]
    AUDIT_ACTION_REJECT: _ClassVar[AuditAction]
    AUDIT_ACTION_COMMAND: _ClassVar[AuditAction]
    AUDIT_ACTION_LOGIN: _ClassVar[AuditAction]
    AUDIT_ACTION_LOGOUT: _ClassVar[AuditAction]
    AUDIT_ACTION_EXPORT: _ClassVar[AuditAction]
    AUDIT_ACTION_PROMOTE: _ClassVar[AuditAction]
    AUDIT_ACTION_ASSIGN: _ClassVar[AuditAction]
    AUDIT_ACTION_UNASSIGN: _ClassVar[AuditAction]

class AuditOutcome(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUDIT_OUTCOME_UNSPECIFIED: _ClassVar[AuditOutcome]
    AUDIT_OUTCOME_SUCCESS: _ClassVar[AuditOutcome]
    AUDIT_OUTCOME_REFUSED: _ClassVar[AuditOutcome]
    AUDIT_OUTCOME_FAILED: _ClassVar[AuditOutcome]

class AuditSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUDIT_SOURCE_UNSPECIFIED: _ClassVar[AuditSource]
    AUDIT_SOURCE_CONSOLE: _ClassVar[AuditSource]
    AUDIT_SOURCE_API: _ClassVar[AuditSource]
    AUDIT_SOURCE_SDK: _ClassVar[AuditSource]
    AUDIT_SOURCE_AGENT: _ClassVar[AuditSource]
    AUDIT_SOURCE_INTEGRATION_HUB: _ClassVar[AuditSource]
    AUDIT_SOURCE_TRIGGER: _ClassVar[AuditSource]
    AUDIT_SOURCE_SCHEDULE: _ClassVar[AuditSource]
    AUDIT_SOURCE_PLATFORM: _ClassVar[AuditSource]

class ExportFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXPORT_FORMAT_UNSPECIFIED: _ClassVar[ExportFormat]
    EXPORT_FORMAT_JSON_LINES: _ClassVar[ExportFormat]
    EXPORT_FORMAT_CSV: _ClassVar[ExportFormat]
ACTOR_TYPE_UNSPECIFIED: ActorType
ACTOR_TYPE_USER: ActorType
ACTOR_TYPE_AGENT: ActorType
ACTOR_TYPE_SERVICE: ActorType
ACTOR_TYPE_EDGE: ActorType
ACTOR_TYPE_SYSTEM: ActorType
AUDIT_ACTION_UNSPECIFIED: AuditAction
AUDIT_ACTION_CREATE: AuditAction
AUDIT_ACTION_UPDATE: AuditAction
AUDIT_ACTION_DELETE: AuditAction
AUDIT_ACTION_ENABLE: AuditAction
AUDIT_ACTION_DISABLE: AuditAction
AUDIT_ACTION_START: AuditAction
AUDIT_ACTION_CANCEL: AuditAction
AUDIT_ACTION_APPROVE: AuditAction
AUDIT_ACTION_REJECT: AuditAction
AUDIT_ACTION_COMMAND: AuditAction
AUDIT_ACTION_LOGIN: AuditAction
AUDIT_ACTION_LOGOUT: AuditAction
AUDIT_ACTION_EXPORT: AuditAction
AUDIT_ACTION_PROMOTE: AuditAction
AUDIT_ACTION_ASSIGN: AuditAction
AUDIT_ACTION_UNASSIGN: AuditAction
AUDIT_OUTCOME_UNSPECIFIED: AuditOutcome
AUDIT_OUTCOME_SUCCESS: AuditOutcome
AUDIT_OUTCOME_REFUSED: AuditOutcome
AUDIT_OUTCOME_FAILED: AuditOutcome
AUDIT_SOURCE_UNSPECIFIED: AuditSource
AUDIT_SOURCE_CONSOLE: AuditSource
AUDIT_SOURCE_API: AuditSource
AUDIT_SOURCE_SDK: AuditSource
AUDIT_SOURCE_AGENT: AuditSource
AUDIT_SOURCE_INTEGRATION_HUB: AuditSource
AUDIT_SOURCE_TRIGGER: AuditSource
AUDIT_SOURCE_SCHEDULE: AuditSource
AUDIT_SOURCE_PLATFORM: AuditSource
EXPORT_FORMAT_UNSPECIFIED: ExportFormat
EXPORT_FORMAT_JSON_LINES: ExportFormat
EXPORT_FORMAT_CSV: ExportFormat

class Actor(_message.Message):
    __slots__ = ("type", "id", "display_name", "on_behalf_of_user_id", "agent_session_id", "agent_message_id")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ON_BEHALF_OF_USER_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    type: ActorType
    id: str
    display_name: str
    on_behalf_of_user_id: str
    agent_session_id: str
    agent_message_id: str
    def __init__(self, type: _Optional[_Union[ActorType, str]] = ..., id: _Optional[str] = ..., display_name: _Optional[str] = ..., on_behalf_of_user_id: _Optional[str] = ..., agent_session_id: _Optional[str] = ..., agent_message_id: _Optional[str] = ...) -> None: ...

class ResourceRef(_message.Message):
    __slots__ = ("type", "id", "name", "version")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    type: str
    id: str
    name: str
    version: str
    def __init__(self, type: _Optional[str] = ..., id: _Optional[str] = ..., name: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...

class AuditEvent(_message.Message):
    __slots__ = ("id", "occurred_at", "organization_id", "actor", "action", "resource", "before", "after", "reason", "outcome", "source", "request_id", "trace_id", "client_ip", "prev_hash", "hash")
    ID_FIELD_NUMBER: _ClassVar[int]
    OCCURRED_AT_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    OUTCOME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_IP_FIELD_NUMBER: _ClassVar[int]
    PREV_HASH_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    id: str
    occurred_at: _timestamp_pb2.Timestamp
    organization_id: str
    actor: Actor
    action: AuditAction
    resource: ResourceRef
    before: _struct_pb2.Struct
    after: _struct_pb2.Struct
    reason: str
    outcome: AuditOutcome
    source: AuditSource
    request_id: str
    trace_id: str
    client_ip: str
    prev_hash: str
    hash: str
    def __init__(self, id: _Optional[str] = ..., occurred_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., organization_id: _Optional[str] = ..., actor: _Optional[_Union[Actor, _Mapping]] = ..., action: _Optional[_Union[AuditAction, str]] = ..., resource: _Optional[_Union[ResourceRef, _Mapping]] = ..., before: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., after: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., reason: _Optional[str] = ..., outcome: _Optional[_Union[AuditOutcome, str]] = ..., source: _Optional[_Union[AuditSource, str]] = ..., request_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., client_ip: _Optional[str] = ..., prev_hash: _Optional[str] = ..., hash: _Optional[str] = ...) -> None: ...

class RecordAuditEventRequest(_message.Message):
    __slots__ = ("context", "event")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    event: AuditEvent
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., event: _Optional[_Union[AuditEvent, _Mapping]] = ...) -> None: ...

class RecordAuditEventResponse(_message.Message):
    __slots__ = ("id", "hash")
    ID_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    id: str
    hash: str
    def __init__(self, id: _Optional[str] = ..., hash: _Optional[str] = ...) -> None: ...

class AuditFilter(_message.Message):
    __slots__ = ("to", "actor_types", "actor_id", "resource_type", "resource_id", "actions", "outcomes", "agent_session_id", "organization_id")
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    ACTOR_TYPES_FIELD_NUMBER: _ClassVar[int]
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    OUTCOMES_FIELD_NUMBER: _ClassVar[int]
    AGENT_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    to: _timestamp_pb2.Timestamp
    actor_types: _containers.RepeatedScalarFieldContainer[ActorType]
    actor_id: str
    resource_type: str
    resource_id: str
    actions: _containers.RepeatedScalarFieldContainer[AuditAction]
    outcomes: _containers.RepeatedScalarFieldContainer[AuditOutcome]
    agent_session_id: str
    organization_id: str
    def __init__(self, to: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., actor_types: _Optional[_Iterable[_Union[ActorType, str]]] = ..., actor_id: _Optional[str] = ..., resource_type: _Optional[str] = ..., resource_id: _Optional[str] = ..., actions: _Optional[_Iterable[_Union[AuditAction, str]]] = ..., outcomes: _Optional[_Iterable[_Union[AuditOutcome, str]]] = ..., agent_session_id: _Optional[str] = ..., organization_id: _Optional[str] = ..., **kwargs) -> None: ...

class ListAuditEventsRequest(_message.Message):
    __slots__ = ("filter", "page")
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    filter: AuditFilter
    page: _common_pb2.PageRequest
    def __init__(self, filter: _Optional[_Union[AuditFilter, _Mapping]] = ..., page: _Optional[_Union[_common_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class ListAuditEventsResponse(_message.Message):
    __slots__ = ("events", "page")
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[AuditEvent]
    page: _common_pb2.PageResponse
    def __init__(self, events: _Optional[_Iterable[_Union[AuditEvent, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class ExportAuditEventsRequest(_message.Message):
    __slots__ = ("filter", "format")
    FILTER_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    filter: AuditFilter
    format: ExportFormat
    def __init__(self, filter: _Optional[_Union[AuditFilter, _Mapping]] = ..., format: _Optional[_Union[ExportFormat, str]] = ...) -> None: ...

class ExportAuditEventsResponse(_message.Message):
    __slots__ = ("chunk",)
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    chunk: bytes
    def __init__(self, chunk: _Optional[bytes] = ...) -> None: ...

class VerifyAuditChainRequest(_message.Message):
    __slots__ = ("organization_id",)
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    organization_id: str
    def __init__(self, organization_id: _Optional[str] = ...) -> None: ...

class VerifyAuditChainResponse(_message.Message):
    __slots__ = ("intact", "verified_events", "first_mismatch_event_id")
    INTACT_FIELD_NUMBER: _ClassVar[int]
    VERIFIED_EVENTS_FIELD_NUMBER: _ClassVar[int]
    FIRST_MISMATCH_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    intact: bool
    verified_events: int
    first_mismatch_event_id: str
    def __init__(self, intact: bool = ..., verified_events: _Optional[int] = ..., first_mismatch_event_id: _Optional[str] = ...) -> None: ...
