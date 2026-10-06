import datetime

from google.protobuf import field_mask_pb2 as _field_mask_pb2
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

class AssetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ASSET_TYPE_UNSPECIFIED: _ClassVar[AssetType]
    ASSET_TYPE_AIRCRAFT: _ClassVar[AssetType]
    ASSET_TYPE_DOCK: _ClassVar[AssetType]
    ASSET_TYPE_SENSOR: _ClassVar[AssetType]
    ASSET_TYPE_CAMERA: _ClassVar[AssetType]
    ASSET_TYPE_OTHER: _ClassVar[AssetType]
    ASSET_TYPE_JAMMER: _ClassVar[AssetType]
    ASSET_TYPE_CYBER_ATTACK: _ClassVar[AssetType]
    ASSET_TYPE_SAPIENT: _ClassVar[AssetType]
    ASSET_TYPE_RNS: _ClassVar[AssetType]

class Vendor(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VENDOR_UNSPECIFIED: _ClassVar[Vendor]
    VENDOR_DJI: _ClassVar[Vendor]
    VENDOR_AUTEL: _ClassVar[Vendor]
    VENDOR_ROS: _ClassVar[Vendor]
    VENDOR_MAVLINK: _ClassVar[Vendor]
    VENDOR_RTMP_RTSP: _ClassVar[Vendor]
    VENDOR_SAPIENT: _ClassVar[Vendor]
    VENDOR_BETAFLIGHT: _ClassVar[Vendor]
    VENDOR_RNS: _ClassVar[Vendor]
    VENDOR_ZQNT: _ClassVar[Vendor]

class Connection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONNECTION_UNSPECIFIED: _ClassVar[Connection]
    CONNECTION_MQTT: _ClassVar[Connection]
    CONNECTION_TCP: _ClassVar[Connection]
    CONNECTION_SERIAL: _ClassVar[Connection]
ASSET_TYPE_UNSPECIFIED: AssetType
ASSET_TYPE_AIRCRAFT: AssetType
ASSET_TYPE_DOCK: AssetType
ASSET_TYPE_SENSOR: AssetType
ASSET_TYPE_CAMERA: AssetType
ASSET_TYPE_OTHER: AssetType
ASSET_TYPE_JAMMER: AssetType
ASSET_TYPE_CYBER_ATTACK: AssetType
ASSET_TYPE_SAPIENT: AssetType
ASSET_TYPE_RNS: AssetType
VENDOR_UNSPECIFIED: Vendor
VENDOR_DJI: Vendor
VENDOR_AUTEL: Vendor
VENDOR_ROS: Vendor
VENDOR_MAVLINK: Vendor
VENDOR_RTMP_RTSP: Vendor
VENDOR_SAPIENT: Vendor
VENDOR_BETAFLIGHT: Vendor
VENDOR_RNS: Vendor
VENDOR_ZQNT: Vendor
CONNECTION_UNSPECIFIED: Connection
CONNECTION_MQTT: Connection
CONNECTION_TCP: Connection
CONNECTION_SERIAL: Connection

class Asset(_message.Message):
    __slots__ = ("id", "sn", "name", "type", "vendor", "model", "connection", "connection_string", "external_device_type", "external_device_sub_type", "external_id", "organization_id", "site_id", "live_stream_push_url", "live_stream_pull_url", "payloads", "sub_assets", "created_at", "modified_at", "modified_by")
    ID_FIELD_NUMBER: _ClassVar[int]
    SN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VENDOR_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_STRING_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_DEVICE_SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    LIVE_STREAM_PUSH_URL_FIELD_NUMBER: _ClassVar[int]
    LIVE_STREAM_PULL_URL_FIELD_NUMBER: _ClassVar[int]
    PAYLOADS_FIELD_NUMBER: _ClassVar[int]
    SUB_ASSETS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_BY_FIELD_NUMBER: _ClassVar[int]
    id: str
    sn: str
    name: str
    type: AssetType
    vendor: Vendor
    model: str
    connection: Connection
    connection_string: str
    external_device_type: str
    external_device_sub_type: str
    external_id: str
    organization_id: str
    site_id: str
    live_stream_push_url: str
    live_stream_pull_url: str
    payloads: _containers.RepeatedCompositeFieldContainer[Payload]
    sub_assets: _containers.RepeatedCompositeFieldContainer[SubAsset]
    created_at: _timestamp_pb2.Timestamp
    modified_at: _timestamp_pb2.Timestamp
    modified_by: str
    def __init__(self, id: _Optional[str] = ..., sn: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[_Union[AssetType, str]] = ..., vendor: _Optional[_Union[Vendor, str]] = ..., model: _Optional[str] = ..., connection: _Optional[_Union[Connection, str]] = ..., connection_string: _Optional[str] = ..., external_device_type: _Optional[str] = ..., external_device_sub_type: _Optional[str] = ..., external_id: _Optional[str] = ..., organization_id: _Optional[str] = ..., site_id: _Optional[str] = ..., live_stream_push_url: _Optional[str] = ..., live_stream_pull_url: _Optional[str] = ..., payloads: _Optional[_Iterable[_Union[Payload, _Mapping]]] = ..., sub_assets: _Optional[_Iterable[_Union[SubAsset, _Mapping]]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., modified_by: _Optional[str] = ...) -> None: ...

class SubAsset(_message.Message):
    __slots__ = ("id", "sn", "name", "type", "vendor", "model", "connection", "connection_string", "external_device_type", "external_device_sub_type", "external_id", "stream_url_predefined", "live_stream_push_url", "live_stream_pull_url", "payloads", "created_at", "modified_at", "modified_by")
    ID_FIELD_NUMBER: _ClassVar[int]
    SN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VENDOR_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_STRING_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_DEVICE_SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    STREAM_URL_PREDEFINED_FIELD_NUMBER: _ClassVar[int]
    LIVE_STREAM_PUSH_URL_FIELD_NUMBER: _ClassVar[int]
    LIVE_STREAM_PULL_URL_FIELD_NUMBER: _ClassVar[int]
    PAYLOADS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_BY_FIELD_NUMBER: _ClassVar[int]
    id: str
    sn: str
    name: str
    type: AssetType
    vendor: Vendor
    model: str
    connection: Connection
    connection_string: str
    external_device_type: str
    external_device_sub_type: str
    external_id: str
    stream_url_predefined: bool
    live_stream_push_url: str
    live_stream_pull_url: str
    payloads: _containers.RepeatedCompositeFieldContainer[Payload]
    created_at: _timestamp_pb2.Timestamp
    modified_at: _timestamp_pb2.Timestamp
    modified_by: str
    def __init__(self, id: _Optional[str] = ..., sn: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[_Union[AssetType, str]] = ..., vendor: _Optional[_Union[Vendor, str]] = ..., model: _Optional[str] = ..., connection: _Optional[_Union[Connection, str]] = ..., connection_string: _Optional[str] = ..., external_device_type: _Optional[str] = ..., external_device_sub_type: _Optional[str] = ..., external_id: _Optional[str] = ..., stream_url_predefined: bool = ..., live_stream_push_url: _Optional[str] = ..., live_stream_pull_url: _Optional[str] = ..., payloads: _Optional[_Iterable[_Union[Payload, _Mapping]]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., modified_by: _Optional[str] = ...) -> None: ...

class Payload(_message.Message):
    __slots__ = ("id", "external_id", "external_type", "slot_index", "name", "serial_number", "kind", "vendor", "model", "firmware_version", "library_version", "state", "active", "last_seen_at", "created_at", "modified_at", "modified_by", "payload_ref")
    ID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_TYPE_FIELD_NUMBER: _ClassVar[int]
    SLOT_INDEX_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    VENDOR_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    LIBRARY_VERSION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    LAST_SEEN_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_BY_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_REF_FIELD_NUMBER: _ClassVar[int]
    id: str
    external_id: str
    external_type: str
    slot_index: int
    name: str
    serial_number: str
    kind: str
    vendor: str
    model: str
    firmware_version: str
    library_version: str
    state: _struct_pb2.Struct
    active: bool
    last_seen_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    modified_at: _timestamp_pb2.Timestamp
    modified_by: str
    payload_ref: str
    def __init__(self, id: _Optional[str] = ..., external_id: _Optional[str] = ..., external_type: _Optional[str] = ..., slot_index: _Optional[int] = ..., name: _Optional[str] = ..., serial_number: _Optional[str] = ..., kind: _Optional[str] = ..., vendor: _Optional[str] = ..., model: _Optional[str] = ..., firmware_version: _Optional[str] = ..., library_version: _Optional[str] = ..., state: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., active: bool = ..., last_seen_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., modified_by: _Optional[str] = ..., payload_ref: _Optional[str] = ...) -> None: ...

class PayloadOwner(_message.Message):
    __slots__ = ("asset_id", "sub_asset_id")
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    asset_id: str
    sub_asset_id: str
    def __init__(self, asset_id: _Optional[str] = ..., sub_asset_id: _Optional[str] = ...) -> None: ...

class Property(_message.Message):
    __slots__ = ("key", "value", "description", "created_at", "modified_at")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: _struct_pb2.Value
    description: str
    created_at: _timestamp_pb2.Timestamp
    modified_at: _timestamp_pb2.Timestamp
    def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., description: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., modified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Claim(_message.Message):
    __slots__ = ("id", "organization_id", "label", "created_by", "allowed_vendor", "allowed_type", "max_redemptions", "redemption_count", "expires_at", "revoked_at", "created_at", "redemptions")
    ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_VENDOR_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_TYPE_FIELD_NUMBER: _ClassVar[int]
    MAX_REDEMPTIONS_FIELD_NUMBER: _ClassVar[int]
    REDEMPTION_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    REVOKED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    REDEMPTIONS_FIELD_NUMBER: _ClassVar[int]
    id: str
    organization_id: str
    label: str
    created_by: str
    allowed_vendor: Vendor
    allowed_type: AssetType
    max_redemptions: int
    redemption_count: int
    expires_at: _timestamp_pb2.Timestamp
    revoked_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    redemptions: _containers.RepeatedCompositeFieldContainer[ClaimRedemption]
    def __init__(self, id: _Optional[str] = ..., organization_id: _Optional[str] = ..., label: _Optional[str] = ..., created_by: _Optional[str] = ..., allowed_vendor: _Optional[_Union[Vendor, str]] = ..., allowed_type: _Optional[_Union[AssetType, str]] = ..., max_redemptions: _Optional[int] = ..., redemption_count: _Optional[int] = ..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., revoked_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., redemptions: _Optional[_Iterable[_Union[ClaimRedemption, _Mapping]]] = ...) -> None: ...

class ClaimRedemption(_message.Message):
    __slots__ = ("id", "asset_id", "sn", "redeemed_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    SN_FIELD_NUMBER: _ClassVar[int]
    REDEEMED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    asset_id: str
    sn: str
    redeemed_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., asset_id: _Optional[str] = ..., sn: _Optional[str] = ..., redeemed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListAssetsRequest(_message.Message):
    __slots__ = ("context", "organization_id", "page")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    organization_id: str
    page: _common_pb2.PageRequest
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., organization_id: _Optional[str] = ..., page: _Optional[_Union[_common_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class ListAssetsResponse(_message.Message):
    __slots__ = ("assets", "page")
    ASSETS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    assets: _containers.RepeatedCompositeFieldContainer[Asset]
    page: _common_pb2.PageResponse
    def __init__(self, assets: _Optional[_Iterable[_Union[Asset, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class GetAssetRequest(_message.Message):
    __slots__ = ("context", "asset")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    asset: _common_pb2.AssetRef
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., asset: _Optional[_Union[_common_pb2.AssetRef, _Mapping]] = ...) -> None: ...

class GetAssetResponse(_message.Message):
    __slots__ = ("asset",)
    ASSET_FIELD_NUMBER: _ClassVar[int]
    asset: Asset
    def __init__(self, asset: _Optional[_Union[Asset, _Mapping]] = ...) -> None: ...

class GetSubAssetRequest(_message.Message):
    __slots__ = ("context", "sn")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SN_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    sn: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., sn: _Optional[str] = ...) -> None: ...

class GetSubAssetResponse(_message.Message):
    __slots__ = ("sub_asset",)
    SUB_ASSET_FIELD_NUMBER: _ClassVar[int]
    sub_asset: SubAsset
    def __init__(self, sub_asset: _Optional[_Union[SubAsset, _Mapping]] = ...) -> None: ...

class RegisterAssetRequest(_message.Message):
    __slots__ = ("context", "asset")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    asset: Asset
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., asset: _Optional[_Union[Asset, _Mapping]] = ...) -> None: ...

class RegisterAssetResponse(_message.Message):
    __slots__ = ("asset",)
    ASSET_FIELD_NUMBER: _ClassVar[int]
    asset: Asset
    def __init__(self, asset: _Optional[_Union[Asset, _Mapping]] = ...) -> None: ...

class UpdateAssetRequest(_message.Message):
    __slots__ = ("context", "asset")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    asset: Asset
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., asset: _Optional[_Union[Asset, _Mapping]] = ...) -> None: ...

class UpdateAssetResponse(_message.Message):
    __slots__ = ("asset",)
    ASSET_FIELD_NUMBER: _ClassVar[int]
    asset: Asset
    def __init__(self, asset: _Optional[_Union[Asset, _Mapping]] = ...) -> None: ...

class UpdateSubAssetRequest(_message.Message):
    __slots__ = ("context", "sub_asset")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SUB_ASSET_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    sub_asset: SubAsset
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., sub_asset: _Optional[_Union[SubAsset, _Mapping]] = ...) -> None: ...

class UpdateSubAssetResponse(_message.Message):
    __slots__ = ("sub_asset",)
    SUB_ASSET_FIELD_NUMBER: _ClassVar[int]
    sub_asset: SubAsset
    def __init__(self, sub_asset: _Optional[_Union[SubAsset, _Mapping]] = ...) -> None: ...

class DeleteAssetRequest(_message.Message):
    __slots__ = ("context", "asset")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    asset: _common_pb2.AssetRef
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., asset: _Optional[_Union[_common_pb2.AssetRef, _Mapping]] = ...) -> None: ...

class DeleteAssetResponse(_message.Message):
    __slots__ = ("deleted",)
    DELETED_FIELD_NUMBER: _ClassVar[int]
    deleted: bool
    def __init__(self, deleted: bool = ...) -> None: ...

class WatchAssetsRequest(_message.Message):
    __slots__ = ("context", "organization_id", "vendor")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    VENDOR_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    organization_id: str
    vendor: Vendor
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., organization_id: _Optional[str] = ..., vendor: _Optional[_Union[Vendor, str]] = ...) -> None: ...

class WatchAssetsResponse(_message.Message):
    __slots__ = ("assets",)
    ASSETS_FIELD_NUMBER: _ClassVar[int]
    assets: _containers.RepeatedCompositeFieldContainer[Asset]
    def __init__(self, assets: _Optional[_Iterable[_Union[Asset, _Mapping]]] = ...) -> None: ...

class UpsertPayloadRequest(_message.Message):
    __slots__ = ("context", "owner", "payload", "update_mask")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    owner: PayloadOwner
    payload: Payload
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., owner: _Optional[_Union[PayloadOwner, _Mapping]] = ..., payload: _Optional[_Union[Payload, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpsertPayloadResponse(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: Payload
    def __init__(self, payload: _Optional[_Union[Payload, _Mapping]] = ...) -> None: ...

class ListPayloadsRequest(_message.Message):
    __slots__ = ("context", "owner")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    owner: PayloadOwner
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., owner: _Optional[_Union[PayloadOwner, _Mapping]] = ...) -> None: ...

class ListPayloadsResponse(_message.Message):
    __slots__ = ("payloads",)
    PAYLOADS_FIELD_NUMBER: _ClassVar[int]
    payloads: _containers.RepeatedCompositeFieldContainer[Payload]
    def __init__(self, payloads: _Optional[_Iterable[_Union[Payload, _Mapping]]] = ...) -> None: ...

class DeletePayloadRequest(_message.Message):
    __slots__ = ("context", "owner", "payload_id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    owner: PayloadOwner
    payload_id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., owner: _Optional[_Union[PayloadOwner, _Mapping]] = ..., payload_id: _Optional[str] = ...) -> None: ...

class DeletePayloadResponse(_message.Message):
    __slots__ = ("deleted",)
    DELETED_FIELD_NUMBER: _ClassVar[int]
    deleted: bool
    def __init__(self, deleted: bool = ...) -> None: ...

class SetPropertyRequest(_message.Message):
    __slots__ = ("context", "sn", "key", "value", "description")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SN_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    sn: str
    key: str
    value: _struct_pb2.Value
    description: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., sn: _Optional[str] = ..., key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., description: _Optional[str] = ...) -> None: ...

class SetPropertyResponse(_message.Message):
    __slots__ = ("property",)
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    property: Property
    def __init__(self, property: _Optional[_Union[Property, _Mapping]] = ...) -> None: ...

class ListPropertiesRequest(_message.Message):
    __slots__ = ("context", "sn")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SN_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    sn: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., sn: _Optional[str] = ...) -> None: ...

class ListPropertiesResponse(_message.Message):
    __slots__ = ("properties",)
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    properties: _containers.RepeatedCompositeFieldContainer[Property]
    def __init__(self, properties: _Optional[_Iterable[_Union[Property, _Mapping]]] = ...) -> None: ...

class DeletePropertyRequest(_message.Message):
    __slots__ = ("context", "sn", "key")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SN_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    sn: str
    key: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., sn: _Optional[str] = ..., key: _Optional[str] = ...) -> None: ...

class DeletePropertyResponse(_message.Message):
    __slots__ = ("deleted",)
    DELETED_FIELD_NUMBER: _ClassVar[int]
    deleted: bool
    def __init__(self, deleted: bool = ...) -> None: ...

class CreateClaimRequest(_message.Message):
    __slots__ = ("context", "organization_id", "label", "allowed_vendor", "allowed_type", "max_redemptions", "ttl_seconds")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_VENDOR_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_TYPE_FIELD_NUMBER: _ClassVar[int]
    MAX_REDEMPTIONS_FIELD_NUMBER: _ClassVar[int]
    TTL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    organization_id: str
    label: str
    allowed_vendor: Vendor
    allowed_type: AssetType
    max_redemptions: int
    ttl_seconds: int
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., organization_id: _Optional[str] = ..., label: _Optional[str] = ..., allowed_vendor: _Optional[_Union[Vendor, str]] = ..., allowed_type: _Optional[_Union[AssetType, str]] = ..., max_redemptions: _Optional[int] = ..., ttl_seconds: _Optional[int] = ...) -> None: ...

class CreateClaimResponse(_message.Message):
    __slots__ = ("claim", "code")
    CLAIM_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    claim: Claim
    code: str
    def __init__(self, claim: _Optional[_Union[Claim, _Mapping]] = ..., code: _Optional[str] = ...) -> None: ...

class ListClaimsRequest(_message.Message):
    __slots__ = ("context", "include_closed")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_CLOSED_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    include_closed: bool
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., include_closed: bool = ...) -> None: ...

