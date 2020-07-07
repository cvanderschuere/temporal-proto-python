# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: temporal/enums/v1/common.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='temporal/enums/v1/common.proto',
  package='temporal.enums.v1',
  syntax='proto3',
  serialized_options=b'\n\024io.temporal.enums.v1B\013CommonProtoP\001Z,go.temporal.io/temporal-proto/enums/v1;enums',
  serialized_pb=b'\n\x1etemporal/enums/v1/common.proto\x12\x11temporal.enums.v1*_\n\x0c\x45ncodingType\x12\x1d\n\x19\x45NCODING_TYPE_UNSPECIFIED\x10\x00\x12\x18\n\x14\x45NCODING_TYPE_PROTO3\x10\x01\x12\x16\n\x12\x45NCODING_TYPE_JSON\x10\x02*\xee\x01\n\x10IndexedValueType\x12\"\n\x1eINDEXED_VALUE_TYPE_UNSPECIFIED\x10\x00\x12\x1d\n\x19INDEXED_VALUE_TYPE_STRING\x10\x01\x12\x1e\n\x1aINDEXED_VALUE_TYPE_KEYWORD\x10\x02\x12\x1a\n\x16INDEXED_VALUE_TYPE_INT\x10\x03\x12\x1d\n\x19INDEXED_VALUE_TYPE_DOUBLE\x10\x04\x12\x1b\n\x17INDEXED_VALUE_TYPE_BOOL\x10\x05\x12\x1f\n\x1bINDEXED_VALUE_TYPE_DATETIME\x10\x06\x42S\n\x14io.temporal.enums.v1B\x0b\x43ommonProtoP\x01Z,go.temporal.io/temporal-proto/enums/v1;enumsb\x06proto3'
)

_ENCODINGTYPE = _descriptor.EnumDescriptor(
  name='EncodingType',
  full_name='temporal.enums.v1.EncodingType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ENCODING_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENCODING_TYPE_PROTO3', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENCODING_TYPE_JSON', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=53,
  serialized_end=148,
)
_sym_db.RegisterEnumDescriptor(_ENCODINGTYPE)

EncodingType = enum_type_wrapper.EnumTypeWrapper(_ENCODINGTYPE)
_INDEXEDVALUETYPE = _descriptor.EnumDescriptor(
  name='IndexedValueType',
  full_name='temporal.enums.v1.IndexedValueType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INDEXED_VALUE_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INDEXED_VALUE_TYPE_STRING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INDEXED_VALUE_TYPE_KEYWORD', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INDEXED_VALUE_TYPE_INT', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INDEXED_VALUE_TYPE_DOUBLE', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INDEXED_VALUE_TYPE_BOOL', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INDEXED_VALUE_TYPE_DATETIME', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=151,
  serialized_end=389,
)
_sym_db.RegisterEnumDescriptor(_INDEXEDVALUETYPE)

IndexedValueType = enum_type_wrapper.EnumTypeWrapper(_INDEXEDVALUETYPE)
ENCODING_TYPE_UNSPECIFIED = 0
ENCODING_TYPE_PROTO3 = 1
ENCODING_TYPE_JSON = 2
INDEXED_VALUE_TYPE_UNSPECIFIED = 0
INDEXED_VALUE_TYPE_STRING = 1
INDEXED_VALUE_TYPE_KEYWORD = 2
INDEXED_VALUE_TYPE_INT = 3
INDEXED_VALUE_TYPE_DOUBLE = 4
INDEXED_VALUE_TYPE_BOOL = 5
INDEXED_VALUE_TYPE_DATETIME = 6


DESCRIPTOR.enum_types_by_name['EncodingType'] = _ENCODINGTYPE
DESCRIPTOR.enum_types_by_name['IndexedValueType'] = _INDEXEDVALUETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
