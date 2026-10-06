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

class FiringOutcome(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FIRING_OUTCOME_UNSPECIFIED: _ClassVar[FiringOutcome]
    FIRING_OUTCOME_STARTED: _ClassVar[FiringOutcome]
    FIRING_OUTCOME_SKIPPED: _ClassVar[FiringOutcome]
    FIRING_OUTCOME_FAILED: _ClassVar[FiringOutcome]

class TriggerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRIGGER_TYPE_UNSPECIFIED: _ClassVar[TriggerType]
    TRIGGER_TYPE_DETECTION: _ClassVar[TriggerType]
    TRIGGER_TYPE_TELEMETRY_THRESHOLD: _ClassVar[TriggerType]
    TRIGGER_TYPE_ASSET_STATUS: _ClassVar[TriggerType]
    TRIGGER_TYPE_WEBHOOK: _ClassVar[TriggerType]
    TRIGGER_TYPE_INTEGRATION: _ClassVar[TriggerType]

class Comparison(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMPARISON_UNSPECIFIED: _ClassVar[Comparison]
    COMPARISON_LESS_THAN: _ClassVar[Comparison]
    COMPARISON_GREATER_THAN: _ClassVar[Comparison]
    COMPARISON_EQUALS: _ClassVar[Comparison]
    COMPARISON_NOT_EQUALS: _ClassVar[Comparison]

class DispatchTarget(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DISPATCH_TARGET_UNSPECIFIED: _ClassVar[DispatchTarget]
    DISPATCH_TARGET_POLICY_SELECTED: _ClassVar[DispatchTarget]
FIRING_OUTCOME_UNSPECIFIED: FiringOutcome
FIRING_OUTCOME_STARTED: FiringOutcome
FIRING_OUTCOME_SKIPPED: FiringOutcome
FIRING_OUTCOME_FAILED: FiringOutcome
TRIGGER_TYPE_UNSPECIFIED: TriggerType
TRIGGER_TYPE_DETECTION: TriggerType
TRIGGER_TYPE_TELEMETRY_THRESHOLD: TriggerType
TRIGGER_TYPE_ASSET_STATUS: TriggerType
TRIGGER_TYPE_WEBHOOK: TriggerType
TRIGGER_TYPE_INTEGRATION: TriggerType
COMPARISON_UNSPECIFIED: Comparison
COMPARISON_LESS_THAN: Comparison
COMPARISON_GREATER_THAN: Comparison
COMPARISON_EQUALS: Comparison
COMPARISON_NOT_EQUALS: Comparison
DISPATCH_TARGET_UNSPECIFIED: DispatchTarget
DISPATCH_TARGET_POLICY_SELECTED: DispatchTarget

class RunTarget(_message.Message):
    __slots__ = ("skill", "command_id")
    SKILL_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    skill: SkillTarget
    command_id: str
    def __init__(self, skill: _Optional[_Union[SkillTarget, _Mapping]] = ..., command_id: _Optional[str] = ...) -> None: ...

class SkillTarget(_message.Message):
    __slots__ = ("application_id", "skill_id")
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    application_id: str
    skill_id: str
    def __init__(self, application_id: _Optional[str] = ..., skill_id: _Optional[str] = ...) -> None: ...

class Schedule(_message.Message):
    __slots__ = ("id", "organization_id", "name", "cron_expression", "time_zone", "active", "target", "asset_sn", "inputs", "auto_start", "last_fired_at", "last_firing_outcome", "last_firing_reason", "last_execution_id", "created_at", "modified_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CRON_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    AUTO_START_FIELD_NUMBER: _ClassVar[int]
    LAST_FIRED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_FIRING_OUTCOME_FIELD_NUMBER: _ClassVar[int]
    LAST_FIRING_REASON_FIELD_NUMBER: _ClassVar[int]
    LAST_EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    organization_id: str
    name: str
    cron_expression: str
    time_zone: str
    active: bool
    target: RunTarget
    asset_sn: str
    inputs: _struct_pb2.Struct
    auto_start: bool
    last_fired_at: _timestamp_pb2.Timestamp
    last_firing_outcome: FiringOutcome
    last_firing_reason: str
    last_execution_id: str
    created_at: _timestamp_pb2.Timestamp
    modified_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., organization_id: _Optional[str] = ..., name: _Optional[str] = ..., cron_expression: _Optional[str] = ..., time_zone: _Optional[str] = ..., active: bool = ..., target: _Optional[_Union[RunTarget, _Mapping]] = ..., asset_sn: _Optional[str] = ..., inputs: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., auto_start: bool = ..., last_fired_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_firing_outcome: _Optional[_Union[FiringOutcome, str]] = ..., last_firing_reason: _Optional[str] = ..., last_execution_id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Trigger(_message.Message):
    __slots__ = ("id", "organization_id", "name", "active", "type", "asset_sn", "object_type", "min_confidence", "telemetry_field", "comparison", "comparison_value", "webhook_token", "bridge_id", "target", "inputs", "auto_start", "cooldown_seconds", "dispatch_target", "priority", "site_id", "attention_reason", "last_fired_at", "created_at", "modified_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    MIN_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    TELEMETRY_FIELD_FIELD_NUMBER: _ClassVar[int]
    COMPARISON_FIELD_NUMBER: _ClassVar[int]
    COMPARISON_VALUE_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_TOKEN_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    AUTO_START_FIELD_NUMBER: _ClassVar[int]
    COOLDOWN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    DISPATCH_TARGET_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTENTION_REASON_FIELD_NUMBER: _ClassVar[int]
    LAST_FIRED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    organization_id: str
    name: str
    active: bool
    type: TriggerType
    asset_sn: str
    object_type: str
    min_confidence: float
    telemetry_field: str
    comparison: Comparison
    comparison_value: str
    webhook_token: str
    bridge_id: str
    target: RunTarget
    inputs: _struct_pb2.Struct
    auto_start: bool
    cooldown_seconds: int
    dispatch_target: DispatchTarget
    priority: int
    site_id: str
    attention_reason: str
    last_fired_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    modified_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., organization_id: _Optional[str] = ..., name: _Optional[str] = ..., active: bool = ..., type: _Optional[_Union[TriggerType, str]] = ..., asset_sn: _Optional[str] = ..., object_type: _Optional[str] = ..., min_confidence: _Optional[float] = ..., telemetry_field: _Optional[str] = ..., comparison: _Optional[_Union[Comparison, str]] = ..., comparison_value: _Optional[str] = ..., webhook_token: _Optional[str] = ..., bridge_id: _Optional[str] = ..., target: _Optional[_Union[RunTarget, _Mapping]] = ..., inputs: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., auto_start: bool = ..., cooldown_seconds: _Optional[int] = ..., dispatch_target: _Optional[_Union[DispatchTarget, str]] = ..., priority: _Optional[int] = ..., site_id: _Optional[str] = ..., attention_reason: _Optional[str] = ..., last_fired_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListSchedulesRequest(_message.Message):
    __slots__ = ("context", "organization_id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    organization_id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., organization_id: _Optional[str] = ...) -> None: ...

class ListSchedulesResponse(_message.Message):
    __slots__ = ("schedules",)
    SCHEDULES_FIELD_NUMBER: _ClassVar[int]
    schedules: _containers.RepeatedCompositeFieldContainer[Schedule]
    def __init__(self, schedules: _Optional[_Iterable[_Union[Schedule, _Mapping]]] = ...) -> None: ...

class GetScheduleRequest(_message.Message):
    __slots__ = ("context", "id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...

class GetScheduleResponse(_message.Message):
    __slots__ = ("schedule",)
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    schedule: Schedule
    def __init__(self, schedule: _Optional[_Union[Schedule, _Mapping]] = ...) -> None: ...

class CreateScheduleRequest(_message.Message):
    __slots__ = ("context", "schedule")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    schedule: Schedule
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., schedule: _Optional[_Union[Schedule, _Mapping]] = ...) -> None: ...

class CreateScheduleResponse(_message.Message):
    __slots__ = ("schedule",)
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    schedule: Schedule
    def __init__(self, schedule: _Optional[_Union[Schedule, _Mapping]] = ...) -> None: ...

class UpdateScheduleRequest(_message.Message):
    __slots__ = ("context", "schedule")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    schedule: Schedule
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., schedule: _Optional[_Union[Schedule, _Mapping]] = ...) -> None: ...

class UpdateScheduleResponse(_message.Message):
    __slots__ = ("schedule",)
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    schedule: Schedule
    def __init__(self, schedule: _Optional[_Union[Schedule, _Mapping]] = ...) -> None: ...

class DeleteScheduleRequest(_message.Message):
    __slots__ = ("context", "id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...

class DeleteScheduleResponse(_message.Message):
    __slots__ = ("deleted",)
    DELETED_FIELD_NUMBER: _ClassVar[int]
    deleted: bool
    def __init__(self, deleted: bool = ...) -> None: ...

class RecordScheduleFiringRequest(_message.Message):
    __slots__ = ("context", "schedule_id", "fired_at", "outcome", "reason", "execution_id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_ID_FIELD_NUMBER: _ClassVar[int]
    FIRED_AT_FIELD_NUMBER: _ClassVar[int]
    OUTCOME_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    schedule_id: str
    fired_at: _timestamp_pb2.Timestamp
    outcome: FiringOutcome
    reason: str
    execution_id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., schedule_id: _Optional[str] = ..., fired_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., outcome: _Optional[_Union[FiringOutcome, str]] = ..., reason: _Optional[str] = ..., execution_id: _Optional[str] = ...) -> None: ...

class RecordScheduleFiringResponse(_message.Message):
    __slots__ = ("schedule",)
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    schedule: Schedule
    def __init__(self, schedule: _Optional[_Union[Schedule, _Mapping]] = ...) -> None: ...

class ListTriggersRequest(_message.Message):
    __slots__ = ("context", "organization_id", "active_only")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_ONLY_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    organization_id: str
    active_only: bool
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., organization_id: _Optional[str] = ..., active_only: bool = ...) -> None: ...

class ListTriggersResponse(_message.Message):
    __slots__ = ("triggers",)
    TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    triggers: _containers.RepeatedCompositeFieldContainer[Trigger]
    def __init__(self, triggers: _Optional[_Iterable[_Union[Trigger, _Mapping]]] = ...) -> None: ...

class GetTriggerRequest(_message.Message):
    __slots__ = ("context", "id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...

class GetTriggerResponse(_message.Message):
    __slots__ = ("trigger",)
    TRIGGER_FIELD_NUMBER: _ClassVar[int]
    trigger: Trigger
    def __init__(self, trigger: _Optional[_Union[Trigger, _Mapping]] = ...) -> None: ...

class CreateTriggerRequest(_message.Message):
    __slots__ = ("context", "trigger")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    trigger: Trigger
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., trigger: _Optional[_Union[Trigger, _Mapping]] = ...) -> None: ...

class CreateTriggerResponse(_message.Message):
    __slots__ = ("trigger",)
    TRIGGER_FIELD_NUMBER: _ClassVar[int]
    trigger: Trigger
    def __init__(self, trigger: _Optional[_Union[Trigger, _Mapping]] = ...) -> None: ...

class UpdateTriggerRequest(_message.Message):
    __slots__ = ("context", "trigger")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    trigger: Trigger
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., trigger: _Optional[_Union[Trigger, _Mapping]] = ...) -> None: ...

class UpdateTriggerResponse(_message.Message):
    __slots__ = ("trigger",)
    TRIGGER_FIELD_NUMBER: _ClassVar[int]
    trigger: Trigger
    def __init__(self, trigger: _Optional[_Union[Trigger, _Mapping]] = ...) -> None: ...

class DeleteTriggerRequest(_message.Message):
    __slots__ = ("context", "id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...

class DeleteTriggerResponse(_message.Message):
    __slots__ = ("deleted",)
    DELETED_FIELD_NUMBER: _ClassVar[int]
    deleted: bool
    def __init__(self, deleted: bool = ...) -> None: ...

class RecordTriggerFiredRequest(_message.Message):
    __slots__ = ("context", "id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...

class RecordTriggerFiredResponse(_message.Message):
    __slots__ = ("trigger",)
    TRIGGER_FIELD_NUMBER: _ClassVar[int]
    trigger: Trigger
    def __init__(self, trigger: _Optional[_Union[Trigger, _Mapping]] = ...) -> None: ...

class RegenerateWebhookTokenRequest(_message.Message):
    __slots__ = ("context", "id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...

class RegenerateWebhookTokenResponse(_message.Message):
    __slots__ = ("trigger",)
    TRIGGER_FIELD_NUMBER: _ClassVar[int]
    trigger: Trigger
    def __init__(self, trigger: _Optional[_Union[Trigger, _Mapping]] = ...) -> None: ...

class GetTriggerByWebhookTokenRequest(_message.Message):
    __slots__ = ("context", "token")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    token: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., token: _Optional[str] = ...) -> None: ...

class GetTriggerByWebhookTokenResponse(_message.Message):
    __slots__ = ("trigger",)
    TRIGGER_FIELD_NUMBER: _ClassVar[int]
    trigger: Trigger
    def __init__(self, trigger: _Optional[_Union[Trigger, _Mapping]] = ...) -> None: ...
