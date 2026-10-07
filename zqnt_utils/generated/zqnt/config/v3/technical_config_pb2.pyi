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
    SCOPE_KIND_GLOBAL: _ClassVar[ScopeKind]
    SCOPE_KIND_SERVICE: _ClassVar[ScopeKind]
    SCOPE_KIND_ADAPTER: _ClassVar[ScopeKind]
    SCOPE_KIND_ASSET_TYPE: _ClassVar[ScopeKind]
    SCOPE_KIND_ORGANIZATION: _ClassVar[ScopeKind]
    SCOPE_KIND_SITE: _ClassVar[ScopeKind]
    SCOPE_KIND_ASSET: _ClassVar[ScopeKind]

class ValueType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VALUE_TYPE_UNSPECIFIED: _ClassVar[ValueType]
    VALUE_TYPE_STRING: _ClassVar[ValueType]
    VALUE_TYPE_INTEGER: _ClassVar[ValueType]
    VALUE_TYPE_LONG: _ClassVar[ValueType]
    VALUE_TYPE_BOOLEAN: _ClassVar[ValueType]
    VALUE_TYPE_DOUBLE: _ClassVar[ValueType]
    VALUE_TYPE_JSON: _ClassVar[ValueType]
    VALUE_TYPE_SECRET_REF: _ClassVar[ValueType]
SCOPE_KIND_UNSPECIFIED: ScopeKind
SCOPE_KIND_GLOBAL: ScopeKind
SCOPE_KIND_SERVICE: ScopeKind
SCOPE_KIND_ADAPTER: ScopeKind
SCOPE_KIND_ASSET_TYPE: ScopeKind
SCOPE_KIND_ORGANIZATION: ScopeKind
SCOPE_KIND_SITE: ScopeKind
SCOPE_KIND_ASSET: ScopeKind
VALUE_TYPE_UNSPECIFIED: ValueType
VALUE_TYPE_STRING: ValueType
VALUE_TYPE_INTEGER: ValueType
VALUE_TYPE_LONG: ValueType
VALUE_TYPE_BOOLEAN: ValueType
VALUE_TYPE_DOUBLE: ValueType
VALUE_TYPE_JSON: ValueType
VALUE_TYPE_SECRET_REF: ValueType

class ConfigScope(_message.Message):
    __slots__ = ("kind", "target")
    KIND_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    kind: ScopeKind
    target: str
    def __init__(self, kind: _Optional[_Union[ScopeKind, str]] = ..., target: _Optional[str] = ...) -> None: ...

class TechnicalConfig(_message.Message):
    __slots__ = ("id", "key", "value", "value_type", "scope", "active", "description", "organization_id", "created_at", "modified_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    key: str
    value: str
    value_type: ValueType
    scope: ConfigScope
    active: bool
    description: str
    organization_id: str
    created_at: _timestamp_pb2.Timestamp
    modified_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., key: _Optional[str] = ..., value: _Optional[str] = ..., value_type: _Optional[_Union[ValueType, str]] = ..., scope: _Optional[_Union[ConfigScope, _Mapping]] = ..., active: bool = ..., description: _Optional[str] = ..., organization_id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListTechnicalConfigsRequest(_message.Message):
    __slots__ = ("context", "scope", "include_inactive")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_INACTIVE_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    scope: ConfigScope
    include_inactive: bool
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., scope: _Optional[_Union[ConfigScope, _Mapping]] = ..., include_inactive: bool = ...) -> None: ...

class ListTechnicalConfigsResponse(_message.Message):
    __slots__ = ("configs",)
    CONFIGS_FIELD_NUMBER: _ClassVar[int]
    configs: _containers.RepeatedCompositeFieldContainer[TechnicalConfig]
    def __init__(self, configs: _Optional[_Iterable[_Union[TechnicalConfig, _Mapping]]] = ...) -> None: ...

class GetTechnicalConfigRequest(_message.Message):
    __slots__ = ("context", "id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...

class GetTechnicalConfigResponse(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: TechnicalConfig
    def __init__(self, config: _Optional[_Union[TechnicalConfig, _Mapping]] = ...) -> None: ...

class CreateTechnicalConfigRequest(_message.Message):
    __slots__ = ("context", "config")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    config: TechnicalConfig
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., config: _Optional[_Union[TechnicalConfig, _Mapping]] = ...) -> None: ...

class CreateTechnicalConfigResponse(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: TechnicalConfig
    def __init__(self, config: _Optional[_Union[TechnicalConfig, _Mapping]] = ...) -> None: ...

class UpdateTechnicalConfigRequest(_message.Message):
    __slots__ = ("context", "config")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    config: TechnicalConfig
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., config: _Optional[_Union[TechnicalConfig, _Mapping]] = ...) -> None: ...

class UpdateTechnicalConfigResponse(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: TechnicalConfig
    def __init__(self, config: _Optional[_Union[TechnicalConfig, _Mapping]] = ...) -> None: ...

class DeleteTechnicalConfigRequest(_message.Message):
    __slots__ = ("context", "id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...

class DeleteTechnicalConfigResponse(_message.Message):
    __slots__ = ("deleted",)
    DELETED_FIELD_NUMBER: _ClassVar[int]
    deleted: bool
    def __init__(self, deleted: bool = ...) -> None: ...
