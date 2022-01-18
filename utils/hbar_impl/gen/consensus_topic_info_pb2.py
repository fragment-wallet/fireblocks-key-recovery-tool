# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: consensus_topic_info.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from utils.hbar_impl.gen import basic_types_pb2 as basic__types__pb2
from utils.hbar_impl.gen import duration_pb2 as duration__pb2
from utils.hbar_impl.gen import timestamp_pb2 as timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='consensus_topic_info.proto',
  package='proto',
  syntax='proto3',
  serialized_options=b'\n\"com.hederahashgraph.api.proto.javaP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1a\x63onsensus_topic_info.proto\x12\x05proto\x1a\x11\x62\x61sic_types.proto\x1a\x0e\x64uration.proto\x1a\x0ftimestamp.proto\"\x8c\x02\n\x12\x43onsensusTopicInfo\x12\x0c\n\x04memo\x18\x01 \x01(\t\x12\x13\n\x0brunningHash\x18\x02 \x01(\x0c\x12\x16\n\x0esequenceNumber\x18\x03 \x01(\x04\x12(\n\x0e\x65xpirationTime\x18\x04 \x01(\x0b\x32\x10.proto.Timestamp\x12\x1c\n\x08\x61\x64minKey\x18\x05 \x01(\x0b\x32\n.proto.Key\x12\x1d\n\tsubmitKey\x18\x06 \x01(\x0b\x32\n.proto.Key\x12(\n\x0f\x61utoRenewPeriod\x18\x07 \x01(\x0b\x32\x0f.proto.Duration\x12*\n\x10\x61utoRenewAccount\x18\x08 \x01(\x0b\x32\x10.proto.AccountIDB&\n\"com.hederahashgraph.api.proto.javaP\x01\x62\x06proto3'
  ,
  dependencies=[basic__types__pb2.DESCRIPTOR,duration__pb2.DESCRIPTOR,timestamp__pb2.DESCRIPTOR,])




_CONSENSUSTOPICINFO = _descriptor.Descriptor(
  name='ConsensusTopicInfo',
  full_name='proto.ConsensusTopicInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='memo', full_name='proto.ConsensusTopicInfo.memo', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='runningHash', full_name='proto.ConsensusTopicInfo.runningHash', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sequenceNumber', full_name='proto.ConsensusTopicInfo.sequenceNumber', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='expirationTime', full_name='proto.ConsensusTopicInfo.expirationTime', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='adminKey', full_name='proto.ConsensusTopicInfo.adminKey', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='submitKey', full_name='proto.ConsensusTopicInfo.submitKey', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='autoRenewPeriod', full_name='proto.ConsensusTopicInfo.autoRenewPeriod', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='autoRenewAccount', full_name='proto.ConsensusTopicInfo.autoRenewAccount', index=7,
      number=8, type=11, cpp_type=10, label=1,
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
  serialized_start=90,
  serialized_end=358,
)

_CONSENSUSTOPICINFO.fields_by_name['expirationTime'].message_type = timestamp__pb2._TIMESTAMP
_CONSENSUSTOPICINFO.fields_by_name['adminKey'].message_type = basic__types__pb2._KEY
_CONSENSUSTOPICINFO.fields_by_name['submitKey'].message_type = basic__types__pb2._KEY
_CONSENSUSTOPICINFO.fields_by_name['autoRenewPeriod'].message_type = duration__pb2._DURATION
_CONSENSUSTOPICINFO.fields_by_name['autoRenewAccount'].message_type = basic__types__pb2._ACCOUNTID
DESCRIPTOR.message_types_by_name['ConsensusTopicInfo'] = _CONSENSUSTOPICINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConsensusTopicInfo = _reflection.GeneratedProtocolMessageType('ConsensusTopicInfo', (_message.Message,), {
  'DESCRIPTOR' : _CONSENSUSTOPICINFO,
  '__module__' : 'consensus_topic_info_pb2'
  # @@protoc_insertion_point(class_scope:proto.ConsensusTopicInfo)
  })
_sym_db.RegisterMessage(ConsensusTopicInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
