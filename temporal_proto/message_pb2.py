# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='message.proto',
  package='temporal.version.v1',
  syntax='proto3',
  serialized_options=b'\n\034io.temporal.proto.version.v1B\014MessageProtoP\001Z0go.temporal.io/temporal-proto/version/v1;version',
  serialized_pb=b'\n\rmessage.proto\x12\x13temporal.version.v1\"8\n\x14SupportedSDKVersions\x12\x0e\n\x06go_sdk\x18\x01 \x01(\t\x12\x10\n\x08java_sdk\x18\x02 \x01(\t\"D\n\x11WorkerVersionInfo\x12\x16\n\x0eimplementation\x18\x01 \x01(\t\x12\x17\n\x0f\x66\x65\x61ture_version\x18\x02 \x01(\tB`\n\x1cio.temporal.proto.version.v1B\x0cMessageProtoP\x01Z0go.temporal.io/temporal-proto/version/v1;versionb\x06proto3'
)




_SUPPORTEDSDKVERSIONS = _descriptor.Descriptor(
  name='SupportedSDKVersions',
  full_name='temporal.version.v1.SupportedSDKVersions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='go_sdk', full_name='temporal.version.v1.SupportedSDKVersions.go_sdk', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='java_sdk', full_name='temporal.version.v1.SupportedSDKVersions.java_sdk', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=94,
)


_WORKERVERSIONINFO = _descriptor.Descriptor(
  name='WorkerVersionInfo',
  full_name='temporal.version.v1.WorkerVersionInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='implementation', full_name='temporal.version.v1.WorkerVersionInfo.implementation', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='feature_version', full_name='temporal.version.v1.WorkerVersionInfo.feature_version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=96,
  serialized_end=164,
)

DESCRIPTOR.message_types_by_name['SupportedSDKVersions'] = _SUPPORTEDSDKVERSIONS
DESCRIPTOR.message_types_by_name['WorkerVersionInfo'] = _WORKERVERSIONINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SupportedSDKVersions = _reflection.GeneratedProtocolMessageType('SupportedSDKVersions', (_message.Message,), {
  'DESCRIPTOR' : _SUPPORTEDSDKVERSIONS,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:temporal.version.v1.SupportedSDKVersions)
  })
_sym_db.RegisterMessage(SupportedSDKVersions)

WorkerVersionInfo = _reflection.GeneratedProtocolMessageType('WorkerVersionInfo', (_message.Message,), {
  'DESCRIPTOR' : _WORKERVERSIONINFO,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:temporal.version.v1.WorkerVersionInfo)
  })
_sym_db.RegisterMessage(WorkerVersionInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
