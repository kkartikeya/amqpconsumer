# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/kkartikeya/home/internet/speed.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='com/kkartikeya/home/internet/speed.proto',
  package='com.kkartikeya.home.internet',
  syntax='proto3',
  serialized_pb=_b('\n(com/kkartikeya/home/internet/speed.proto\x12\x1c\x63om.kkartikeya.home.internet\"J\n\x05Speed\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x12\x0c\n\x04ping\x18\x02 \x01(\x02\x12\x10\n\x08\x64ownload\x18\x03 \x01(\x02\x12\x0e\n\x06upload\x18\x04 \x01(\x02\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SPEED = _descriptor.Descriptor(
  name='Speed',
  full_name='com.kkartikeya.home.internet.Speed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='com.kkartikeya.home.internet.Speed.timestamp', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ping', full_name='com.kkartikeya.home.internet.Speed.ping', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='download', full_name='com.kkartikeya.home.internet.Speed.download', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='upload', full_name='com.kkartikeya.home.internet.Speed.upload', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=74,
  serialized_end=148,
)

DESCRIPTOR.message_types_by_name['Speed'] = _SPEED

Speed = _reflection.GeneratedProtocolMessageType('Speed', (_message.Message,), dict(
  DESCRIPTOR = _SPEED,
  __module__ = 'com.kkartikeya.home.internet.speed_pb2'
  # @@protoc_insertion_point(class_scope:com.kkartikeya.home.internet.Speed)
  ))
_sym_db.RegisterMessage(Speed)


# @@protoc_insertion_point(module_scope)