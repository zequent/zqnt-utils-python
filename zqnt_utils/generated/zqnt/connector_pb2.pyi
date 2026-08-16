import datetime

from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from . import common_pb2 as _common_pb2
from . import base_pb2 as _base_pb2
from . import asset_pb2 as _asset_pb2
from . import device_control_contracts_pb2 as _device_control_contracts_pb2
from . import detection_pb2 as _detection_pb2
from . import mission_autonomy_types_pb2 as _mission_autonomy_types_pb2
from . import mission_autonomy_dto_pb2 as _mission_autonomy_dto_pb2
from . import events_pb2 as _events_pb2
from . import mission_autonomy_contracts_pb2 as _mission_autonomy_contracts_pb2
from . import capability_execution_contracts_pb2 as _capability_execution_contracts_pb2
from . import capability_execution_dto_pb2 as _capability_execution_dto_pb2
from . import device_control_contracts_pb2 as _device_control_contracts_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SkillContractStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SKILL_CONTRACT_STATUS_ACTIVE: _ClassVar[SkillContractStatus]
    SKILL_CONTRACT_STATUS_DRAFT: _ClassVar[SkillContractStatus]
    SKILL_CONTRACT_STATUS_DEPRECATED: _ClassVar[SkillContractStatus]
    SKILL_CONTRACT_STATUS_RETIRED: _ClassVar[SkillContractStatus]

class SkillContractCompatibility(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SKILL_CONTRACT_COMPATIBILITY_UNKNOWN: _ClassVar[SkillContractCompatibility]
    SKILL_CONTRACT_COMPATIBILITY_NEW: _ClassVar[SkillContractCompatibility]
    SKILL_CONTRACT_COMPATIBILITY_COMPATIBLE: _ClassVar[SkillContractCompatibility]
    SKILL_CONTRACT_COMPATIBILITY_BREAKING: _ClassVar[SkillContractCompatibility]

class TelemetryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TELEMETRY_TYPE_UNSPECIFIED: _ClassVar[TelemetryType]
    TELEMETRY_TYPE_ASSET: _ClassVar[TelemetryType]
    TELEMETRY_TYPE_SUBASSET: _ClassVar[TelemetryType]
SKILL_CONTRACT_STATUS_ACTIVE: SkillContractStatus
SKILL_CONTRACT_STATUS_DRAFT: SkillContractStatus
SKILL_CONTRACT_STATUS_DEPRECATED: SkillContractStatus
SKILL_CONTRACT_STATUS_RETIRED: SkillContractStatus
SKILL_CONTRACT_COMPATIBILITY_UNKNOWN: SkillContractCompatibility
SKILL_CONTRACT_COMPATIBILITY_NEW: SkillContractCompatibility
SKILL_CONTRACT_COMPATIBILITY_COMPATIBLE: SkillContractCompatibility
SKILL_CONTRACT_COMPATIBILITY_BREAKING: SkillContractCompatibility
TELEMETRY_TYPE_UNSPECIFIED: TelemetryType
TELEMETRY_TYPE_ASSET: TelemetryType
TELEMETRY_TYPE_SUBASSET: TelemetryType

class PersistSkillExecutionRequest(_message.Message):
    __slots__ = ("base", "execution")
    BASE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    execution: _capability_execution_dto_pb2.SkillExecutionProtoDTO
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., execution: _Optional[_Union[_capability_execution_dto_pb2.SkillExecutionProtoDTO, _Mapping]] = ...) -> None: ...

class AppendSkillExecutionEventRequest(_message.Message):
    __slots__ = ("base", "event")
    BASE_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    event: _capability_execution_dto_pb2.SkillExecutionEventProto
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., event: _Optional[_Union[_capability_execution_dto_pb2.SkillExecutionEventProto, _Mapping]] = ...) -> None: ...

