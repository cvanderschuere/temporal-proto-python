# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: query/enum.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='query/enum.proto',
  package='query',
  syntax='proto3',
  serialized_options=b'\n\027io.temporal.proto.queryP\001Z#go.temporal.io/temporal-proto/query',
  serialized_pb=b'\n\x10query/enum.proto\x12\x05query*r\n\x0fQueryResultType\x12!\n\x1dQUERY_RESULT_TYPE_UNSPECIFIED\x10\x00\x12\x1e\n\x1aQUERY_RESULT_TYPE_ANSWERED\x10\x01\x12\x1c\n\x18QUERY_RESULT_TYPE_FAILED\x10\x02*\x95\x01\n\x14QueryRejectCondition\x12&\n\"QUERY_REJECT_CONDITION_UNSPECIFIED\x10\x00\x12#\n\x1fQUERY_REJECT_CONDITION_NOT_OPEN\x10\x01\x12\x30\n,QUERY_REJECT_CONDITION_NOT_COMPLETED_CLEANLY\x10\x02*\x8a\x01\n\x15QueryConsistencyLevel\x12\'\n#QUERY_CONSISTENCY_LEVEL_UNSPECIFIED\x10\x00\x12$\n QUERY_CONSISTENCY_LEVEL_EVENTUAL\x10\x01\x12\"\n\x1eQUERY_CONSISTENCY_LEVEL_STRONG\x10\x02\x42@\n\x17io.temporal.proto.queryP\x01Z#go.temporal.io/temporal-proto/queryb\x06proto3'
)

_QUERYRESULTTYPE = _descriptor.EnumDescriptor(
  name='QueryResultType',
  full_name='query.QueryResultType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='QUERY_RESULT_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUERY_RESULT_TYPE_ANSWERED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUERY_RESULT_TYPE_FAILED', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=27,
  serialized_end=141,
)
_sym_db.RegisterEnumDescriptor(_QUERYRESULTTYPE)

QueryResultType = enum_type_wrapper.EnumTypeWrapper(_QUERYRESULTTYPE)
_QUERYREJECTCONDITION = _descriptor.EnumDescriptor(
  name='QueryRejectCondition',
  full_name='query.QueryRejectCondition',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='QUERY_REJECT_CONDITION_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUERY_REJECT_CONDITION_NOT_OPEN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUERY_REJECT_CONDITION_NOT_COMPLETED_CLEANLY', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=144,
  serialized_end=293,
)
_sym_db.RegisterEnumDescriptor(_QUERYREJECTCONDITION)

QueryRejectCondition = enum_type_wrapper.EnumTypeWrapper(_QUERYREJECTCONDITION)
_QUERYCONSISTENCYLEVEL = _descriptor.EnumDescriptor(
  name='QueryConsistencyLevel',
  full_name='query.QueryConsistencyLevel',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='QUERY_CONSISTENCY_LEVEL_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUERY_CONSISTENCY_LEVEL_EVENTUAL', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUERY_CONSISTENCY_LEVEL_STRONG', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=296,
  serialized_end=434,
)
_sym_db.RegisterEnumDescriptor(_QUERYCONSISTENCYLEVEL)

QueryConsistencyLevel = enum_type_wrapper.EnumTypeWrapper(_QUERYCONSISTENCYLEVEL)
QUERY_RESULT_TYPE_UNSPECIFIED = 0
QUERY_RESULT_TYPE_ANSWERED = 1
QUERY_RESULT_TYPE_FAILED = 2
QUERY_REJECT_CONDITION_UNSPECIFIED = 0
QUERY_REJECT_CONDITION_NOT_OPEN = 1
QUERY_REJECT_CONDITION_NOT_COMPLETED_CLEANLY = 2
QUERY_CONSISTENCY_LEVEL_UNSPECIFIED = 0
QUERY_CONSISTENCY_LEVEL_EVENTUAL = 1
QUERY_CONSISTENCY_LEVEL_STRONG = 2


DESCRIPTOR.enum_types_by_name['QueryResultType'] = _QUERYRESULTTYPE
DESCRIPTOR.enum_types_by_name['QueryRejectCondition'] = _QUERYREJECTCONDITION
DESCRIPTOR.enum_types_by_name['QueryConsistencyLevel'] = _QUERYCONSISTENCYLEVEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
