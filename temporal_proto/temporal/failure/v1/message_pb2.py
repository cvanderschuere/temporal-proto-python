# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: temporal/failure/v1/message.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from temporal.common.v1 import message_pb2 as temporal_dot_common_dot_v1_dot_message__pb2
from temporal.enums.v1 import workflow_pb2 as temporal_dot_enums_dot_v1_dot_workflow__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='temporal/failure/v1/message.proto',
  package='temporal.failure.v1',
  syntax='proto3',
  serialized_options=b'\n\034io.temporal.proto.failure.v1B\014MessageProtoP\001Z0go.temporal.io/temporal-proto/failure/v1;failure',
  serialized_pb=b'\n!temporal/failure/v1/message.proto\x12\x13temporal.failure.v1\x1a temporal/common/v1/message.proto\x1a temporal/enums/v1/workflow.proto\"l\n\x16\x41pplicationFailureInfo\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x15\n\rnon_retryable\x18\x02 \x01(\x08\x12-\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32\x1c.temporal.common.v1.Payloads\"\x88\x01\n\x12TimeoutFailureInfo\x12\x34\n\x0ctimeout_type\x18\x01 \x01(\x0e\x32\x1e.temporal.enums.v1.TimeoutType\x12<\n\x16last_heartbeat_details\x18\x02 \x01(\x0b\x32\x1c.temporal.common.v1.Payloads\"D\n\x13\x43\x61nceledFailureInfo\x12-\n\x07\x64\x65tails\x18\x01 \x01(\x0b\x32\x1c.temporal.common.v1.Payloads\"\x17\n\x15TerminatedFailureInfo\"*\n\x11ServerFailureInfo\x12\x15\n\rnon_retryable\x18\x01 \x01(\x08\"X\n\x18ResetWorkflowFailureInfo\x12<\n\x16last_heartbeat_details\x18\x01 \x01(\x0b\x32\x1c.temporal.common.v1.Payloads\"\xe1\x01\n\x13\x41\x63tivityFailureInfo\x12\x1a\n\x12scheduled_event_id\x18\x01 \x01(\x03\x12\x18\n\x10started_event_id\x18\x02 \x01(\x03\x12\x10\n\x08identity\x18\x03 \x01(\t\x12\x37\n\ractivity_type\x18\x04 \x01(\x0b\x32 .temporal.common.v1.ActivityType\x12\x13\n\x0b\x61\x63tivity_id\x18\x05 \x01(\t\x12\x34\n\x0cretry_status\x18\x06 \x01(\x0e\x32\x1e.temporal.enums.v1.RetryStatus\"\x9e\x02\n!ChildWorkflowExecutionFailureInfo\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x41\n\x12workflow_execution\x18\x02 \x01(\x0b\x32%.temporal.common.v1.WorkflowExecution\x12\x37\n\rworkflow_type\x18\x03 \x01(\x0b\x32 .temporal.common.v1.WorkflowType\x12\x1a\n\x12initiated_event_id\x18\x04 \x01(\x03\x12\x18\n\x10started_event_id\x18\x05 \x01(\x03\x12\x34\n\x0cretry_status\x18\x06 \x01(\x0e\x32\x1e.temporal.enums.v1.RetryStatus\"\x81\x06\n\x07\x46\x61ilure\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0e\n\x06source\x18\x02 \x01(\t\x12\x13\n\x0bstack_trace\x18\x03 \x01(\t\x12+\n\x05\x63\x61use\x18\x04 \x01(\x0b\x32\x1c.temporal.failure.v1.Failure\x12O\n\x18\x61pplication_failure_info\x18\x05 \x01(\x0b\x32+.temporal.failure.v1.ApplicationFailureInfoH\x00\x12G\n\x14timeout_failure_info\x18\x06 \x01(\x0b\x32\'.temporal.failure.v1.TimeoutFailureInfoH\x00\x12I\n\x15\x63\x61nceled_failure_info\x18\x07 \x01(\x0b\x32(.temporal.failure.v1.CanceledFailureInfoH\x00\x12M\n\x17terminated_failure_info\x18\x08 \x01(\x0b\x32*.temporal.failure.v1.TerminatedFailureInfoH\x00\x12\x45\n\x13server_failure_info\x18\t \x01(\x0b\x32&.temporal.failure.v1.ServerFailureInfoH\x00\x12T\n\x1breset_workflow_failure_info\x18\n \x01(\x0b\x32-.temporal.failure.v1.ResetWorkflowFailureInfoH\x00\x12I\n\x15\x61\x63tivity_failure_info\x18\x0b \x01(\x0b\x32(.temporal.failure.v1.ActivityFailureInfoH\x00\x12g\n%child_workflow_execution_failure_info\x18\x0c \x01(\x0b\x32\x36.temporal.failure.v1.ChildWorkflowExecutionFailureInfoH\x00\x42\x0e\n\x0c\x66\x61ilure_infoB`\n\x1cio.temporal.proto.failure.v1B\x0cMessageProtoP\x01Z0go.temporal.io/temporal-proto/failure/v1;failureb\x06proto3'
  ,
  dependencies=[temporal_dot_common_dot_v1_dot_message__pb2.DESCRIPTOR,temporal_dot_enums_dot_v1_dot_workflow__pb2.DESCRIPTOR,])




