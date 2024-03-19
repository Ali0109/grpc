from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class StudentRequest(_message.Message):
    __slots__ = ("name", "age")
    NAME_FIELD_NUMBER: _ClassVar[int]
    AGE_FIELD_NUMBER: _ClassVar[int]
    name: str
    age: int
    def __init__(self, name: _Optional[str] = ..., age: _Optional[int] = ...) -> None: ...

class StudentReply(_message.Message):
    __slots__ = ("course",)
    COURSE_FIELD_NUMBER: _ClassVar[int]
    course: int
    def __init__(self, course: _Optional[int] = ...) -> None: ...
