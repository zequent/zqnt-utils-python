import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from zqnt_utils.generated.zqnt.common.v3 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExecutionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXECUTION_STATUS_UNSPECIFIED: _ClassVar[ExecutionStatus]
    EXECUTION_STATUS_PENDING: _ClassVar[ExecutionStatus]
    EXECUTION_STATUS_RUNNING: _ClassVar[ExecutionStatus]
    EXECUTION_STATUS_PAUSED: _ClassVar[ExecutionStatus]
    EXECUTION_STATUS_SUCCEEDED: _ClassVar[ExecutionStatus]
    EXECUTION_STATUS_FAILED: _ClassVar[ExecutionStatus]
    EXECUTION_STATUS_CANCELLED: _ClassVar[ExecutionStatus]
    EXECUTION_STATUS_TIMED_OUT: _ClassVar[ExecutionStatus]
    EXECUTION_STATUS_CANCELLING: _ClassVar[ExecutionStatus]

class NodeStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NODE_STATUS_UNSPECIFIED: _ClassVar[NodeStatus]
    NODE_STATUS_PENDING: _ClassVar[NodeStatus]
    NODE_STATUS_RUNNING: _ClassVar[NodeStatus]
    NODE_STATUS_SUCCEEDED: _ClassVar[NodeStatus]
    NODE_STATUS_FAILED: _ClassVar[NodeStatus]
    NODE_STATUS_SKIPPED: _ClassVar[NodeStatus]
    NODE_STATUS_CANCELLED: _ClassVar[NodeStatus]
    NODE_STATUS_TIMED_OUT: _ClassVar[NodeStatus]
    NODE_STATUS_WAITING: _ClassVar[NodeStatus]
    NODE_STATUS_PAUSED: _ClassVar[NodeStatus]

