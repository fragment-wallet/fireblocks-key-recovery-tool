# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: crypto_update.proto
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
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='crypto_update.proto',
  package='proto',
  syntax='proto3',
  serialized_options=b'\n\"com.hederahashgraph.api.proto.javaP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13\x63rypto_update.proto\x12\x05proto\x1a\x11\x62\x61sic_types.proto\x1a\x0e\x64uration.proto\x1a\x0ftimestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\x87\x06\n\x1b\x43ryptoUpdateTransactionBody\x12+\n\x11\x61\x63\x63ountIDToUpdate\x18\x02 \x01(\x0b\x32\x10.proto.AccountID\x12\x17\n\x03key\x18\x03 \x01(\x0b\x32\n.proto.Key\x12(\n\x0eproxyAccountID\x18\x04 \x01(\x0b\x32\x10.proto.AccountID\x12\x19\n\rproxyFraction\x18\x05 \x01(\x05\x42\x02\x18\x01\x12!\n\x13sendRecordThreshold\x18\x06 \x01(\x04\x42\x02\x18\x01H\x00\x12\x46\n\x1asendRecordThresholdWrapper\x18\x0b \x01(\x0b\x32\x1c.google.protobuf.UInt64ValueB\x02\x18\x01H\x00\x12$\n\x16receiveRecordThreshold\x18\x07 \x01(\x04\x42\x02\x18\x01H\x01\x12I\n\x1dreceiveRecordThresholdWrapper\x18\x0c \x01(\x0b\x32\x1c.google.protobuf.UInt64ValueB\x02\x18\x01H\x01\x12(\n\x0f\x61utoRenewPeriod\x18\x08 \x01(\x0b\x32\x0f.proto.Duration\x12(\n\x0e\x65xpirationTime\x18\t \x01(\x0b\x32\x10.proto.Timestamp\x12!\n\x13receiverSigRequired\x18\n \x01(\x08\x42\x02\x18\x01H\x02\x12@\n\x1areceiverSigRequiredWrapper\x18\r \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\x02\x12*\n\x04memo\x18\x0e \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x45\n max_automatic_token_associations\x18\x0f \x01(\x0b\x32\x1b.google.protobuf.Int32ValueB\x1a\n\x18sendRecordThresholdFieldB\x1d\n\x1breceiveRecordThresholdFieldB\x1a\n\x18receiverSigRequiredFieldB&\n\"com.hederahashgraph.api.proto.javaP\x01\x62\x06proto3'
  ,
  dependencies=[basic__types__pb2.DESCRIPTOR,duration__pb2.DESCRIPTOR,timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_CRYPTOUPDATETRANSACTIONBODY = _descriptor.Descriptor(
  name='CryptoUpdateTransactionBody',
  full_name='proto.CryptoUpdateTransactionBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='accountIDToUpdate', full_name='proto.CryptoUpdateTransactionBody.accountIDToUpdate', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='key', full_name='proto.CryptoUpdateTransactionBody.key', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='proxyAccountID', full_name='proto.CryptoUpdateTransactionBody.proxyAccountID', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='proxyFraction', full_name='proto.CryptoUpdateTransactionBody.proxyFraction', index=3,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sendRecordThreshold', full_name='proto.CryptoUpdateTransactionBody.sendRecordThreshold', index=4,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sendRecordThresholdWrapper', full_name='proto.CryptoUpdateTransactionBody.sendRecordThresholdWrapper', index=5,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='receiveRecordThreshold', full_name='proto.CryptoUpdateTransactionBody.receiveRecordThreshold', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='receiveRecordThresholdWrapper', full_name='proto.CryptoUpdateTransactionBody.receiveRecordThresholdWrapper', index=7,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='autoRenewPeriod', full_name='proto.CryptoUpdateTransactionBody.autoRenewPeriod', index=8,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='expirationTime', full_name='proto.CryptoUpdateTransactionBody.expirationTime', index=9,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='receiverSigRequired', full_name='proto.CryptoUpdateTransactionBody.receiverSigRequired', index=10,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='receiverSigRequiredWrapper', full_name='proto.CryptoUpdateTransactionBody.receiverSigRequiredWrapper', index=11,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='memo', full_name='proto.CryptoUpdateTransactionBody.memo', index=12,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_automatic_token_associations', full_name='proto.CryptoUpdateTransactionBody.max_automatic_token_associations', index=13,
      number=15, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='sendRecordThresholdField', full_name='proto.CryptoUpdateTransactionBody.sendRecordThresholdField',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='receiveRecordThresholdField', full_name='proto.CryptoUpdateTransactionBody.receiveRecordThresholdField',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='receiverSigRequiredField', full_name='proto.CryptoUpdateTransactionBody.receiverSigRequiredField',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=115,
  serialized_end=890,
)

_CRYPTOUPDATETRANSACTIONBODY.fields_by_name['accountIDToUpdate'].message_type = basic__types__pb2._ACCOUNTID
_CRYPTOUPDATETRANSACTIONBODY.fields_by_name['key'].message_type = basic__types__pb2._KEY
_CRYPTOUPDATETRANSACTIONBODY.fields_by_name['proxyAccountID'].message_type = basic__types__pb2._ACCOUNTID
_CRYPTOUPDATETRANSACTIONBODY.fields_by_name['sendRecordThresholdWrapper'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT64VALUE
_CRYPTOUPDATETRANSACTIONBODY.fields_by_name['receiveRecordThresholdWrapper'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT64VALUE
_CRYPTOUPDATETRANSACTIONBODY.fields_by_name['autoRenewPeriod'].message_type = duration__pb2._DURATION
_CRYPTOUPDATETRANSACTIONBODY.fields_by_name['expirationTime'].message_type = timestamp__pb2._TIMESTAMP
_CRYPTOUPDATETRANSACTIONBODY.fields_by_name['receiverSigRequiredWrapper'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_CRYPTOUPDATETRANSACTIONBODY.fields_by_name['memo'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CRYPTOUPDATETRANSACTIONBODY.fields_by_name['max_automatic_token_associations'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT32VALUE
_CRYPTOUPDATETRANSACTIONBODY.oneofs_by_name['sendRecordThresholdField'].fields.append(
  _CRYPTOUPDATETRANSACTIONBODY.fields_by_name['sendRecordThreshold'])
_CRYPTOUPDATETRANSACTIONBODY.fields_by_name['sendRecordThreshold'].containing_oneof = _CRYPTOUPDATETRANSACTIONBODY.oneofs_by_name['sendRecordThresholdField']
_CRYPTOUPDATETRANSACTIONBODY.oneofs_by_name['sendRecordThresholdField'].fields.append(
  _CRYPTOUPDATETRANSACTIONBODY.fields_by_name['sendRecordThresholdWrapper'])
_CRYPTOUPDATETRANSACTIONBODY.fields_by_name['sendRecordThresholdWrapper'].containing_oneof = _CRYPTOUPDATETRANSACTIONBODY.oneofs_by_name['sendRecordThresholdField']
_CRYPTOUPDATETRANSACTIONBODY.oneofs_by_name['receiveRecordThresholdField'].fields.append(
  _CRYPTOUPDATETRANSACTIONBODY.fields_by_name['receiveRecordThreshold'])
_CRYPTOUPDATETRANSACTIONBODY.fields_by_name['receiveRecordThreshold'].containing_oneof = _CRYPTOUPDATETRANSACTIONBODY.oneofs_by_name['receiveRecordThresholdField']
_CRYPTOUPDATETRANSACTIONBODY.oneofs_by_name['receiveRecordThresholdField'].fields.append(
  _CRYPTOUPDATETRANSACTIONBODY.fields_by_name['receiveRecordThresholdWrapper'])
_CRYPTOUPDATETRANSACTIONBODY.fields_by_name['receiveRecordThresholdWrapper'].containing_oneof = _CRYPTOUPDATETRANSACTIONBODY.oneofs_by_name['receiveRecordThresholdField']
_CRYPTOUPDATETRANSACTIONBODY.oneofs_by_name['receiverSigRequiredField'].fields.append(
  _CRYPTOUPDATETRANSACTIONBODY.fields_by_name['receiverSigRequired'])
_CRYPTOUPDATETRANSACTIONBODY.fields_by_name['receiverSigRequired'].containing_oneof = _CRYPTOUPDATETRANSACTIONBODY.oneofs_by_name['receiverSigRequiredField']
_CRYPTOUPDATETRANSACTIONBODY.oneofs_by_name['receiverSigRequiredField'].fields.append(
  _CRYPTOUPDATETRANSACTIONBODY.fields_by_name['receiverSigRequiredWrapper'])
_CRYPTOUPDATETRANSACTIONBODY.fields_by_name['receiverSigRequiredWrapper'].containing_oneof = _CRYPTOUPDATETRANSACTIONBODY.oneofs_by_name['receiverSigRequiredField']
DESCRIPTOR.message_types_by_name['CryptoUpdateTransactionBody'] = _CRYPTOUPDATETRANSACTIONBODY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CryptoUpdateTransactionBody = _reflection.GeneratedProtocolMessageType('CryptoUpdateTransactionBody', (_message.Message,), {
  'DESCRIPTOR' : _CRYPTOUPDATETRANSACTIONBODY,
  '__module__' : 'crypto_update_pb2'
  # @@protoc_insertion_point(class_scope:proto.CryptoUpdateTransactionBody)
  })
_sym_db.RegisterMessage(CryptoUpdateTransactionBody)


DESCRIPTOR._options = None
_CRYPTOUPDATETRANSACTIONBODY.fields_by_name['proxyFraction']._options = None
_CRYPTOUPDATETRANSACTIONBODY.fields_by_name['sendRecordThreshold']._options = None
_CRYPTOUPDATETRANSACTIONBODY.fields_by_name['sendRecordThresholdWrapper']._options = None
_CRYPTOUPDATETRANSACTIONBODY.fields_by_name['receiveRecordThreshold']._options = None
_CRYPTOUPDATETRANSACTIONBODY.fields_by_name['receiveRecordThresholdWrapper']._options = None
_CRYPTOUPDATETRANSACTIONBODY.fields_by_name['receiverSigRequired']._options = None
# @@protoc_insertion_point(module_scope)