class UpsertAssetPayloadRequest(_message.Message):
    __slots__ = ("base", "payload", "sub_asset_sn", "owner", "update_mask")
    BASE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    SUB_ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    payload: _asset_pb2.AssetPayloadProtoDTO
    sub_asset_sn: str
    owner: AssetPayloadOwner
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., payload: _Optional[_Union[_asset_pb2.AssetPayloadProtoDTO, _Mapping]] = ..., sub_asset_sn: _Optional[str] = ..., owner: _Optional[_Union[AssetPayloadOwner, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class AssetPayloadOwner(_message.Message):
    __slots__ = ("asset_id", "sub_asset_id")
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    asset_id: str
    sub_asset_id: str
    def __init__(self, asset_id: _Optional[str] = ..., sub_asset_id: _Optional[str] = ...) -> None: ...

class ListAssetPayloadsRequest(_message.Message):
    __slots__ = ("base", "owner")
    BASE_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    owner: AssetPayloadOwner
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., owner: _Optional[_Union[AssetPayloadOwner, _Mapping]] = ...) -> None: ...

class DeleteAssetPayloadRequest(_message.Message):
    __slots__ = ("base", "owner", "payload_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    owner: AssetPayloadOwner
    payload_id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., owner: _Optional[_Union[AssetPayloadOwner, _Mapping]] = ..., payload_id: _Optional[str] = ...) -> None: ...

class AssetPayloadResponse(_message.Message):
    __slots__ = ("tid", "has_errors", "payload", "error")
    TID_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    tid: str
    has_errors: bool
    payload: _asset_pb2.AssetPayloadProtoDTO
    error: _base_pb2.GlobalErrorMessage
    def __init__(self, tid: _Optional[str] = ..., has_errors: bool = ..., payload: _Optional[_Union[_asset_pb2.AssetPayloadProtoDTO, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ...) -> None: ...

class AssetPayloadListResponse(_message.Message):
    __slots__ = ("tid", "has_errors", "payloads", "error")
    TID_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    PAYLOADS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    tid: str
    has_errors: bool
    payloads: _containers.RepeatedCompositeFieldContainer[_asset_pb2.AssetPayloadProtoDTO]
    error: _base_pb2.GlobalErrorMessage
    def __init__(self, tid: _Optional[str] = ..., has_errors: bool = ..., payloads: _Optional[_Iterable[_Union[_asset_pb2.AssetPayloadProtoDTO, _Mapping]]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ...) -> None: ...

class SetAssetPropertyRequest(_message.Message):
    __slots__ = ("base", "sn", "key", "value", "description")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SN_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    sn: str
    key: str
    value: _struct_pb2.Value
    description: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., sn: _Optional[str] = ..., key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., description: _Optional[str] = ...) -> None: ...

class ListAssetPropertiesRequest(_message.Message):
    __slots__ = ("base", "sn")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SN_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    sn: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., sn: _Optional[str] = ...) -> None: ...

class DeleteAssetPropertyRequest(_message.Message):
    __slots__ = ("base", "sn", "key")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SN_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    sn: str
    key: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., sn: _Optional[str] = ..., key: _Optional[str] = ...) -> None: ...

class AssetPropertyResponse(_message.Message):
    __slots__ = ("tid", "has_errors", "property", "error")
    TID_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    tid: str
    has_errors: bool
    property: _asset_pb2.AssetPropertyProtoDTO
    error: _base_pb2.GlobalErrorMessage
    def __init__(self, tid: _Optional[str] = ..., has_errors: bool = ..., property: _Optional[_Union[_asset_pb2.AssetPropertyProtoDTO, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ...) -> None: ...

class AssetPropertyListResponse(_message.Message):
    __slots__ = ("tid", "has_errors", "properties", "error")
    TID_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    tid: str
    has_errors: bool
    properties: _containers.RepeatedCompositeFieldContainer[_asset_pb2.AssetPropertyProtoDTO]
    error: _base_pb2.GlobalErrorMessage
    def __init__(self, tid: _Optional[str] = ..., has_errors: bool = ..., properties: _Optional[_Iterable[_Union[_asset_pb2.AssetPropertyProtoDTO, _Mapping]]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ...) -> None: ...

class SkillContractProtoDTO(_message.Message):
    __slots__ = ("id", "command_id", "skill_id", "display_name", "description", "schema_version", "input_schema", "output_schema", "errors", "events", "requirements", "source", "provider", "status", "first_seen_at", "last_seen_at", "previous_schema_version", "compatibility", "compatibility_notes", "required_permissions")
    ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    REQUIREMENTS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FIRST_SEEN_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_SEEN_AT_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    COMPATIBILITY_FIELD_NUMBER: _ClassVar[int]
    COMPATIBILITY_NOTES_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    id: str
    command_id: str
    skill_id: str
    display_name: str
    description: str
    schema_version: str
    input_schema: _struct_pb2.Struct
    output_schema: _struct_pb2.Struct
    errors: _containers.RepeatedCompositeFieldContainer[_device_control_contracts_pb2_1.CapabilityErrorProto]
    events: _containers.RepeatedCompositeFieldContainer[_device_control_contracts_pb2_1.CapabilityEventProto]
    requirements: _device_control_contracts_pb2_1.CapabilityRequirementsProto
    source: _device_control_contracts_pb2_1.CapabilitySourceProto
    provider: str
    status: SkillContractStatus
    first_seen_at: _timestamp_pb2.Timestamp
    last_seen_at: _timestamp_pb2.Timestamp
    previous_schema_version: str
    compatibility: SkillContractCompatibility
    compatibility_notes: _containers.RepeatedScalarFieldContainer[str]
    required_permissions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., command_id: _Optional[str] = ..., skill_id: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., schema_version: _Optional[str] = ..., input_schema: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., output_schema: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., errors: _Optional[_Iterable[_Union[_device_control_contracts_pb2_1.CapabilityErrorProto, _Mapping]]] = ..., events: _Optional[_Iterable[_Union[_device_control_contracts_pb2_1.CapabilityEventProto, _Mapping]]] = ..., requirements: _Optional[_Union[_device_control_contracts_pb2_1.CapabilityRequirementsProto, _Mapping]] = ..., source: _Optional[_Union[_device_control_contracts_pb2_1.CapabilitySourceProto, str]] = ..., provider: _Optional[str] = ..., status: _Optional[_Union[SkillContractStatus, str]] = ..., first_seen_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_seen_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., previous_schema_version: _Optional[str] = ..., compatibility: _Optional[_Union[SkillContractCompatibility, str]] = ..., compatibility_notes: _Optional[_Iterable[str]] = ..., required_permissions: _Optional[_Iterable[str]] = ...) -> None: ...

class UpsertSkillContractRequest(_message.Message):
    __slots__ = ("base", "contract")
    BASE_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    contract: SkillContractProtoDTO
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., contract: _Optional[_Union[SkillContractProtoDTO, _Mapping]] = ...) -> None: ...

class ListSkillContractsRequest(_message.Message):
    __slots__ = ("base", "status", "command_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    status: SkillContractStatus
    command_id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., status: _Optional[_Union[SkillContractStatus, str]] = ..., command_id: _Optional[str] = ...) -> None: ...

class SetSkillContractStatusRequest(_message.Message):
    __slots__ = ("base", "id", "status")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    id: str
    status: SkillContractStatus
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., id: _Optional[str] = ..., status: _Optional[_Union[SkillContractStatus, str]] = ...) -> None: ...

class SetSkillContractPermissionsRequest(_message.Message):
    __slots__ = ("base", "id", "required_permissions")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    id: str
    required_permissions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., id: _Optional[str] = ..., required_permissions: _Optional[_Iterable[str]] = ...) -> None: ...

