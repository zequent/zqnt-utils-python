from zqnt_utils.generated.zqnt.common.v3 import common_pb2 as _common_pb2
from zqnt_utils.generated.zqnt.iam.v3 import user_pb2 as _user_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SignInEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SIGN_IN_EVENT_TYPE_UNSPECIFIED: _ClassVar[SignInEventType]
    SIGN_IN_EVENT_TYPE_LOGIN_SUCCESS: _ClassVar[SignInEventType]
    SIGN_IN_EVENT_TYPE_LOGIN_FAILURE: _ClassVar[SignInEventType]
    SIGN_IN_EVENT_TYPE_LOGOUT: _ClassVar[SignInEventType]
    SIGN_IN_EVENT_TYPE_PASSWORD_RESET: _ClassVar[SignInEventType]
    SIGN_IN_EVENT_TYPE_SESSIONS_REVOKED: _ClassVar[SignInEventType]
SIGN_IN_EVENT_TYPE_UNSPECIFIED: SignInEventType
SIGN_IN_EVENT_TYPE_LOGIN_SUCCESS: SignInEventType
SIGN_IN_EVENT_TYPE_LOGIN_FAILURE: SignInEventType
SIGN_IN_EVENT_TYPE_LOGOUT: SignInEventType
SIGN_IN_EVENT_TYPE_PASSWORD_RESET: SignInEventType
SIGN_IN_EVENT_TYPE_SESSIONS_REVOKED: SignInEventType

class VerifyPasswordRequest(_message.Message):
    __slots__ = ("context", "email", "password")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    email: str
    password: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., email: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class VerifyPasswordResponse(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ...) -> None: ...

class CreateUserRequest(_message.Message):
    __slots__ = ("context", "user_id", "organization_id", "email", "password", "roles")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    user_id: str
    organization_id: str
    email: str
    password: str
    roles: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., user_id: _Optional[str] = ..., organization_id: _Optional[str] = ..., email: _Optional[str] = ..., password: _Optional[str] = ..., roles: _Optional[_Iterable[str]] = ...) -> None: ...

class CreateUserResponse(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ...) -> None: ...

class ResetPasswordRequest(_message.Message):
    __slots__ = ("context", "user_id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    user_id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., user_id: _Optional[str] = ...) -> None: ...

class ResetPasswordResponse(_message.Message):
    __slots__ = ("new_password",)
    NEW_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    new_password: str
    def __init__(self, new_password: _Optional[str] = ...) -> None: ...

class FindSsoUserRequest(_message.Message):
    __slots__ = ("context", "organization_id", "external_subject")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_SUBJECT_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    organization_id: str
    external_subject: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., organization_id: _Optional[str] = ..., external_subject: _Optional[str] = ...) -> None: ...

class FindSsoUserResponse(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ...) -> None: ...

class UpsertSsoUserRequest(_message.Message):
    __slots__ = ("context", "organization_id", "external_subject", "email", "roles", "user_id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_SUBJECT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    organization_id: str
    external_subject: str
    email: str
    roles: _containers.RepeatedScalarFieldContainer[str]
    user_id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., organization_id: _Optional[str] = ..., external_subject: _Optional[str] = ..., email: _Optional[str] = ..., roles: _Optional[_Iterable[str]] = ..., user_id: _Optional[str] = ...) -> None: ...

class UpsertSsoUserResponse(_message.Message):
    __slots__ = ("user", "created")
    USER_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    created: bool
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., created: bool = ...) -> None: ...

class RecordSignInEventRequest(_message.Message):
    __slots__ = ("context", "type", "user_id", "organization_id", "email", "source_ip", "detail")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    SOURCE_IP_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    type: SignInEventType
    user_id: str
    organization_id: str
    email: str
    source_ip: str
    detail: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., type: _Optional[_Union[SignInEventType, str]] = ..., user_id: _Optional[str] = ..., organization_id: _Optional[str] = ..., email: _Optional[str] = ..., source_ip: _Optional[str] = ..., detail: _Optional[str] = ...) -> None: ...

class RecordSignInEventResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
