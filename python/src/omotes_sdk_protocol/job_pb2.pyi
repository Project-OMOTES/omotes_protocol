"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class JobSubmission(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    UUID_FIELD_NUMBER: builtins.int
    TIMEOUT_MS_FIELD_NUMBER: builtins.int
    WORKFLOW_TYPE_FIELD_NUMBER: builtins.int
    ESDL_FIELD_NUMBER: builtins.int
    uuid: builtins.str
    timeout_ms: builtins.int
    workflow_type: builtins.str
    esdl: builtins.bytes
    def __init__(
        self,
        *,
        uuid: builtins.str = ...,
        timeout_ms: builtins.int | None = ...,
        workflow_type: builtins.str = ...,
        esdl: builtins.bytes = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_timeout_ms", b"_timeout_ms", "timeout_ms", b"timeout_ms"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_timeout_ms", b"_timeout_ms", "esdl", b"esdl", "timeout_ms", b"timeout_ms", "uuid", b"uuid", "workflow_type", b"workflow_type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_timeout_ms", b"_timeout_ms"]) -> typing_extensions.Literal["timeout_ms"] | None: ...

global___JobSubmission = JobSubmission

@typing_extensions.final
class JobResult(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _ResultType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _ResultTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[JobResult._ResultType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        SUCCEEDED: JobResult._ResultType.ValueType  # 0
        TIMEOUT: JobResult._ResultType.ValueType  # 1
        ERROR: JobResult._ResultType.ValueType  # 2

    class ResultType(_ResultType, metaclass=_ResultTypeEnumTypeWrapper): ...
    SUCCEEDED: JobResult.ResultType.ValueType  # 0
    TIMEOUT: JobResult.ResultType.ValueType  # 1
    ERROR: JobResult.ResultType.ValueType  # 2

    UUID_FIELD_NUMBER: builtins.int
    RESULT_TYPE_FIELD_NUMBER: builtins.int
    uuid: builtins.str
    result_type: global___JobResult.ResultType.ValueType
    def __init__(
        self,
        *,
        uuid: builtins.str = ...,
        result_type: global___JobResult.ResultType.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["result_type", b"result_type", "uuid", b"uuid"]) -> None: ...

global___JobResult = JobResult

@typing_extensions.final
class JobProgressUpdate(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    UUID_FIELD_NUMBER: builtins.int
    PROGRESS_FIELD_NUMBER: builtins.int
    uuid: builtins.str
    progress: builtins.float
    def __init__(
        self,
        *,
        uuid: builtins.str = ...,
        progress: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["progress", b"progress", "uuid", b"uuid"]) -> None: ...

global___JobProgressUpdate = JobProgressUpdate

@typing_extensions.final
class JobStatusUpdate(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _JobStatus:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _JobStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[JobStatusUpdate._JobStatus.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        REGISTERED: JobStatusUpdate._JobStatus.ValueType  # 0
        ENQUEUED: JobStatusUpdate._JobStatus.ValueType  # 1
        RUNNING: JobStatusUpdate._JobStatus.ValueType  # 2
        FINISHED: JobStatusUpdate._JobStatus.ValueType  # 3

    class JobStatus(_JobStatus, metaclass=_JobStatusEnumTypeWrapper): ...
    REGISTERED: JobStatusUpdate.JobStatus.ValueType  # 0
    ENQUEUED: JobStatusUpdate.JobStatus.ValueType  # 1
    RUNNING: JobStatusUpdate.JobStatus.ValueType  # 2
    FINISHED: JobStatusUpdate.JobStatus.ValueType  # 3

    UUID_FIELD_NUMBER: builtins.int
    uuid: builtins.str
    def __init__(
        self,
        *,
        uuid: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["uuid", b"uuid"]) -> None: ...

global___JobStatusUpdate = JobStatusUpdate

@typing_extensions.final
class JobCancel(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    UUID_FIELD_NUMBER: builtins.int
    uuid: builtins.str
    def __init__(
        self,
        *,
        uuid: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["uuid", b"uuid"]) -> None: ...

global___JobCancel = JobCancel