_APPLICATIONFAILUREINFO = _descriptor.Descriptor(
  name='ApplicationFailureInfo',
  full_name='temporal.failure.v1.ApplicationFailureInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='temporal.failure.v1.ApplicationFailureInfo.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='non_retryable', full_name='temporal.failure.v1.ApplicationFailureInfo.non_retryable', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='details', full_name='temporal.failure.v1.ApplicationFailureInfo.details', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=126,
  serialized_end=234,
)


_TIMEOUTFAILUREINFO = _descriptor.Descriptor(
  name='TimeoutFailureInfo',
  full_name='temporal.failure.v1.TimeoutFailureInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeout_type', full_name='temporal.failure.v1.TimeoutFailureInfo.timeout_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_heartbeat_details', full_name='temporal.failure.v1.TimeoutFailureInfo.last_heartbeat_details', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=237,
  serialized_end=373,
)


_CANCELEDFAILUREINFO = _descriptor.Descriptor(
  name='CanceledFailureInfo',
  full_name='temporal.failure.v1.CanceledFailureInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='details', full_name='temporal.failure.v1.CanceledFailureInfo.details', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=375,
  serialized_end=443,
)


_TERMINATEDFAILUREINFO = _descriptor.Descriptor(
  name='TerminatedFailureInfo',
  full_name='temporal.failure.v1.TerminatedFailureInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=445,
  serialized_end=468,
)


_SERVERFAILUREINFO = _descriptor.Descriptor(
  name='ServerFailureInfo',
  full_name='temporal.failure.v1.ServerFailureInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='non_retryable', full_name='temporal.failure.v1.ServerFailureInfo.non_retryable', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=470,
  serialized_end=512,
)


_RESETWORKFLOWFAILUREINFO = _descriptor.Descriptor(
  name='ResetWorkflowFailureInfo',
  full_name='temporal.failure.v1.ResetWorkflowFailureInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='last_heartbeat_details', full_name='temporal.failure.v1.ResetWorkflowFailureInfo.last_heartbeat_details', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=514,
  serialized_end=602,
)


_ACTIVITYFAILUREINFO = _descriptor.Descriptor(
  name='ActivityFailureInfo',
  full_name='temporal.failure.v1.ActivityFailureInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scheduled_event_id', full_name='temporal.failure.v1.ActivityFailureInfo.scheduled_event_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='started_event_id', full_name='temporal.failure.v1.ActivityFailureInfo.started_event_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='identity', full_name='temporal.failure.v1.ActivityFailureInfo.identity', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='activity_type', full_name='temporal.failure.v1.ActivityFailureInfo.activity_type', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='activity_id', full_name='temporal.failure.v1.ActivityFailureInfo.activity_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='retry_status', full_name='temporal.failure.v1.ActivityFailureInfo.retry_status', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=605,
  serialized_end=830,
)