class SkillContractResponse(_message.Message):
    __slots__ = ("tid", "has_errors", "contract", "error")
    TID_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    tid: str
    has_errors: bool
    contract: SkillContractProtoDTO
    error: _base_pb2.GlobalErrorMessage
    def __init__(self, tid: _Optional[str] = ..., has_errors: bool = ..., contract: _Optional[_Union[SkillContractProtoDTO, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ...) -> None: ...

class SkillContractListResponse(_message.Message):
    __slots__ = ("tid", "has_errors", "contracts", "error")
    TID_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    CONTRACTS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    tid: str
    has_errors: bool
    contracts: _containers.RepeatedCompositeFieldContainer[SkillContractProtoDTO]
    error: _base_pb2.GlobalErrorMessage
    def __init__(self, tid: _Optional[str] = ..., has_errors: bool = ..., contracts: _Optional[_Iterable[_Union[SkillContractProtoDTO, _Mapping]]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ...) -> None: ...

class ConnectorGetAssetByIdRequest(_message.Message):
    __slots__ = ("base", "asset_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    asset_id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., asset_id: _Optional[str] = ...) -> None: ...

class ConnectorAssetList(_message.Message):
    __slots__ = ("assets",)
    ASSETS_FIELD_NUMBER: _ClassVar[int]
    assets: _containers.RepeatedCompositeFieldContainer[_asset_pb2.AssetProtoDTO]
    def __init__(self, assets: _Optional[_Iterable[_Union[_asset_pb2.AssetProtoDTO, _Mapping]]] = ...) -> None: ...

class ConnectorRegisterAssetRequest(_message.Message):
    __slots__ = ("base", "asset")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    asset: _asset_pb2.AssetProtoDTO
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., asset: _Optional[_Union[_asset_pb2.AssetProtoDTO, _Mapping]] = ...) -> None: ...

class ConnectorUpdateAssetRequest(_message.Message):
    __slots__ = ("base", "asset", "asset_id", "update_mask")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    asset: _asset_pb2.AssetProtoDTO
    asset_id: str
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., asset: _Optional[_Union[_asset_pb2.AssetProtoDTO, _Mapping]] = ..., asset_id: _Optional[str] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ConnectorUpdateSubAssetRequest(_message.Message):
    __slots__ = ("base", "sub_asset", "sub_asset_id", "update_mask")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SUB_ASSET_FIELD_NUMBER: _ClassVar[int]
    SUB_ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    sub_asset: _asset_pb2.SubAssetProtoDTO
    sub_asset_id: str
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., sub_asset: _Optional[_Union[_asset_pb2.SubAssetProtoDTO, _Mapping]] = ..., sub_asset_id: _Optional[str] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ConnectorResponse(_message.Message):
    __slots__ = ("tid", "id", "timestamp", "has_errors", "asset_id", "response_message", "empty", "error", "asset", "sub_asset", "organization")
    TID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    EMPTY_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    SUB_ASSET_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    tid: str
    id: str
    timestamp: _timestamp_pb2.Timestamp
    has_errors: bool
    asset_id: str
    response_message: str
    empty: _empty_pb2.Empty
    error: _base_pb2.GlobalErrorMessage
    asset: _asset_pb2.AssetProtoDTO
    sub_asset: _asset_pb2.SubAssetProtoDTO
    organization: _asset_pb2.OrganizationProtoDTO
    def __init__(self, tid: _Optional[str] = ..., id: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., has_errors: bool = ..., asset_id: _Optional[str] = ..., response_message: _Optional[str] = ..., empty: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ..., asset: _Optional[_Union[_asset_pb2.AssetProtoDTO, _Mapping]] = ..., sub_asset: _Optional[_Union[_asset_pb2.SubAssetProtoDTO, _Mapping]] = ..., organization: _Optional[_Union[_asset_pb2.OrganizationProtoDTO, _Mapping]] = ...) -> None: ...

class AssetMonitoringResponse(_message.Message):
    __slots__ = ("tid", "timestamp", "has_errors", "empty", "error", "assets")
    TID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    EMPTY_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ASSETS_FIELD_NUMBER: _ClassVar[int]
    tid: str
    timestamp: _timestamp_pb2.Timestamp
    has_errors: bool
    empty: _empty_pb2.Empty
    error: _base_pb2.GlobalErrorMessage
    assets: ConnectorAssetList
    def __init__(self, tid: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., has_errors: bool = ..., empty: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ..., assets: _Optional[_Union[ConnectorAssetList, _Mapping]] = ...) -> None: ...

class ConnectorGetOrganizationRequest(_message.Message):
    __slots__ = ("base", "bind_code")
    BASE_FIELD_NUMBER: _ClassVar[int]
    BIND_CODE_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    bind_code: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., bind_code: _Optional[str] = ...) -> None: ...

class ConnectorStoreTelemetryRequest(_message.Message):
    __slots__ = ("base", "type", "asset_telemetry", "sub_asset_telemetry")
    BASE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ASSET_TELEMETRY_FIELD_NUMBER: _ClassVar[int]
    SUB_ASSET_TELEMETRY_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    type: TelemetryType
    asset_telemetry: AssetTelemetryProto
    sub_asset_telemetry: SubAssetTelemetryProto
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., type: _Optional[_Union[TelemetryType, str]] = ..., asset_telemetry: _Optional[_Union[AssetTelemetryProto, _Mapping]] = ..., sub_asset_telemetry: _Optional[_Union[SubAssetTelemetryProto, _Mapping]] = ...) -> None: ...

class ConnectorStoreDetectionRequest(_message.Message):
    __slots__ = ("base", "asset_sn", "sub_asset_sn", "task_id", "object_id", "object_type", "confidence", "bounding_box_x", "bounding_box_y", "bounding_box_width", "bounding_box_height", "stream_url", "detected_at")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    SUB_ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    BOUNDING_BOX_X_FIELD_NUMBER: _ClassVar[int]
    BOUNDING_BOX_Y_FIELD_NUMBER: _ClassVar[int]
    BOUNDING_BOX_WIDTH_FIELD_NUMBER: _ClassVar[int]
    BOUNDING_BOX_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    STREAM_URL_FIELD_NUMBER: _ClassVar[int]
    DETECTED_AT_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    asset_sn: str
    sub_asset_sn: str
    task_id: str
    object_id: str
    object_type: str
    confidence: float
    bounding_box_x: float
    bounding_box_y: float
    bounding_box_width: float
    bounding_box_height: float
    stream_url: str
    detected_at: _timestamp_pb2.Timestamp
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., asset_sn: _Optional[str] = ..., sub_asset_sn: _Optional[str] = ..., task_id: _Optional[str] = ..., object_id: _Optional[str] = ..., object_type: _Optional[str] = ..., confidence: _Optional[float] = ..., bounding_box_x: _Optional[float] = ..., bounding_box_y: _Optional[float] = ..., bounding_box_width: _Optional[float] = ..., bounding_box_height: _Optional[float] = ..., stream_url: _Optional[str] = ..., detected_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AssetTelemetryProto(_message.Message):
    __slots__ = ("asset_id", "timestamp", "latitude", "longitude", "altitude", "relative_altitude", "heading", "temperature", "humidity", "wind_speed", "battery_percentage", "network_type", "network_quality", "operational_mode", "is_online", "source_system", "telemetry_data")
    class TelemetryDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    HEADING_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    HUMIDITY_FIELD_NUMBER: _ClassVar[int]
    WIND_SPEED_FIELD_NUMBER: _ClassVar[int]
    BATTERY_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_TYPE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_QUALITY_FIELD_NUMBER: _ClassVar[int]
    OPERATIONAL_MODE_FIELD_NUMBER: _ClassVar[int]
    IS_ONLINE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    TELEMETRY_DATA_FIELD_NUMBER: _ClassVar[int]
    asset_id: str
    timestamp: _timestamp_pb2.Timestamp
    latitude: float
    longitude: float
    altitude: float
    relative_altitude: float
    heading: float
    temperature: float
    humidity: float
    wind_speed: float
    battery_percentage: float
    network_type: str
    network_quality: int
    operational_mode: str
    is_online: bool
    source_system: str
    telemetry_data: _containers.ScalarMap[str, str]
    def __init__(self, asset_id: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., altitude: _Optional[float] = ..., relative_altitude: _Optional[float] = ..., heading: _Optional[float] = ..., temperature: _Optional[float] = ..., humidity: _Optional[float] = ..., wind_speed: _Optional[float] = ..., battery_percentage: _Optional[float] = ..., network_type: _Optional[str] = ..., network_quality: _Optional[int] = ..., operational_mode: _Optional[str] = ..., is_online: bool = ..., source_system: _Optional[str] = ..., telemetry_data: _Optional[_Mapping[str, str]] = ...) -> None: ...

class SubAssetTelemetryProto(_message.Message):
    __slots__ = ("asset_id", "timestamp", "latitude", "longitude", "altitude", "relative_altitude", "heading", "horizontal_speed", "vertical_speed", "wind_speed", "battery_percentage", "operational_mode", "is_online", "source_system", "telemetry_data")
    class TelemetryDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    HEADING_FIELD_NUMBER: _ClassVar[int]
    HORIZONTAL_SPEED_FIELD_NUMBER: _ClassVar[int]
    VERTICAL_SPEED_FIELD_NUMBER: _ClassVar[int]
    WIND_SPEED_FIELD_NUMBER: _ClassVar[int]
    BATTERY_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    OPERATIONAL_MODE_FIELD_NUMBER: _ClassVar[int]
    IS_ONLINE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    TELEMETRY_DATA_FIELD_NUMBER: _ClassVar[int]
    asset_id: str
    timestamp: _timestamp_pb2.Timestamp
    latitude: float
    longitude: float
    altitude: float
    relative_altitude: float
    heading: float
    horizontal_speed: float
    vertical_speed: float
    wind_speed: float
    battery_percentage: float
    operational_mode: str
    is_online: bool
    source_system: str
    telemetry_data: _containers.ScalarMap[str, str]
    def __init__(self, asset_id: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., altitude: _Optional[float] = ..., relative_altitude: _Optional[float] = ..., heading: _Optional[float] = ..., horizontal_speed: _Optional[float] = ..., vertical_speed: _Optional[float] = ..., wind_speed: _Optional[float] = ..., battery_percentage: _Optional[float] = ..., operational_mode: _Optional[str] = ..., is_online: bool = ..., source_system: _Optional[str] = ..., telemetry_data: _Optional[_Mapping[str, str]] = ...) -> None: ...

class PolicyProtoDTO(_message.Message):
    __slots__ = ("id", "name", "description", "policy_type", "scope", "scope_target", "priority", "active", "strategy_type", "conditions", "constraints", "actions")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    POLICY_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_TARGET_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    STRATEGY_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    policy_type: str
    scope: str
    scope_target: str
    priority: int
    active: bool
    strategy_type: str
    conditions: str
    constraints: str
    actions: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., policy_type: _Optional[str] = ..., scope: _Optional[str] = ..., scope_target: _Optional[str] = ..., priority: _Optional[int] = ..., active: bool = ..., strategy_type: _Optional[str] = ..., conditions: _Optional[str] = ..., constraints: _Optional[str] = ..., actions: _Optional[str] = ...) -> None: ...