class ListClaimsResponse(_message.Message):
    __slots__ = ("claims",)
    CLAIMS_FIELD_NUMBER: _ClassVar[int]
    claims: _containers.RepeatedCompositeFieldContainer[Claim]
    def __init__(self, claims: _Optional[_Iterable[_Union[Claim, _Mapping]]] = ...) -> None: ...

class RevokeClaimRequest(_message.Message):
    __slots__ = ("context", "claim_id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    CLAIM_ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    claim_id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., claim_id: _Optional[str] = ...) -> None: ...

class RevokeClaimResponse(_message.Message):
    __slots__ = ("claim",)
    CLAIM_FIELD_NUMBER: _ClassVar[int]
    claim: Claim
    def __init__(self, claim: _Optional[_Union[Claim, _Mapping]] = ...) -> None: ...

class DescribeClaimRequest(_message.Message):
    __slots__ = ("context", "code")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    code: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., code: _Optional[str] = ...) -> None: ...

class DescribeClaimResponse(_message.Message):
    __slots__ = ("organization_name",)
    ORGANIZATION_NAME_FIELD_NUMBER: _ClassVar[int]
    organization_name: str
    def __init__(self, organization_name: _Optional[str] = ...) -> None: ...

class RedeemClaimRequest(_message.Message):
    __slots__ = ("context", "code", "asset")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    code: str
    asset: Asset
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., code: _Optional[str] = ..., asset: _Optional[_Union[Asset, _Mapping]] = ...) -> None: ...

class RedeemClaimResponse(_message.Message):
    __slots__ = ("asset",)
    ASSET_FIELD_NUMBER: _ClassVar[int]
    asset: Asset
    def __init__(self, asset: _Optional[_Union[Asset, _Mapping]] = ...) -> None: ...