_CHILDWORKFLOWEXECUTIONFAILUREINFO = _descriptor.Descriptor(
  name='ChildWorkflowExecutionFailureInfo',
  full_name='temporal.failure.v1.ChildWorkflowExecutionFailureInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace', full_name='temporal.failure.v1.ChildWorkflowExecutionFailureInfo.namespace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workflow_execution', full_name='temporal.failure.v1.ChildWorkflowExecutionFailureInfo.workflow_execution', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workflow_type', full_name='temporal.failure.v1.ChildWorkflowExecutionFailureInfo.workflow_type', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='initiated_event_id', full_name='temporal.failure.v1.ChildWorkflowExecutionFailureInfo.initiated_event_id', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='started_event_id', full_name='temporal.failure.v1.ChildWorkflowExecutionFailureInfo.started_event_id', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='retry_status', full_name='temporal.failure.v1.ChildWorkflowExecutionFailureInfo.retry_status', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=833,
  serialized_end=1119,
)


_FAILURE = _descriptor.Descriptor(
  name='Failure',
  full_name='temporal.failure.v1.Failure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='temporal.failure.v1.Failure.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='temporal.failure.v1.Failure.source', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stack_trace', full_name='temporal.failure.v1.Failure.stack_trace', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cause', full_name='temporal.failure.v1.Failure.cause', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='application_failure_info', full_name='temporal.failure.v1.Failure.application_failure_info', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout_failure_info', full_name='temporal.failure.v1.Failure.timeout_failure_info', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='canceled_failure_info', full_name='temporal.failure.v1.Failure.canceled_failure_info', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='terminated_failure_info', full_name='temporal.failure.v1.Failure.terminated_failure_info', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='server_failure_info', full_name='temporal.failure.v1.Failure.server_failure_info', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reset_workflow_failure_info', full_name='temporal.failure.v1.Failure.reset_workflow_failure_info', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='activity_failure_info', full_name='temporal.failure.v1.Failure.activity_failure_info', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='child_workflow_execution_failure_info', full_name='temporal.failure.v1.Failure.child_workflow_execution_failure_info', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='failure_info', full_name='temporal.failure.v1.Failure.failure_info',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1122,
  serialized_end=1891,
)

_APPLICATIONFAILUREINFO.fields_by_name['details'].message_type = temporal_dot_common_dot_v1_dot_message__pb2._PAYLOADS
_TIMEOUTFAILUREINFO.fields_by_name['timeout_type'].enum_type = temporal_dot_enums_dot_v1_dot_workflow__pb2._TIMEOUTTYPE
_TIMEOUTFAILUREINFO.fields_by_name['last_heartbeat_details'].message_type = temporal_dot_common_dot_v1_dot_message__pb2._PAYLOADS
_CANCELEDFAILUREINFO.fields_by_name['details'].message_type = temporal_dot_common_dot_v1_dot_message__pb2._PAYLOADS
_RESETWORKFLOWFAILUREINFO.fields_by_name['last_heartbeat_details'].message_type = temporal_dot_common_dot_v1_dot_message__pb2._PAYLOADS
_ACTIVITYFAILUREINFO.fields_by_name['activity_type'].message_type = temporal_dot_common_dot_v1_dot_message__pb2._ACTIVITYTYPE
_ACTIVITYFAILUREINFO.fields_by_name['retry_status'].enum_type = temporal_dot_enums_dot_v1_dot_workflow__pb2._RETRYSTATUS
_CHILDWORKFLOWEXECUTIONFAILUREINFO.fields_by_name['workflow_execution'].message_type = temporal_dot_common_dot_v1_dot_message__pb2._WORKFLOWEXECUTION
_CHILDWORKFLOWEXECUTIONFAILUREINFO.fields_by_name['workflow_type'].message_type = temporal_dot_common_dot_v1_dot_message__pb2._WORKFLOWTYPE
_CHILDWORKFLOWEXECUTIONFAILUREINFO.fields_by_name['retry_status'].enum_type = temporal_dot_enums_dot_v1_dot_workflow__pb2._RETRYSTATUS
_FAILURE.fields_by_name['cause'].message_type = _FAILURE
_FAILURE.fields_by_name['application_failure_info'].message_type = _APPLICATIONFAILUREINFO
_FAILURE.fields_by_name['timeout_failure_info'].message_type = _TIMEOUTFAILUREINFO
_FAILURE.fields_by_name['canceled_failure_info'].message_type = _CANCELEDFAILUREINFO
_FAILURE.fields_by_name['terminated_failure_info'].message_type = _TERMINATEDFAILUREINFO
_FAILURE.fields_by_name['server_failure_info'].message_type = _SERVERFAILUREINFO
_FAILURE.fields_by_name['reset_workflow_failure_info'].message_type = _RESETWORKFLOWFAILUREINFO
_FAILURE.fields_by_name['activity_failure_info'].message_type = _ACTIVITYFAILUREINFO
_FAILURE.fields_by_name['child_workflow_execution_failure_info'].message_type = _CHILDWORKFLOWEXECUTIONFAILUREINFO
_FAILURE.oneofs_by_name['failure_info'].fields.append(
  _FAILURE.fields_by_name['application_failure_info'])
