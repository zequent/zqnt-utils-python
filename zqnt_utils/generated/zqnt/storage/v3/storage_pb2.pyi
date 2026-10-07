from zqnt_utils.generated.zqnt.application.v3 import application_pb2 as _application_pb2
from zqnt_utils.generated.zqnt.common.v3 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExecutionSnapshot(_message.Message):
    __slots__ = ("format", "state")
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    format: str
    state: bytes
    def __init__(self, format: _Optional[str] = ..., state: _Optional[bytes] = ...) -> None: ...

class ExecutionEventSnapshot(_message.Message):
    __slots__ = ("format", "event")
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    format: str
    event: bytes
    def __init__(self, format: _Optional[str] = ..., event: _Optional[bytes] = ...) -> None: ...

class SaveApplicationRequest(_message.Message):
    __slots__ = ("context", "application", "expected_revision", "acted_by")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_REVISION_FIELD_NUMBER: _ClassVar[int]
    ACTED_BY_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    application: _application_pb2.Application
    expected_revision: str
    acted_by: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., application: _Optional[_Union[_application_pb2.Application, _Mapping]] = ..., expected_revision: _Optional[str] = ..., acted_by: _Optional[str] = ...) -> None: ...

class SaveApplicationResponse(_message.Message):
    __slots__ = ("application", "warnings")
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    application: _application_pb2.Application
    warnings: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, application: _Optional[_Union[_application_pb2.Application, _Mapping]] = ..., warnings: _Optional[_Iterable[str]] = ...) -> None: ...

class GetApplicationRequest(_message.Message):
    __slots__ = ("context", "application_id", "version")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    application_id: str
    version: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., application_id: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...

class GetApplicationResponse(_message.Message):
    __slots__ = ("application",)
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    application: _application_pb2.Application
    def __init__(self, application: _Optional[_Union[_application_pb2.Application, _Mapping]] = ...) -> None: ...

class ListApplicationsRequest(_message.Message):
    __slots__ = ("context",)
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ...) -> None: ...

class ListApplicationsResponse(_message.Message):
    __slots__ = ("applications",)
    APPLICATIONS_FIELD_NUMBER: _ClassVar[int]
    applications: _containers.RepeatedCompositeFieldContainer[_application_pb2.Application]
    def __init__(self, applications: _Optional[_Iterable[_Union[_application_pb2.Application, _Mapping]]] = ...) -> None: ...

class DeleteApplicationRequest(_message.Message):
    __slots__ = ("context", "application_id", "version", "expected_revision")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_REVISION_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    application_id: str
    version: str
    expected_revision: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., application_id: _Optional[str] = ..., version: _Optional[str] = ..., expected_revision: _Optional[str] = ...) -> None: ...

class DeleteApplicationResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListEnvironmentsRequest(_message.Message):
    __slots__ = ("context", "application_id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    application_id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., application_id: _Optional[str] = ...) -> None: ...

class ListEnvironmentsResponse(_message.Message):
    __slots__ = ("pointers",)
    POINTERS_FIELD_NUMBER: _ClassVar[int]
    pointers: _containers.RepeatedCompositeFieldContainer[_application_pb2.EnvironmentPointer]
    def __init__(self, pointers: _Optional[_Iterable[_Union[_application_pb2.EnvironmentPointer, _Mapping]]] = ...) -> None: ...

class PromoteVersionRequest(_message.Message):
    __slots__ = ("context", "application_id", "version", "environment", "acted_by")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    ACTED_BY_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    application_id: str
    version: str
    environment: _application_pb2.Environment
    acted_by: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., application_id: _Optional[str] = ..., version: _Optional[str] = ..., environment: _Optional[_Union[_application_pb2.Environment, str]] = ..., acted_by: _Optional[str] = ...) -> None: ...