class StatsGrouping(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STATS_GROUPING_UNSPECIFIED: _ClassVar[StatsGrouping]
    STATS_GROUPING_NONE: _ClassVar[StatsGrouping]
    STATS_GROUPING_DAY: _ClassVar[StatsGrouping]
    STATS_GROUPING_APPLICATION: _ClassVar[StatsGrouping]
    STATS_GROUPING_ASSET: _ClassVar[StatsGrouping]
    STATS_GROUPING_SITE: _ClassVar[StatsGrouping]
EXECUTION_STATUS_UNSPECIFIED: ExecutionStatus
EXECUTION_STATUS_PENDING: ExecutionStatus
EXECUTION_STATUS_RUNNING: ExecutionStatus
EXECUTION_STATUS_PAUSED: ExecutionStatus
EXECUTION_STATUS_SUCCEEDED: ExecutionStatus
EXECUTION_STATUS_FAILED: ExecutionStatus
EXECUTION_STATUS_CANCELLED: ExecutionStatus
EXECUTION_STATUS_TIMED_OUT: ExecutionStatus
EXECUTION_STATUS_CANCELLING: ExecutionStatus
NODE_STATUS_UNSPECIFIED: NodeStatus
NODE_STATUS_PENDING: NodeStatus
NODE_STATUS_RUNNING: NodeStatus
NODE_STATUS_SUCCEEDED: NodeStatus
NODE_STATUS_FAILED: NodeStatus
NODE_STATUS_SKIPPED: NodeStatus
NODE_STATUS_CANCELLED: NodeStatus
NODE_STATUS_TIMED_OUT: NodeStatus
NODE_STATUS_WAITING: NodeStatus
NODE_STATUS_PAUSED: NodeStatus
STATS_GROUPING_UNSPECIFIED: StatsGrouping
STATS_GROUPING_NONE: StatsGrouping
STATS_GROUPING_DAY: StatsGrouping
STATS_GROUPING_APPLICATION: StatsGrouping
STATS_GROUPING_ASSET: StatsGrouping
STATS_GROUPING_SITE: StatsGrouping

class TimeRange(_message.Message):
    __slots__ = ("to",)
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    to: _timestamp_pb2.Timestamp
    def __init__(self, to: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., **kwargs) -> None: ...

class NodeRun(_message.Message):
    __slots__ = ("execution_id", "node_id", "node_name", "command_id", "asset_sn", "status", "attempt", "started_at", "completed_at", "duration", "error")
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_NAME_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    execution_id: str
    node_id: str
    node_name: str
    command_id: str
    asset_sn: str
    status: NodeStatus
    attempt: int
    started_at: _timestamp_pb2.Timestamp
    completed_at: _timestamp_pb2.Timestamp
    duration: _duration_pb2.Duration
    error: _common_pb2.Error
    def __init__(self, execution_id: _Optional[str] = ..., node_id: _Optional[str] = ..., node_name: _Optional[str] = ..., command_id: _Optional[str] = ..., asset_sn: _Optional[str] = ..., status: _Optional[_Union[NodeStatus, str]] = ..., attempt: _Optional[int] = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., completed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., duration: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ...) -> None: ...

class ExecutionFilter(_message.Message):
    __slots__ = ("time_range", "application_id", "skill_id", "asset_sn", "site_id", "statuses")
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    STATUSES_FIELD_NUMBER: _ClassVar[int]
    time_range: TimeRange
    application_id: str
    skill_id: str
    asset_sn: str
    site_id: str
    statuses: _containers.RepeatedScalarFieldContainer[ExecutionStatus]
    def __init__(self, time_range: _Optional[_Union[TimeRange, _Mapping]] = ..., application_id: _Optional[str] = ..., skill_id: _Optional[str] = ..., asset_sn: _Optional[str] = ..., site_id: _Optional[str] = ..., statuses: _Optional[_Iterable[_Union[ExecutionStatus, str]]] = ...) -> None: ...

class StatusCount(_message.Message):
    __slots__ = ("status", "count")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    status: ExecutionStatus
    count: int
    def __init__(self, status: _Optional[_Union[ExecutionStatus, str]] = ..., count: _Optional[int] = ...) -> None: ...

class NodeFailureCount(_message.Message):
    __slots__ = ("node_id", "node_name", "command_id", "failures", "top_error_code")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_NAME_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    FAILURES_FIELD_NUMBER: _ClassVar[int]
    TOP_ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    node_id: str
    node_name: str
    command_id: str
    failures: int
    top_error_code: str
    def __init__(self, node_id: _Optional[str] = ..., node_name: _Optional[str] = ..., command_id: _Optional[str] = ..., failures: _Optional[int] = ..., top_error_code: _Optional[str] = ...) -> None: ...

class ExecutionStatsBucket(_message.Message):
    __slots__ = ("key", "runs", "by_status", "success_rate", "duration_p50", "duration_p95", "failing_nodes")
    KEY_FIELD_NUMBER: _ClassVar[int]
    RUNS_FIELD_NUMBER: _ClassVar[int]
    BY_STATUS_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_RATE_FIELD_NUMBER: _ClassVar[int]
    DURATION_P50_FIELD_NUMBER: _ClassVar[int]
    DURATION_P95_FIELD_NUMBER: _ClassVar[int]
    FAILING_NODES_FIELD_NUMBER: _ClassVar[int]
    key: str
    runs: int
    by_status: _containers.RepeatedCompositeFieldContainer[StatusCount]
    success_rate: float
    duration_p50: _duration_pb2.Duration
    duration_p95: _duration_pb2.Duration
    failing_nodes: _containers.RepeatedCompositeFieldContainer[NodeFailureCount]
    def __init__(self, key: _Optional[str] = ..., runs: _Optional[int] = ..., by_status: _Optional[_Iterable[_Union[StatusCount, _Mapping]]] = ..., success_rate: _Optional[float] = ..., duration_p50: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., duration_p95: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., failing_nodes: _Optional[_Iterable[_Union[NodeFailureCount, _Mapping]]] = ...) -> None: ...

class GetExecutionStatsRequest(_message.Message):
    __slots__ = ("filter", "grouping", "failing_nodes_limit")
    FILTER_FIELD_NUMBER: _ClassVar[int]
    GROUPING_FIELD_NUMBER: _ClassVar[int]
    FAILING_NODES_LIMIT_FIELD_NUMBER: _ClassVar[int]
    filter: ExecutionFilter
    grouping: StatsGrouping
    failing_nodes_limit: int
    def __init__(self, filter: _Optional[_Union[ExecutionFilter, _Mapping]] = ..., grouping: _Optional[_Union[StatsGrouping, str]] = ..., failing_nodes_limit: _Optional[int] = ...) -> None: ...

class GetExecutionStatsResponse(_message.Message):
    __slots__ = ("buckets",)
    BUCKETS_FIELD_NUMBER: _ClassVar[int]
    buckets: _containers.RepeatedCompositeFieldContainer[ExecutionStatsBucket]
    def __init__(self, buckets: _Optional[_Iterable[_Union[ExecutionStatsBucket, _Mapping]]] = ...) -> None: ...

class ListNodeRunsRequest(_message.Message):
    __slots__ = ("execution_id", "filter", "statuses", "page")
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    STATUSES_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    execution_id: str
    filter: ExecutionFilter
    statuses: _containers.RepeatedScalarFieldContainer[NodeStatus]
    page: _common_pb2.PageRequest
    def __init__(self, execution_id: _Optional[str] = ..., filter: _Optional[_Union[ExecutionFilter, _Mapping]] = ..., statuses: _Optional[_Iterable[_Union[NodeStatus, str]]] = ..., page: _Optional[_Union[_common_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class ListNodeRunsResponse(_message.Message):
    __slots__ = ("node_runs", "page")
    NODE_RUNS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    node_runs: _containers.RepeatedCompositeFieldContainer[NodeRun]
    page: _common_pb2.PageResponse
    def __init__(self, node_runs: _Optional[_Iterable[_Union[NodeRun, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.PageResponse, _Mapping]] = ...) -> None: ...