_FAILURE.fields_by_name['application_failure_info'].containing_oneof = _FAILURE.oneofs_by_name['failure_info']
_FAILURE.oneofs_by_name['failure_info'].fields.append(
  _FAILURE.fields_by_name['timeout_failure_info'])
_FAILURE.fields_by_name['timeout_failure_info'].containing_oneof = _FAILURE.oneofs_by_name['failure_info']
_FAILURE.oneofs_by_name['failure_info'].fields.append(
  _FAILURE.fields_by_name['canceled_failure_info'])
_FAILURE.fields_by_name['canceled_failure_info'].containing_oneof = _FAILURE.oneofs_by_name['failure_info']
_FAILURE.oneofs_by_name['failure_info'].fields.append(
  _FAILURE.fields_by_name['terminated_failure_info'])
_FAILURE.fields_by_name['terminated_failure_info'].containing_oneof = _FAILURE.oneofs_by_name['failure_info']
_FAILURE.oneofs_by_name['failure_info'].fields.append(
  _FAILURE.fields_by_name['server_failure_info'])
_FAILURE.fields_by_name['server_failure_info'].containing_oneof = _FAILURE.oneofs_by_name['failure_info']
_FAILURE.oneofs_by_name['failure_info'].fields.append(
  _FAILURE.fields_by_name['reset_workflow_failure_info'])
_FAILURE.fields_by_name['reset_workflow_failure_info'].containing_oneof = _FAILURE.oneofs_by_name['failure_info']
_FAILURE.oneofs_by_name['failure_info'].fields.append(
  _FAILURE.fields_by_name['activity_failure_info'])
_FAILURE.fields_by_name['activity_failure_info'].containing_oneof = _FAILURE.oneofs_by_name['failure_info']
_FAILURE.oneofs_by_name['failure_info'].fields.append(
  _FAILURE.fields_by_name['child_workflow_execution_failure_info'])
_FAILURE.fields_by_name['child_workflow_execution_failure_info'].containing_oneof = _FAILURE.oneofs_by_name['failure_info']
DESCRIPTOR.message_types_by_name['ApplicationFailureInfo'] = _APPLICATIONFAILUREINFO
DESCRIPTOR.message_types_by_name['TimeoutFailureInfo'] = _TIMEOUTFAILUREINFO
DESCRIPTOR.message_types_by_name['CanceledFailureInfo'] = _CANCELEDFAILUREINFO
DESCRIPTOR.message_types_by_name['TerminatedFailureInfo'] = _TERMINATEDFAILUREINFO
DESCRIPTOR.message_types_by_name['ServerFailureInfo'] = _SERVERFAILUREINFO
DESCRIPTOR.message_types_by_name['ResetWorkflowFailureInfo'] = _RESETWORKFLOWFAILUREINFO
DESCRIPTOR.message_types_by_name['ActivityFailureInfo'] = _ACTIVITYFAILUREINFO
DESCRIPTOR.message_types_by_name['ChildWorkflowExecutionFailureInfo'] = _CHILDWORKFLOWEXECUTIONFAILUREINFO
DESCRIPTOR.message_types_by_name['Failure'] = _FAILURE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ApplicationFailureInfo = _reflection.GeneratedProtocolMessageType('ApplicationFailureInfo', (_message.Message,), {
  'DESCRIPTOR' : _APPLICATIONFAILUREINFO,
  '__module__' : 'temporal.failure.v1.message_pb2'
  # @@protoc_insertion_point(class_scope:temporal.failure.v1.ApplicationFailureInfo)
  })
