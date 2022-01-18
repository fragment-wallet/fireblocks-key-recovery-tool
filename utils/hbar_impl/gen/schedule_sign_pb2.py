# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: schedule_sign.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from utils.hbar_impl.gen import basic_types_pb2 as basic__types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='schedule_sign.proto',
  package='proto',
  syntax='proto3',
  serialized_options=b'\n\"com.hederahashgraph.api.proto.javaP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13schedule_sign.proto\x12\x05proto\x1a\x11\x62\x61sic_types.proto\"D\n\x1bScheduleSignTransactionBody\x12%\n\nscheduleID\x18\x01 \x01(\x0b\x32\x11.proto.ScheduleIDB&\n\"com.hederahashgraph.api.proto.javaP\x01\x62\x06proto3'
  ,
  dependencies=[basic__types__pb2.DESCRIPTOR,])




_SCHEDULESIGNTRANSACTIONBODY = _descriptor.Descriptor(
  name='ScheduleSignTransactionBody',
  full_name='proto.ScheduleSignTransactionBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='scheduleID', full_name='proto.ScheduleSignTransactionBody.scheduleID', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=49,
  serialized_end=117,
)

_SCHEDULESIGNTRANSACTIONBODY.fields_by_name['scheduleID'].message_type = basic__types__pb2._SCHEDULEID
DESCRIPTOR.message_types_by_name['ScheduleSignTransactionBody'] = _SCHEDULESIGNTRANSACTIONBODY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ScheduleSignTransactionBody = _reflection.GeneratedProtocolMessageType('ScheduleSignTransactionBody', (_message.Message,), {
  'DESCRIPTOR' : _SCHEDULESIGNTRANSACTIONBODY,
  '__module__' : 'schedule_sign_pb2'
  # @@protoc_insertion_point(class_scope:proto.ScheduleSignTransactionBody)
  })
_sym_db.RegisterMessage(ScheduleSignTransactionBody)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