class PolicyProtoDTOList(_message.Message):
    __slots__ = ("policies",)
    POLICIES_FIELD_NUMBER: _ClassVar[int]
    policies: _containers.RepeatedCompositeFieldContainer[PolicyProtoDTO]
    def __init__(self, policies: _Optional[_Iterable[_Union[PolicyProtoDTO, _Mapping]]] = ...) -> None: ...

class ConnectorGetPoliciesRequest(_message.Message):
    __slots__ = ("base", "policy_type")
    BASE_FIELD_NUMBER: _ClassVar[int]
    POLICY_TYPE_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    policy_type: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., policy_type: _Optional[str] = ...) -> None: ...

class ConnectorGetAllPoliciesRequest(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ...) -> None: ...

class ConnectorPolicyResponse(_message.Message):
    __slots__ = ("tid", "has_errors", "timestamp", "error", "policy_list")
    TID_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    POLICY_LIST_FIELD_NUMBER: _ClassVar[int]
    tid: str
    has_errors: bool
    timestamp: _timestamp_pb2.Timestamp
    error: _base_pb2.GlobalErrorMessage
    policy_list: PolicyProtoDTOList
    def __init__(self, tid: _Optional[str] = ..., has_errors: bool = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ..., policy_list: _Optional[_Union[PolicyProtoDTOList, _Mapping]] = ...) -> None: ...

