import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from zqnt_utils.generated.zqnt.capability.v3 import capability_pb2 as _capability_pb2
from zqnt_utils.generated.zqnt.common.v3 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Permission(_message.Message):
    __slots__ = ("id", "resource", "action", "description", "risk")
    ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    RISK_FIELD_NUMBER: _ClassVar[int]
    id: str
    resource: str
    action: str
    description: str
    risk: _capability_pb2.CommandRisk
    def __init__(self, id: _Optional[str] = ..., resource: _Optional[str] = ..., action: _Optional[str] = ..., description: _Optional[str] = ..., risk: _Optional[_Union[_capability_pb2.CommandRisk, str]] = ...) -> None: ...

class Role(_message.Message):
    __slots__ = ("id", "organization_id", "name", "description", "built_in", "permission_ids", "created_at", "updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    BUILT_IN_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_IDS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    organization_id: str
    name: str
    description: str
    built_in: bool
    permission_ids: _containers.RepeatedScalarFieldContainer[str]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., organization_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., built_in: bool = ..., permission_ids: _Optional[_Iterable[str]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class RoleAssignment(_message.Message):
    __slots__ = ("id", "user_id", "role_id", "site_ids", "created_at", "created_by")
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    SITE_IDS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    id: str
    user_id: str
    role_id: str
    site_ids: _containers.RepeatedScalarFieldContainer[str]
    created_at: _timestamp_pb2.Timestamp
    created_by: str
    def __init__(self, id: _Optional[str] = ..., user_id: _Optional[str] = ..., role_id: _Optional[str] = ..., site_ids: _Optional[_Iterable[str]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[str] = ...) -> None: ...

class EffectivePermissions(_message.Message):
    __slots__ = ("user_id", "organization_id", "organization_permissions", "site_permissions", "revision")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    SITE_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    organization_id: str
    organization_permissions: _containers.RepeatedScalarFieldContainer[str]
    site_permissions: _containers.RepeatedCompositeFieldContainer[SitePermissions]
    revision: str
    def __init__(self, user_id: _Optional[str] = ..., organization_id: _Optional[str] = ..., organization_permissions: _Optional[_Iterable[str]] = ..., site_permissions: _Optional[_Iterable[_Union[SitePermissions, _Mapping]]] = ..., revision: _Optional[str] = ...) -> None: ...

class SitePermissions(_message.Message):
    __slots__ = ("site_id", "permissions")
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    site_id: str
    permissions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, site_id: _Optional[str] = ..., permissions: _Optional[_Iterable[str]] = ...) -> None: ...

class IdentityGroupMapping(_message.Message):
    __slots__ = ("id", "identity_provider_id", "group", "role_id", "site_ids")
    ID_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    SITE_IDS_FIELD_NUMBER: _ClassVar[int]
    id: str
    identity_provider_id: str
    group: str
    role_id: str
    site_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., identity_provider_id: _Optional[str] = ..., group: _Optional[str] = ..., role_id: _Optional[str] = ..., site_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class ListPermissionsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListPermissionsResponse(_message.Message):
    __slots__ = ("permissions",)
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    permissions: _containers.RepeatedCompositeFieldContainer[Permission]
    def __init__(self, permissions: _Optional[_Iterable[_Union[Permission, _Mapping]]] = ...) -> None: ...

class ListRolesRequest(_message.Message):
    __slots__ = ("page",)
    PAGE_FIELD_NUMBER: _ClassVar[int]
    page: _common_pb2.PageRequest
    def __init__(self, page: _Optional[_Union[_common_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class ListRolesResponse(_message.Message):
    __slots__ = ("roles", "page")
    ROLES_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    roles: _containers.RepeatedCompositeFieldContainer[Role]
    page: _common_pb2.PageResponse
    def __init__(self, roles: _Optional[_Iterable[_Union[Role, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class GetRoleRequest(_message.Message):
    __slots__ = ("role_id",)
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    role_id: str
    def __init__(self, role_id: _Optional[str] = ...) -> None: ...

class GetRoleResponse(_message.Message):
    __slots__ = ("role",)
    ROLE_FIELD_NUMBER: _ClassVar[int]
    role: Role
    def __init__(self, role: _Optional[_Union[Role, _Mapping]] = ...) -> None: ...

class CreateRoleRequest(_message.Message):
    __slots__ = ("context", "name", "description", "permission_ids", "copy_from_role_id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_IDS_FIELD_NUMBER: _ClassVar[int]
    COPY_FROM_ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    name: str
    description: str
    permission_ids: _containers.RepeatedScalarFieldContainer[str]
    copy_from_role_id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., permission_ids: _Optional[_Iterable[str]] = ..., copy_from_role_id: _Optional[str] = ...) -> None: ...

class CreateRoleResponse(_message.Message):
    __slots__ = ("role",)
    ROLE_FIELD_NUMBER: _ClassVar[int]
    role: Role
    def __init__(self, role: _Optional[_Union[Role, _Mapping]] = ...) -> None: ...

class UpdateRoleRequest(_message.Message):
    __slots__ = ("context", "role_id", "name", "description", "permission_ids")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_IDS_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    role_id: str
    name: str
    description: str
    permission_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., role_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., permission_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class UpdateRoleResponse(_message.Message):
    __slots__ = ("role",)
    ROLE_FIELD_NUMBER: _ClassVar[int]
    role: Role
    def __init__(self, role: _Optional[_Union[Role, _Mapping]] = ...) -> None: ...

class DeleteRoleRequest(_message.Message):
    __slots__ = ("context", "role_id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    role_id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., role_id: _Optional[str] = ...) -> None: ...

class DeleteRoleResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AssignRoleRequest(_message.Message):
    __slots__ = ("context", "user_id", "role_id", "site_ids")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    SITE_IDS_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    user_id: str
    role_id: str
    site_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., user_id: _Optional[str] = ..., role_id: _Optional[str] = ..., site_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class AssignRoleResponse(_message.Message):
    __slots__ = ("assignment",)
    ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    assignment: RoleAssignment
    def __init__(self, assignment: _Optional[_Union[RoleAssignment, _Mapping]] = ...) -> None: ...

class UnassignRoleRequest(_message.Message):
    __slots__ = ("context", "assignment_id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ASSIGNMENT_ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    assignment_id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., assignment_id: _Optional[str] = ...) -> None: ...

class UnassignRoleResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListRoleAssignmentsRequest(_message.Message):
    __slots__ = ("user_id", "role_id", "page")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    role_id: str
    page: _common_pb2.PageRequest
    def __init__(self, user_id: _Optional[str] = ..., role_id: _Optional[str] = ..., page: _Optional[_Union[_common_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class ListRoleAssignmentsResponse(_message.Message):
    __slots__ = ("assignments", "page")
    ASSIGNMENTS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    assignments: _containers.RepeatedCompositeFieldContainer[RoleAssignment]
    page: _common_pb2.PageResponse
    def __init__(self, assignments: _Optional[_Iterable[_Union[RoleAssignment, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class GetEffectivePermissionsRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class GetEffectivePermissionsResponse(_message.Message):
    __slots__ = ("permissions",)
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    permissions: EffectivePermissions
    def __init__(self, permissions: _Optional[_Union[EffectivePermissions, _Mapping]] = ...) -> None: ...

class ListIdentityGroupMappingsRequest(_message.Message):
    __slots__ = ("identity_provider_id",)
    IDENTITY_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    identity_provider_id: str
    def __init__(self, identity_provider_id: _Optional[str] = ...) -> None: ...

class ListIdentityGroupMappingsResponse(_message.Message):
    __slots__ = ("mappings",)
    MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    mappings: _containers.RepeatedCompositeFieldContainer[IdentityGroupMapping]
    def __init__(self, mappings: _Optional[_Iterable[_Union[IdentityGroupMapping, _Mapping]]] = ...) -> None: ...

class SetIdentityGroupMappingsRequest(_message.Message):
    __slots__ = ("context", "identity_provider_id", "mappings")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    identity_provider_id: str
    mappings: _containers.RepeatedCompositeFieldContainer[IdentityGroupMapping]
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., identity_provider_id: _Optional[str] = ..., mappings: _Optional[_Iterable[_Union[IdentityGroupMapping, _Mapping]]] = ...) -> None: ...

class SetIdentityGroupMappingsResponse(_message.Message):
    __slots__ = ("mappings",)
    MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    mappings: _containers.RepeatedCompositeFieldContainer[IdentityGroupMapping]
    def __init__(self, mappings: _Optional[_Iterable[_Union[IdentityGroupMapping, _Mapping]]] = ...) -> None: ...