_sym_db.RegisterMessage(ApplicationFailureInfo)

TimeoutFailureInfo = _reflection.GeneratedProtocolMessageType('TimeoutFailureInfo', (_message.Message,), {
  'DESCRIPTOR' : _TIMEOUTFAILUREINFO,
  '__module__' : 'temporal.failure.v1.message_pb2'
  # @@protoc_insertion_point(class_scope:temporal.failure.v1.TimeoutFailureInfo)
  })
_sym_db.RegisterMessage(TimeoutFailureInfo)

CanceledFailureInfo = _reflection.GeneratedProtocolMessageType('CanceledFailureInfo', (_message.Message,), {
  'DESCRIPTOR' : _CANCELEDFAILUREINFO,
  '__module__' : 'temporal.failure.v1.message_pb2'
  # @@protoc_insertion_point(class_scope:temporal.failure.v1.CanceledFailureInfo)
  })
_sym_db.RegisterMessage(CanceledFailureInfo)

TerminatedFailureInfo = _reflection.GeneratedProtocolMessageType('TerminatedFailureInfo', (_message.Message,), {
  'DESCRIPTOR' : _TERMINATEDFAILUREINFO,
  '__module__' : 'temporal.failure.v1.message_pb2'
  # @@protoc_insertion_point(class_scope:temporal.failure.v1.TerminatedFailureInfo)
  })
_sym_db.RegisterMessage(TerminatedFailureInfo)

ServerFailureInfo = _reflection.GeneratedProtocolMessageType('ServerFailureInfo', (_message.Message,), {
  'DESCRIPTOR' : _SERVERFAILUREINFO,
  '__module__' : 'temporal.failure.v1.message_pb2'
  # @@protoc_insertion_point(class_scope:temporal.failure.v1.ServerFailureInfo)
  })
_sym_db.RegisterMessage(ServerFailureInfo)

ResetWorkflowFailureInfo = _reflection.GeneratedProtocolMessageType('ResetWorkflowFailureInfo', (_message.Message,), {
  'DESCRIPTOR' : _RESETWORKFLOWFAILUREINFO,
  '__module__' : 'temporal.failure.v1.message_pb2'
  # @@protoc_insertion_point(class_scope:temporal.failure.v1.ResetWorkflowFailureInfo)
  })
_sym_db.RegisterMessage(ResetWorkflowFailureInfo)

ActivityFailureInfo = _reflection.GeneratedProtocolMessageType('ActivityFailureInfo', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVITYFAILUREINFO,
  '__module__' : 'temporal.failure.v1.message_pb2'
  # @@protoc_insertion_point(class_scope:temporal.failure.v1.ActivityFailureInfo)
  })
_sym_db.RegisterMessage(ActivityFailureInfo)

ChildWorkflowExecutionFailureInfo = _reflection.GeneratedProtocolMessageType('ChildWorkflowExecutionFailureInfo', (_message.Message,), {
  'DESCRIPTOR' : _CHILDWORKFLOWEXECUTIONFAILUREINFO,
  '__module__' : 'temporal.failure.v1.message_pb2'
  # @@protoc_insertion_point(class_scope:temporal.failure.v1.ChildWorkflowExecutionFailureInfo)
  })
_sym_db.RegisterMessage(ChildWorkflowExecutionFailureInfo)

Failure = _reflection.GeneratedProtocolMessageType('Failure', (_message.Message,), {
  'DESCRIPTOR' : _FAILURE,
  '__module__' : 'temporal.failure.v1.message_pb2'
  # @@protoc_insertion_point(class_scope:temporal.failure.v1.Failure)
  })
_sym_db.RegisterMessage(Failure)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
