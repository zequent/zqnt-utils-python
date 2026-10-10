import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from zqnt_utils.generated.zqnt.common.v3 import common_pb2 as _common_pb2
from zqnt_utils.generated.zqnt.licensing.v3 import license_activation_pb2 as _license_activation_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Organization(_message.Message):
    __slots__ = ("id", "name", "description", "created_at", "modified_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    created_at: _timestamp_pb2.Timestamp
    modified_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Polygon(_message.Message):
    __slots__ = ("vertices",)
    VERTICES_FIELD_NUMBER: _ClassVar[int]
    vertices: _containers.RepeatedCompositeFieldContainer[_common_pb2.GeoPoint]
    def __init__(self, vertices: _Optional[_Iterable[_Union[_common_pb2.GeoPoint, _Mapping]]] = ...) -> None: ...

class Circle(_message.Message):
    __slots__ = ("center", "radius_meters")
    CENTER_FIELD_NUMBER: _ClassVar[int]
    RADIUS_METERS_FIELD_NUMBER: _ClassVar[int]
    center: _common_pb2.GeoPoint
    radius_meters: float
    def __init__(self, center: _Optional[_Union[_common_pb2.GeoPoint, _Mapping]] = ..., radius_meters: _Optional[float] = ...) -> None: ...

class Area(_message.Message):
    __slots__ = ("polygon", "circle")
    POLYGON_FIELD_NUMBER: _ClassVar[int]
    CIRCLE_FIELD_NUMBER: _ClassVar[int]
    polygon: Polygon
    circle: Circle
    def __init__(self, polygon: _Optional[_Union[Polygon, _Mapping]] = ..., circle: _Optional[_Union[Circle, _Mapping]] = ...) -> None: ...

class Site(_message.Message):
    __slots__ = ("id", "organization_id", "name", "description", "area", "parent_site_id", "asset_ids", "assigned_user_ids", "created_at", "modified_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AREA_FIELD_NUMBER: _ClassVar[int]
    PARENT_SITE_ID_FIELD_NUMBER: _ClassVar[int]
    ASSET_IDS_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_USER_IDS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    organization_id: str
    name: str
    description: str
    area: Area
    parent_site_id: str
    asset_ids: _containers.RepeatedScalarFieldContainer[str]
    assigned_user_ids: _containers.RepeatedScalarFieldContainer[str]
    created_at: _timestamp_pb2.Timestamp
    modified_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., organization_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., area: _Optional[_Union[Area, _Mapping]] = ..., parent_site_id: _Optional[str] = ..., asset_ids: _Optional[_Iterable[str]] = ..., assigned_user_ids: _Optional[_Iterable[str]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetOrganizationRequest(_message.Message):
    __slots__ = ("context", "id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...

class GetOrganizationResponse(_message.Message):
    __slots__ = ("organization",)
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    organization: Organization
    def __init__(self, organization: _Optional[_Union[Organization, _Mapping]] = ...) -> None: ...

class ListOrganizationsRequest(_message.Message):
    __slots__ = ("context",)
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ...) -> None: ...

class ListOrganizationsResponse(_message.Message):
    __slots__ = ("organizations",)
    ORGANIZATIONS_FIELD_NUMBER: _ClassVar[int]
    organizations: _containers.RepeatedCompositeFieldContainer[Organization]
    def __init__(self, organizations: _Optional[_Iterable[_Union[Organization, _Mapping]]] = ...) -> None: ...

class CreateOrganizationRequest(_message.Message):
    __slots__ = ("context", "organization")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    organization: Organization
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., organization: _Optional[_Union[Organization, _Mapping]] = ...) -> None: ...

class CreateOrganizationResponse(_message.Message):
    __slots__ = ("organization",)
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    organization: Organization
    def __init__(self, organization: _Optional[_Union[Organization, _Mapping]] = ...) -> None: ...

class UpdateOrganizationRequest(_message.Message):
    __slots__ = ("context", "organization")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    organization: Organization
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., organization: _Optional[_Union[Organization, _Mapping]] = ...) -> None: ...

class UpdateOrganizationResponse(_message.Message):
    __slots__ = ("organization",)
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    organization: Organization
    def __init__(self, organization: _Optional[_Union[Organization, _Mapping]] = ...) -> None: ...

class DeleteOrganizationRequest(_message.Message):
    __slots__ = ("context", "id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...

class DeleteOrganizationResponse(_message.Message):
    __slots__ = ("deleted",)
    DELETED_FIELD_NUMBER: _ClassVar[int]
    deleted: bool
    def __init__(self, deleted: bool = ...) -> None: ...

class ListSitesRequest(_message.Message):
    __slots__ = ("context", "organization_id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    organization_id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., organization_id: _Optional[str] = ...) -> None: ...

class ListSitesResponse(_message.Message):
    __slots__ = ("sites",)
    SITES_FIELD_NUMBER: _ClassVar[int]
    sites: _containers.RepeatedCompositeFieldContainer[Site]
    def __init__(self, sites: _Optional[_Iterable[_Union[Site, _Mapping]]] = ...) -> None: ...

class GetSiteRequest(_message.Message):
    __slots__ = ("context", "id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...

class GetSiteResponse(_message.Message):
    __slots__ = ("site",)
    SITE_FIELD_NUMBER: _ClassVar[int]
    site: Site
    def __init__(self, site: _Optional[_Union[Site, _Mapping]] = ...) -> None: ...

class CreateSiteRequest(_message.Message):
    __slots__ = ("context", "site")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SITE_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    site: Site
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., site: _Optional[_Union[Site, _Mapping]] = ...) -> None: ...

class CreateSiteResponse(_message.Message):
    __slots__ = ("site",)
    SITE_FIELD_NUMBER: _ClassVar[int]
    site: Site
    def __init__(self, site: _Optional[_Union[Site, _Mapping]] = ...) -> None: ...

class UpdateSiteRequest(_message.Message):
    __slots__ = ("context", "site")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SITE_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    site: Site
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., site: _Optional[_Union[Site, _Mapping]] = ...) -> None: ...

class UpdateSiteResponse(_message.Message):
    __slots__ = ("site",)
    SITE_FIELD_NUMBER: _ClassVar[int]
    site: Site
    def __init__(self, site: _Optional[_Union[Site, _Mapping]] = ...) -> None: ...

class DeleteSiteRequest(_message.Message):
    __slots__ = ("context", "id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...

class DeleteSiteResponse(_message.Message):
    __slots__ = ("deleted",)
    DELETED_FIELD_NUMBER: _ClassVar[int]
    deleted: bool
    def __init__(self, deleted: bool = ...) -> None: ...

class AssignUserRequest(_message.Message):
    __slots__ = ("context", "site_id", "user_id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    site_id: str
    user_id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., site_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class AssignUserResponse(_message.Message):
    __slots__ = ("site",)
    SITE_FIELD_NUMBER: _ClassVar[int]
    site: Site
    def __init__(self, site: _Optional[_Union[Site, _Mapping]] = ...) -> None: ...

class UnassignUserRequest(_message.Message):
    __slots__ = ("context", "site_id", "user_id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    site_id: str
    user_id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., site_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class UnassignUserResponse(_message.Message):
    __slots__ = ("site",)
    SITE_FIELD_NUMBER: _ClassVar[int]
    site: Site
    def __init__(self, site: _Optional[_Union[Site, _Mapping]] = ...) -> None: ...

class ProvisionLicensedOrganizationRequest(_message.Message):
    __slots__ = ("context", "organization_id", "name", "description", "activation")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ACTIVATION_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    organization_id: str
    name: str
    description: str
    activation: _license_activation_pb2.LicenseActivation
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., organization_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., activation: _Optional[_Union[_license_activation_pb2.LicenseActivation, _Mapping]] = ...) -> None: ...

class ProvisionLicensedOrganizationResponse(_message.Message):
    __slots__ = ("organization", "already_exists")
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    ALREADY_EXISTS_FIELD_NUMBER: _ClassVar[int]
    organization: Organization
    already_exists: bool
    def __init__(self, organization: _Optional[_Union[Organization, _Mapping]] = ..., already_exists: bool = ...) -> None: ...
