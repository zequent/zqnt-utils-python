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

class SignIn(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SIGN_IN_UNSPECIFIED: _ClassVar[SignIn]
    SIGN_IN_PASSWORD: _ClassVar[SignIn]
    SIGN_IN_SSO: _ClassVar[SignIn]
SIGN_IN_UNSPECIFIED: SignIn
SIGN_IN_PASSWORD: SignIn
SIGN_IN_SSO: SignIn

class User(_message.Message):
    __slots__ = ("id", "email", "organization_id", "roles", "enabled", "sign_in", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    SIGN_IN_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    email: str
    organization_id: str
    roles: _containers.RepeatedScalarFieldContainer[str]
    enabled: bool
    sign_in: SignIn
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., email: _Optional[str] = ..., organization_id: _Optional[str] = ..., roles: _Optional[_Iterable[str]] = ..., enabled: bool = ..., sign_in: _Optional[_Union[SignIn, str]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class IdentityProvider(_message.Message):
    __slots__ = ("organization_id", "issuer_url", "client_id", "client_secret", "email_domains", "role_claim_name", "claim_role_mapping", "enabled", "created_at", "modified_at")
    class ClaimRoleMappingEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    ISSUER_URL_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    EMAIL_DOMAINS_FIELD_NUMBER: _ClassVar[int]
    ROLE_CLAIM_NAME_FIELD_NUMBER: _ClassVar[int]
    CLAIM_ROLE_MAPPING_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    organization_id: str
    issuer_url: str
    client_id: str
    client_secret: str
    email_domains: _containers.RepeatedScalarFieldContainer[str]
    role_claim_name: str
    claim_role_mapping: _containers.ScalarMap[str, str]
    enabled: bool
    created_at: _timestamp_pb2.Timestamp
    modified_at: _timestamp_pb2.Timestamp
    def __init__(self, organization_id: _Optional[str] = ..., issuer_url: _Optional[str] = ..., client_id: _Optional[str] = ..., client_secret: _Optional[str] = ..., email_domains: _Optional[_Iterable[str]] = ..., role_claim_name: _Optional[str] = ..., claim_role_mapping: _Optional[_Mapping[str, str]] = ..., enabled: bool = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListUsersRequest(_message.Message):
    __slots__ = ("context",)
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ...) -> None: ...

class ListUsersResponse(_message.Message):
    __slots__ = ("users",)
    USERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[User]
    def __init__(self, users: _Optional[_Iterable[_Union[User, _Mapping]]] = ...) -> None: ...

class GetUserRequest(_message.Message):
    __slots__ = ("context", "id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...

class GetUserResponse(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: User
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class UpdateUserRolesRequest(_message.Message):
    __slots__ = ("context", "id", "roles")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    id: str
    roles: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., id: _Optional[str] = ..., roles: _Optional[_Iterable[str]] = ...) -> None: ...

class UpdateUserRolesResponse(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: User
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class SetUserEnabledRequest(_message.Message):
    __slots__ = ("context", "id", "enabled")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    id: str
    enabled: bool
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., id: _Optional[str] = ..., enabled: bool = ...) -> None: ...

class SetUserEnabledResponse(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: User
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class DeleteUserRequest(_message.Message):
    __slots__ = ("context", "id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...

class DeleteUserResponse(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: User
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class GetIdentityProviderRequest(_message.Message):
    __slots__ = ("context", "organization_id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    organization_id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., organization_id: _Optional[str] = ...) -> None: ...

class GetIdentityProviderResponse(_message.Message):
    __slots__ = ("identity_provider",)
    IDENTITY_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    identity_provider: IdentityProvider
    def __init__(self, identity_provider: _Optional[_Union[IdentityProvider, _Mapping]] = ...) -> None: ...

class SetIdentityProviderRequest(_message.Message):
    __slots__ = ("context", "identity_provider")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    identity_provider: IdentityProvider
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., identity_provider: _Optional[_Union[IdentityProvider, _Mapping]] = ...) -> None: ...

class SetIdentityProviderResponse(_message.Message):
    __slots__ = ("identity_provider",)
    IDENTITY_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    identity_provider: IdentityProvider
    def __init__(self, identity_provider: _Optional[_Union[IdentityProvider, _Mapping]] = ...) -> None: ...

class FindIdentityProviderForEmailRequest(_message.Message):
    __slots__ = ("context", "email")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    email: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., email: _Optional[str] = ...) -> None: ...

class FindIdentityProviderForEmailResponse(_message.Message):
    __slots__ = ("identity_provider",)
    IDENTITY_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    identity_provider: IdentityProvider
    def __init__(self, identity_provider: _Optional[_Union[IdentityProvider, _Mapping]] = ...) -> None: ...