class TechnicalConfigProtoDTO(_message.Message):
    __slots__ = ("id", "config_key", "config_value", "value_type", "scope", "scope_target", "active", "description")
    ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_KEY_FIELD_NUMBER: _ClassVar[int]
    CONFIG_VALUE_FIELD_NUMBER: _ClassVar[int]
    VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_TARGET_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    id: str
    config_key: str
    config_value: str
    value_type: str
    scope: str
    scope_target: str
    active: bool
    description: str
    def __init__(self, id: _Optional[str] = ..., config_key: _Optional[str] = ..., config_value: _Optional[str] = ..., value_type: _Optional[str] = ..., scope: _Optional[str] = ..., scope_target: _Optional[str] = ..., active: bool = ..., description: _Optional[str] = ...) -> None: ...

class TechnicalConfigProtoDTOList(_message.Message):
    __slots__ = ("configs",)
    CONFIGS_FIELD_NUMBER: _ClassVar[int]
    configs: _containers.RepeatedCompositeFieldContainer[TechnicalConfigProtoDTO]
    def __init__(self, configs: _Optional[_Iterable[_Union[TechnicalConfigProtoDTO, _Mapping]]] = ...) -> None: ...

class ConnectorGetConfigsRequest(_message.Message):
    __slots__ = ("base", "scope", "scope_target")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_TARGET_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    scope: str
    scope_target: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., scope: _Optional[str] = ..., scope_target: _Optional[str] = ...) -> None: ...

class ConnectorConfigResponse(_message.Message):
    __slots__ = ("tid", "has_errors", "timestamp", "error", "config_list")
    TID_FIELD_NUMBER: _ClassVar[int]
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CONFIG_LIST_FIELD_NUMBER: _ClassVar[int]
    tid: str
    has_errors: bool
    timestamp: _timestamp_pb2.Timestamp
    error: _base_pb2.GlobalErrorMessage
    config_list: TechnicalConfigProtoDTOList
    def __init__(self, tid: _Optional[str] = ..., has_errors: bool = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ..., config_list: _Optional[_Union[TechnicalConfigProtoDTOList, _Mapping]] = ...) -> None: ...
