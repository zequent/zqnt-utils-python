import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from zqnt_utils.generated.zqnt.common.v3 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScopeKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SCOPE_KIND_UNSPECIFIED: _ClassVar[ScopeKind]
    SCOPE_KIND_ORGANIZATION: _ClassVar[ScopeKind]
    SCOPE_KIND_SITE: _ClassVar[ScopeKind]
    SCOPE_KIND_CAPABILITY: _ClassVar[ScopeKind]
    SCOPE_KIND_GLOBAL: _ClassVar[ScopeKind]

class Strategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STRATEGY_UNSPECIFIED: _ClassVar[Strategy]
    STRATEGY_NEAREST: _ClassVar[Strategy]
    STRATEGY_MOST_BATTERY: _ClassVar[Strategy]

class ConditionField(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONDITION_FIELD_UNSPECIFIED: _ClassVar[ConditionField]
    CONDITION_FIELD_OBJECT_TYPE: _ClassVar[ConditionField]
    CONDITION_FIELD_CONFIDENCE: _ClassVar[ConditionField]
    CONDITION_FIELD_HAS_TARGET_POSITION: _ClassVar[ConditionField]
    CONDITION_FIELD_SITE_ID: _ClassVar[ConditionField]
    CONDITION_FIELD_CAPABILITY_ID: _ClassVar[ConditionField]
    CONDITION_FIELD_ASSET_SN: _ClassVar[ConditionField]
    CONDITION_FIELD_ORGANIZATION_ID: _ClassVar[ConditionField]

class ConditionOperator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONDITION_OPERATOR_UNSPECIFIED: _ClassVar[ConditionOperator]
    CONDITION_OPERATOR_EQUALS: _ClassVar[ConditionOperator]
    CONDITION_OPERATOR_NOT_EQUALS: _ClassVar[ConditionOperator]
    CONDITION_OPERATOR_CONTAINS: _ClassVar[ConditionOperator]
    CONDITION_OPERATOR_GREATER_THAN: _ClassVar[ConditionOperator]
    CONDITION_OPERATOR_GREATER_THAN_OR_EQUAL: _ClassVar[ConditionOperator]
    CONDITION_OPERATOR_LESS_THAN: _ClassVar[ConditionOperator]
    CONDITION_OPERATOR_LESS_THAN_OR_EQUAL: _ClassVar[ConditionOperator]
    CONDITION_OPERATOR_IS_SET: _ClassVar[ConditionOperator]
    CONDITION_OPERATOR_IS_NOT_SET: _ClassVar[ConditionOperator]

class ConstraintType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONSTRAINT_TYPE_UNSPECIFIED: _ClassVar[ConstraintType]
    CONSTRAINT_TYPE_BATTERY_MIN: _ClassVar[ConstraintType]
    CONSTRAINT_TYPE_DISTANCE_MAX: _ClassVar[ConstraintType]
    CONSTRAINT_TYPE_ASSET_TYPE: _ClassVar[ConstraintType]
    CONSTRAINT_TYPE_IN_SITE: _ClassVar[ConstraintType]
    CONSTRAINT_TYPE_AVAILABLE: _ClassVar[ConstraintType]

class SelectionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SELECTION_STATUS_UNSPECIFIED: _ClassVar[SelectionStatus]
    SELECTION_STATUS_SELECTED: _ClassVar[SelectionStatus]
    SELECTION_STATUS_BUSY: _ClassVar[SelectionStatus]
    SELECTION_STATUS_NO_RULE: _ClassVar[SelectionStatus]
    SELECTION_STATUS_NO_ASSET: _ClassVar[SelectionStatus]

class StepOutcome(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STEP_OUTCOME_UNSPECIFIED: _ClassVar[StepOutcome]
    STEP_OUTCOME_NOT_APPLICABLE: _ClassVar[StepOutcome]
    STEP_OUTCOME_NO_CANDIDATE: _ClassVar[StepOutcome]
    STEP_OUTCOME_NO_CHOICE: _ClassVar[StepOutcome]
    STEP_OUTCOME_CHOSE: _ClassVar[StepOutcome]
    STEP_OUTCOME_NOT_REACHED: _ClassVar[StepOutcome]
SCOPE_KIND_UNSPECIFIED: ScopeKind
SCOPE_KIND_ORGANIZATION: ScopeKind
SCOPE_KIND_SITE: ScopeKind
SCOPE_KIND_CAPABILITY: ScopeKind
SCOPE_KIND_GLOBAL: ScopeKind
STRATEGY_UNSPECIFIED: Strategy
STRATEGY_NEAREST: Strategy
STRATEGY_MOST_BATTERY: Strategy
CONDITION_FIELD_UNSPECIFIED: ConditionField
CONDITION_FIELD_OBJECT_TYPE: ConditionField
CONDITION_FIELD_CONFIDENCE: ConditionField
CONDITION_FIELD_HAS_TARGET_POSITION: ConditionField
CONDITION_FIELD_SITE_ID: ConditionField
CONDITION_FIELD_CAPABILITY_ID: ConditionField
CONDITION_FIELD_ASSET_SN: ConditionField
CONDITION_FIELD_ORGANIZATION_ID: ConditionField
CONDITION_OPERATOR_UNSPECIFIED: ConditionOperator
CONDITION_OPERATOR_EQUALS: ConditionOperator
CONDITION_OPERATOR_NOT_EQUALS: ConditionOperator
CONDITION_OPERATOR_CONTAINS: ConditionOperator
CONDITION_OPERATOR_GREATER_THAN: ConditionOperator
CONDITION_OPERATOR_GREATER_THAN_OR_EQUAL: ConditionOperator
CONDITION_OPERATOR_LESS_THAN: ConditionOperator
CONDITION_OPERATOR_LESS_THAN_OR_EQUAL: ConditionOperator
CONDITION_OPERATOR_IS_SET: ConditionOperator
CONDITION_OPERATOR_IS_NOT_SET: ConditionOperator
CONSTRAINT_TYPE_UNSPECIFIED: ConstraintType
CONSTRAINT_TYPE_BATTERY_MIN: ConstraintType
CONSTRAINT_TYPE_DISTANCE_MAX: ConstraintType
CONSTRAINT_TYPE_ASSET_TYPE: ConstraintType
CONSTRAINT_TYPE_IN_SITE: ConstraintType
CONSTRAINT_TYPE_AVAILABLE: ConstraintType
SELECTION_STATUS_UNSPECIFIED: SelectionStatus
SELECTION_STATUS_SELECTED: SelectionStatus
SELECTION_STATUS_BUSY: SelectionStatus
SELECTION_STATUS_NO_RULE: SelectionStatus
SELECTION_STATUS_NO_ASSET: SelectionStatus
STEP_OUTCOME_UNSPECIFIED: StepOutcome
STEP_OUTCOME_NOT_APPLICABLE: StepOutcome
STEP_OUTCOME_NO_CANDIDATE: StepOutcome
STEP_OUTCOME_NO_CHOICE: StepOutcome
STEP_OUTCOME_CHOSE: StepOutcome
STEP_OUTCOME_NOT_REACHED: StepOutcome

class RuleScope(_message.Message):
    __slots__ = ("kind", "target")
    KIND_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    kind: ScopeKind
    target: str
    def __init__(self, kind: _Optional[_Union[ScopeKind, str]] = ..., target: _Optional[str] = ...) -> None: ...

class Condition(_message.Message):
    __slots__ = ("field", "operator", "value")
    FIELD_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    field: ConditionField
    operator: ConditionOperator
    value: str
    def __init__(self, field: _Optional[_Union[ConditionField, str]] = ..., operator: _Optional[_Union[ConditionOperator, str]] = ..., value: _Optional[str] = ...) -> None: ...

class Constraint(_message.Message):
    __slots__ = ("type", "min", "max", "required_value")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_VALUE_FIELD_NUMBER: _ClassVar[int]
    type: ConstraintType
    min: float
    max: float
    required_value: str
    def __init__(self, type: _Optional[_Union[ConstraintType, str]] = ..., min: _Optional[float] = ..., max: _Optional[float] = ..., required_value: _Optional[str] = ...) -> None: ...

class DispatchRule(_message.Message):
    __slots__ = ("id", "organization_id", "name", "description", "priority", "active", "scope", "strategy", "conditions", "constraints", "created_at", "modified_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    STRATEGY_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    organization_id: str
    name: str
    description: str
    priority: int
    active: bool
    scope: RuleScope
    strategy: Strategy
    conditions: _containers.RepeatedCompositeFieldContainer[Condition]
    constraints: _containers.RepeatedCompositeFieldContainer[Constraint]
    created_at: _timestamp_pb2.Timestamp
    modified_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., organization_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., priority: _Optional[int] = ..., active: bool = ..., scope: _Optional[_Union[RuleScope, _Mapping]] = ..., strategy: _Optional[_Union[Strategy, str]] = ..., conditions: _Optional[_Iterable[_Union[Condition, _Mapping]]] = ..., constraints: _Optional[_Iterable[_Union[Constraint, _Mapping]]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListDispatchRulesRequest(_message.Message):
    __slots__ = ("context", "organization_id", "include_inactive")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_INACTIVE_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    organization_id: str
    include_inactive: bool
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., organization_id: _Optional[str] = ..., include_inactive: bool = ...) -> None: ...

class ListDispatchRulesResponse(_message.Message):
    __slots__ = ("rules",)
    RULES_FIELD_NUMBER: _ClassVar[int]
    rules: _containers.RepeatedCompositeFieldContainer[DispatchRule]
    def __init__(self, rules: _Optional[_Iterable[_Union[DispatchRule, _Mapping]]] = ...) -> None: ...

class GetDispatchRuleRequest(_message.Message):
    __slots__ = ("context", "id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...

class GetDispatchRuleResponse(_message.Message):
    __slots__ = ("rule",)
    RULE_FIELD_NUMBER: _ClassVar[int]
    rule: DispatchRule
    def __init__(self, rule: _Optional[_Union[DispatchRule, _Mapping]] = ...) -> None: ...

class CreateDispatchRuleRequest(_message.Message):
    __slots__ = ("context", "rule")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    RULE_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    rule: DispatchRule
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., rule: _Optional[_Union[DispatchRule, _Mapping]] = ...) -> None: ...

class CreateDispatchRuleResponse(_message.Message):
    __slots__ = ("rule",)
    RULE_FIELD_NUMBER: _ClassVar[int]
    rule: DispatchRule
    def __init__(self, rule: _Optional[_Union[DispatchRule, _Mapping]] = ...) -> None: ...

class UpdateDispatchRuleRequest(_message.Message):
    __slots__ = ("context", "rule")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    RULE_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    rule: DispatchRule
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., rule: _Optional[_Union[DispatchRule, _Mapping]] = ...) -> None: ...

class UpdateDispatchRuleResponse(_message.Message):
    __slots__ = ("rule",)
    RULE_FIELD_NUMBER: _ClassVar[int]
    rule: DispatchRule
    def __init__(self, rule: _Optional[_Union[DispatchRule, _Mapping]] = ...) -> None: ...

class DeleteDispatchRuleRequest(_message.Message):
    __slots__ = ("context", "id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...

class DeleteDispatchRuleResponse(_message.Message):
    __slots__ = ("deleted",)
    DELETED_FIELD_NUMBER: _ClassVar[int]
    deleted: bool
    def __init__(self, deleted: bool = ...) -> None: ...

class SimulateAssetSelectionRequest(_message.Message):
    __slots__ = ("context", "organization_id", "object_type", "confidence", "target", "site_id", "capability_id", "priority")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    CAPABILITY_ID_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    organization_id: str
    object_type: str
    confidence: float
    target: _common_pb2.GeoPoint
    site_id: str
    capability_id: str
    priority: int
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., organization_id: _Optional[str] = ..., object_type: _Optional[str] = ..., confidence: _Optional[float] = ..., target: _Optional[_Union[_common_pb2.GeoPoint, _Mapping]] = ..., site_id: _Optional[str] = ..., capability_id: _Optional[str] = ..., priority: _Optional[int] = ...) -> None: ...

class SelectionStep(_message.Message):
    __slots__ = ("rule_id", "priority", "strategy", "outcome", "note", "rejections", "level")
    class RejectionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    STRATEGY_FIELD_NUMBER: _ClassVar[int]
    OUTCOME_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    REJECTIONS_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    rule_id: str
    priority: int
    strategy: Strategy
    outcome: StepOutcome
    note: str
    rejections: _containers.ScalarMap[str, str]
    level: str
    def __init__(self, rule_id: _Optional[str] = ..., priority: _Optional[int] = ..., strategy: _Optional[_Union[Strategy, str]] = ..., outcome: _Optional[_Union[StepOutcome, str]] = ..., note: _Optional[str] = ..., rejections: _Optional[_Mapping[str, str]] = ..., level: _Optional[str] = ...) -> None: ...

class SelectionCandidate(_message.Message):
    __slots__ = ("asset", "asset_type", "battery_percent", "available", "held_by_priority", "distance_meters", "site_id", "reason")
    ASSET_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    BATTERY_PERCENT_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    HELD_BY_PRIORITY_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_METERS_FIELD_NUMBER: _ClassVar[int]
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    asset: _common_pb2.AssetRef
    asset_type: str
    battery_percent: int
    available: bool
    held_by_priority: int
    distance_meters: float
    site_id: str
    reason: str
    def __init__(self, asset: _Optional[_Union[_common_pb2.AssetRef, _Mapping]] = ..., asset_type: _Optional[str] = ..., battery_percent: _Optional[int] = ..., available: bool = ..., held_by_priority: _Optional[int] = ..., distance_meters: _Optional[float] = ..., site_id: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class SimulateAssetSelectionResponse(_message.Message):
    __slots__ = ("status", "selected_asset", "answered_by_rule_id", "summary", "steps", "candidates", "site_id")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SELECTED_ASSET_FIELD_NUMBER: _ClassVar[int]
    ANSWERED_BY_RULE_ID_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    STEPS_FIELD_NUMBER: _ClassVar[int]
    CANDIDATES_FIELD_NUMBER: _ClassVar[int]
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    status: SelectionStatus
    selected_asset: _common_pb2.AssetRef
    answered_by_rule_id: str
    summary: str
    steps: _containers.RepeatedCompositeFieldContainer[SelectionStep]
    candidates: _containers.RepeatedCompositeFieldContainer[SelectionCandidate]
    site_id: str
    def __init__(self, status: _Optional[_Union[SelectionStatus, str]] = ..., selected_asset: _Optional[_Union[_common_pb2.AssetRef, _Mapping]] = ..., answered_by_rule_id: _Optional[str] = ..., summary: _Optional[str] = ..., steps: _Optional[_Iterable[_Union[SelectionStep, _Mapping]]] = ..., candidates: _Optional[_Iterable[_Union[SelectionCandidate, _Mapping]]] = ..., site_id: _Optional[str] = ...) -> None: ...
