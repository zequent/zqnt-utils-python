import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from zqnt_utils.generated.zqnt.common.v3 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LicenseActivation(_message.Message):
    __slots__ = ("organization_id", "activation_id", "sealed_token", "sealing_scheme", "created_at", "modified_at")
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVATION_ID_FIELD_NUMBER: _ClassVar[int]
    SEALED_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SEALING_SCHEME_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    organization_id: str
    activation_id: str
    sealed_token: bytes
    sealing_scheme: str
    created_at: _timestamp_pb2.Timestamp
    modified_at: _timestamp_pb2.Timestamp
    def __init__(self, organization_id: _Optional[str] = ..., activation_id: _Optional[str] = ..., sealed_token: _Optional[bytes] = ..., sealing_scheme: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListLicenseActivationsRequest(_message.Message):
    __slots__ = ("context",)
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ...) -> None: ...

class ListLicenseActivationsResponse(_message.Message):
    __slots__ = ("activations",)
    ACTIVATIONS_FIELD_NUMBER: _ClassVar[int]
    activations: _containers.RepeatedCompositeFieldContainer[LicenseActivation]
    def __init__(self, activations: _Optional[_Iterable[_Union[LicenseActivation, _Mapping]]] = ...) -> None: ...

class GetLicenseActivationRequest(_message.Message):
    __slots__ = ("context", "organization_id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    organization_id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., organization_id: _Optional[str] = ...) -> None: ...

class GetLicenseActivationResponse(_message.Message):
    __slots__ = ("activation",)
    ACTIVATION_FIELD_NUMBER: _ClassVar[int]
    activation: LicenseActivation
    def __init__(self, activation: _Optional[_Union[LicenseActivation, _Mapping]] = ...) -> None: ...

class PutLicenseActivationRequest(_message.Message):
    __slots__ = ("context", "activation")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ACTIVATION_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    activation: LicenseActivation
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., activation: _Optional[_Union[LicenseActivation, _Mapping]] = ...) -> None: ...

class PutLicenseActivationResponse(_message.Message):
    __slots__ = ("activation",)
    ACTIVATION_FIELD_NUMBER: _ClassVar[int]
    activation: LicenseActivation
    def __init__(self, activation: _Optional[_Union[LicenseActivation, _Mapping]] = ...) -> None: ...

class DeleteLicenseActivationRequest(_message.Message):
    __slots__ = ("context", "organization_id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    organization_id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., organization_id: _Optional[str] = ...) -> None: ...

class DeleteLicenseActivationResponse(_message.Message):
    __slots__ = ("deleted",)
    DELETED_FIELD_NUMBER: _ClassVar[int]
    deleted: bool
    def __init__(self, deleted: bool = ...) -> None: ...
