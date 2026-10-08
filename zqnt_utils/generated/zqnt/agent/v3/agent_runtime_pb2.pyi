import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from zqnt_utils.generated.zqnt.common.v3 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ApprovalDecision(_message.Message):
    __slots__ = ("tool_call_id", "approval_id", "approved")
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_ID_FIELD_NUMBER: _ClassVar[int]
    APPROVED_FIELD_NUMBER: _ClassVar[int]
    tool_call_id: str
    approval_id: str
    approved: bool
    def __init__(self, tool_call_id: _Optional[str] = ..., approval_id: _Optional[str] = ..., approved: bool = ...) -> None: ...

class RunChatTurnRequest(_message.Message):
    __slots__ = ("context", "session_id", "user_text", "file_ids", "model_id", "approvals")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    USER_TEXT_FIELD_NUMBER: _ClassVar[int]
    FILE_IDS_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    APPROVALS_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    session_id: str
    user_text: str
    file_ids: _containers.RepeatedScalarFieldContainer[str]
    model_id: str
    approvals: _containers.RepeatedCompositeFieldContainer[ApprovalDecision]
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., session_id: _Optional[str] = ..., user_text: _Optional[str] = ..., file_ids: _Optional[_Iterable[str]] = ..., model_id: _Optional[str] = ..., approvals: _Optional[_Iterable[_Union[ApprovalDecision, _Mapping]]] = ...) -> None: ...

class RunChatTurnResponse(_message.Message):
    __slots__ = ("ui_stream_part", "done")
    UI_STREAM_PART_FIELD_NUMBER: _ClassVar[int]
    DONE_FIELD_NUMBER: _ClassVar[int]
    ui_stream_part: str
    done: TurnSummary
    def __init__(self, ui_stream_part: _Optional[str] = ..., done: _Optional[_Union[TurnSummary, _Mapping]] = ...) -> None: ...

class TurnSummary(_message.Message):
    __slots__ = ("turn_id", "input_tokens", "output_tokens", "cost_micro_eur", "pending_tool_call_ids", "error")
    TURN_ID_FIELD_NUMBER: _ClassVar[int]
    INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    COST_MICRO_EUR_FIELD_NUMBER: _ClassVar[int]
    PENDING_TOOL_CALL_IDS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    turn_id: str
    input_tokens: int
    output_tokens: int
    cost_micro_eur: int
    pending_tool_call_ids: _containers.RepeatedScalarFieldContainer[str]
    error: _common_pb2.Error
    def __init__(self, turn_id: _Optional[str] = ..., input_tokens: _Optional[int] = ..., output_tokens: _Optional[int] = ..., cost_micro_eur: _Optional[int] = ..., pending_tool_call_ids: _Optional[_Iterable[str]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ...) -> None: ...

class CancelChatTurnRequest(_message.Message):
    __slots__ = ("session_id",)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    def __init__(self, session_id: _Optional[str] = ...) -> None: ...

class CancelChatTurnResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RunAiNodeRequest(_message.Message):
    __slots__ = ("context", "session_id", "execution_id", "node_id", "prompt", "prompt_version", "model_id", "inputs", "output_schema", "timeout")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    PROMPT_VERSION_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    context: _common_pb2.RequestContext
    session_id: str
    execution_id: str
    node_id: str
    prompt: str
    prompt_version: str
    model_id: str
    inputs: _struct_pb2.Struct
    output_schema: _struct_pb2.Struct
    timeout: _duration_pb2.Duration
    def __init__(self, context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., session_id: _Optional[str] = ..., execution_id: _Optional[str] = ..., node_id: _Optional[str] = ..., prompt: _Optional[str] = ..., prompt_version: _Optional[str] = ..., model_id: _Optional[str] = ..., inputs: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., output_schema: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., timeout: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class RunAiNodeResponse(_message.Message):
    __slots__ = ("output", "model_id", "input_tokens", "output_tokens", "cost_micro_eur", "conversation_id", "error")
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    COST_MICRO_EUR_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    output: _struct_pb2.Struct
    model_id: str
    input_tokens: int
    output_tokens: int
    cost_micro_eur: int
    conversation_id: str
    error: _common_pb2.Error
    def __init__(self, output: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., model_id: _Optional[str] = ..., input_tokens: _Optional[int] = ..., output_tokens: _Optional[int] = ..., cost_micro_eur: _Optional[int] = ..., conversation_id: _Optional[str] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ...) -> None: ...