class PromoteVersionResponse(_message.Message):
    __slots__ = ("pointers",)
    POINTERS_FIELD_NUMBER: _ClassVar[int]
    pointers: _containers.RepeatedCompositeFieldContainer[_application_pb2.EnvironmentPointer]
    def __init__(self, pointers: _Optional[_Iterable[_Union[_application_pb2.EnvironmentPointer, _Mapping]]] = ...) -> None: ...

class SetPauseRequest(_message.Message):
    __slots__ = ("context", "application_id", "skill_id", "paused", "reason", "acted_by")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    PAUSED_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    ACTED_BY_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    application_id: str
    skill_id: str
    paused: bool
    reason: str
    acted_by: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., application_id: _Optional[str] = ..., skill_id: _Optional[str] = ..., paused: bool = ..., reason: _Optional[str] = ..., acted_by: _Optional[str] = ...) -> None: ...

class SetPauseResponse(_message.Message):
    __slots__ = ("pauses",)
    PAUSES_FIELD_NUMBER: _ClassVar[int]
    pauses: _containers.RepeatedCompositeFieldContainer[_application_pb2.Pause]
    def __init__(self, pauses: _Optional[_Iterable[_Union[_application_pb2.Pause, _Mapping]]] = ...) -> None: ...

class ListPausesRequest(_message.Message):
    __slots__ = ("context", "application_id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    application_id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., application_id: _Optional[str] = ...) -> None: ...

class ListPausesResponse(_message.Message):
    __slots__ = ("pauses",)
    PAUSES_FIELD_NUMBER: _ClassVar[int]
    pauses: _containers.RepeatedCompositeFieldContainer[_application_pb2.Pause]
    def __init__(self, pauses: _Optional[_Iterable[_Union[_application_pb2.Pause, _Mapping]]] = ...) -> None: ...

class SaveExecutionRequest(_message.Message):
    __slots__ = ("context", "snapshot")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    snapshot: ExecutionSnapshot
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., snapshot: _Optional[_Union[ExecutionSnapshot, _Mapping]] = ...) -> None: ...

class SaveExecutionResponse(_message.Message):
    __slots__ = ("snapshot",)
    SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    snapshot: ExecutionSnapshot
    def __init__(self, snapshot: _Optional[_Union[ExecutionSnapshot, _Mapping]] = ...) -> None: ...

class GetExecutionRequest(_message.Message):
    __slots__ = ("context", "execution_id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    execution_id: str
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., execution_id: _Optional[str] = ...) -> None: ...

class GetExecutionResponse(_message.Message):
    __slots__ = ("snapshot",)
    SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    snapshot: ExecutionSnapshot
    def __init__(self, snapshot: _Optional[_Union[ExecutionSnapshot, _Mapping]] = ...) -> None: ...

class ListExecutionsRequest(_message.Message):
    __slots__ = ("context", "asset_sn", "organization_id", "status", "application_id", "skill_id", "site_id", "page")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    asset_sn: str
    organization_id: str
    status: str
    application_id: str
    skill_id: str
    site_id: str
    page: _common_pb2.PageRequest
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., asset_sn: _Optional[str] = ..., organization_id: _Optional[str] = ..., status: _Optional[str] = ..., application_id: _Optional[str] = ..., skill_id: _Optional[str] = ..., site_id: _Optional[str] = ..., page: _Optional[_Union[_common_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class ListExecutionsResponse(_message.Message):
    __slots__ = ("snapshots", "page")
    SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    snapshots: _containers.RepeatedCompositeFieldContainer[ExecutionSnapshot]
    page: _common_pb2.PageResponse
    def __init__(self, snapshots: _Optional[_Iterable[_Union[ExecutionSnapshot, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class AppendExecutionEventRequest(_message.Message):
    __slots__ = ("context", "event")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    event: ExecutionEventSnapshot
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., event: _Optional[_Union[ExecutionEventSnapshot, _Mapping]] = ...) -> None: ...

class AppendExecutionEventResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
