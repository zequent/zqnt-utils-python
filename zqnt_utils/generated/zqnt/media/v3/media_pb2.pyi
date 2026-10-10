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

class MediaType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MEDIA_TYPE_UNSPECIFIED: _ClassVar[MediaType]
    MEDIA_TYPE_PHOTO: _ClassVar[MediaType]
    MEDIA_TYPE_VIDEO: _ClassVar[MediaType]
    MEDIA_TYPE_OTHER: _ClassVar[MediaType]

class MediaFileStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MEDIA_FILE_STATUS_UNSPECIFIED: _ClassVar[MediaFileStatus]
    MEDIA_FILE_STATUS_STORED: _ClassVar[MediaFileStatus]
    MEDIA_FILE_STATUS_PENDING: _ClassVar[MediaFileStatus]
MEDIA_TYPE_UNSPECIFIED: MediaType
MEDIA_TYPE_PHOTO: MediaType
MEDIA_TYPE_VIDEO: MediaType
MEDIA_TYPE_OTHER: MediaType
MEDIA_FILE_STATUS_UNSPECIFIED: MediaFileStatus
MEDIA_FILE_STATUS_STORED: MediaFileStatus
MEDIA_FILE_STATUS_PENDING: MediaFileStatus

class CapturePosition(_message.Message):
    __slots__ = ("point", "relative_altitude", "gimbal_yaw")
    POINT_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    GIMBAL_YAW_FIELD_NUMBER: _ClassVar[int]
    point: _common_pb2.GeoPoint
    relative_altitude: float
    gimbal_yaw: float
    def __init__(self, point: _Optional[_Union[_common_pb2.GeoPoint, _Mapping]] = ..., relative_altitude: _Optional[float] = ..., gimbal_yaw: _Optional[float] = ...) -> None: ...

class MediaFile(_message.Message):
    __slots__ = ("id", "media_type", "status", "file_name", "content_type", "size_bytes", "folder_path", "asset_sn", "device_sn", "organization_id", "execution_id", "application_id", "skill_id", "captured_at", "uploaded_at", "position", "vendor_flight_id", "metadata", "download_url", "organization_name", "application_name", "skill_name")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    MEDIA_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    DEVICE_SN_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    CAPTURED_AT_FIELD_NUMBER: _ClassVar[int]
    UPLOADED_AT_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    VENDOR_FLIGHT_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_NAME_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_NAME_FIELD_NUMBER: _ClassVar[int]
    SKILL_NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    media_type: MediaType
    status: MediaFileStatus
    file_name: str
    content_type: str
    size_bytes: int
    folder_path: str
    asset_sn: str
    device_sn: str
    organization_id: str
    execution_id: str
    application_id: str
    skill_id: str
    captured_at: _timestamp_pb2.Timestamp
    uploaded_at: _timestamp_pb2.Timestamp
    position: CapturePosition
    vendor_flight_id: str
    metadata: _containers.ScalarMap[str, str]
    download_url: str
    organization_name: str
    application_name: str
    skill_name: str
    def __init__(self, id: _Optional[str] = ..., media_type: _Optional[_Union[MediaType, str]] = ..., status: _Optional[_Union[MediaFileStatus, str]] = ..., file_name: _Optional[str] = ..., content_type: _Optional[str] = ..., size_bytes: _Optional[int] = ..., folder_path: _Optional[str] = ..., asset_sn: _Optional[str] = ..., device_sn: _Optional[str] = ..., organization_id: _Optional[str] = ..., execution_id: _Optional[str] = ..., application_id: _Optional[str] = ..., skill_id: _Optional[str] = ..., captured_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., uploaded_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., position: _Optional[_Union[CapturePosition, _Mapping]] = ..., vendor_flight_id: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., download_url: _Optional[str] = ..., organization_name: _Optional[str] = ..., application_name: _Optional[str] = ..., skill_name: _Optional[str] = ...) -> None: ...

class RegisterMediaFileRequest(_message.Message):
    __slots__ = ("context", "asset_sn", "device_sn", "source_bucket", "source_object_key", "file_name", "execution_id", "vendor_flight_id", "captured_at", "position", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    DEVICE_SN_FIELD_NUMBER: _ClassVar[int]
    SOURCE_BUCKET_FIELD_NUMBER: _ClassVar[int]
    SOURCE_OBJECT_KEY_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    VENDOR_FLIGHT_ID_FIELD_NUMBER: _ClassVar[int]
    CAPTURED_AT_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    asset_sn: str
    device_sn: str
    source_bucket: str
    source_object_key: str
    file_name: str
    execution_id: str
    vendor_flight_id: str
    captured_at: _timestamp_pb2.Timestamp
    position: CapturePosition
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., asset_sn: _Optional[str] = ..., device_sn: _Optional[str] = ..., source_bucket: _Optional[str] = ..., source_object_key: _Optional[str] = ..., file_name: _Optional[str] = ..., execution_id: _Optional[str] = ..., vendor_flight_id: _Optional[str] = ..., captured_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., position: _Optional[_Union[CapturePosition, _Mapping]] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...

class RegisterMediaFileResponse(_message.Message):
    __slots__ = ("file",)
    FILE_FIELD_NUMBER: _ClassVar[int]
    file: MediaFile
    def __init__(self, file: _Optional[_Union[MediaFile, _Mapping]] = ...) -> None: ...

class ListMediaFilesRequest(_message.Message):
    __slots__ = ("context", "organization_id", "folder_path", "execution_id", "asset_sn", "page")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    organization_id: str
    folder_path: str
    execution_id: str
    asset_sn: str
    page: _common_pb2.PageRequest
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., organization_id: _Optional[str] = ..., folder_path: _Optional[str] = ..., execution_id: _Optional[str] = ..., asset_sn: _Optional[str] = ..., page: _Optional[_Union[_common_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class ListMediaFilesResponse(_message.Message):
    __slots__ = ("files", "folders", "page")
    FILES_FIELD_NUMBER: _ClassVar[int]
    FOLDERS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    files: _containers.RepeatedCompositeFieldContainer[MediaFile]
    folders: _containers.RepeatedScalarFieldContainer[str]
    page: _common_pb2.PageResponse
    def __init__(self, files: _Optional[_Iterable[_Union[MediaFile, _Mapping]]] = ..., folders: _Optional[_Iterable[str]] = ..., page: _Optional[_Union[_common_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class GetMediaFileRequest(_message.Message):
    __slots__ = ("context", "id", "organization_id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    id: str
    organization_id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., id: _Optional[str] = ..., organization_id: _Optional[str] = ...) -> None: ...

class GetMediaFileResponse(_message.Message):
    __slots__ = ("file",)
    FILE_FIELD_NUMBER: _ClassVar[int]
    file: MediaFile
    def __init__(self, file: _Optional[_Union[MediaFile, _Mapping]] = ...) -> None: ...
