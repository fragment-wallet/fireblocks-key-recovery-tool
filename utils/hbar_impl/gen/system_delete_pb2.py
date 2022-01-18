# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: system_delete.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from utils.hbar_impl.gen import basic_types_pb2 as basic__types__pb2
from utils.hbar_impl.gen import timestamp_pb2 as timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='system_delete.proto',
  package='proto',
  syntax='proto3',
  serialized_options=b'\n\"com.hederahashgraph.api.proto.javaP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13system_delete.proto\x12\x05proto\x1a\x11\x62\x61sic_types.proto\x1a\x0ftimestamp.proto\"\x9e\x01\n\x1bSystemDeleteTransactionBody\x12\x1f\n\x06\x66ileID\x18\x01 \x01(\x0b\x32\r.proto.FileIDH\x00\x12\'\n\ncontractID\x18\x02 \x01(\x0b\x32\x11.proto.ContractIDH\x00\x12/\n\x0e\x65xpirationTime\x18\x03 \x01(\x0b\x32\x17.proto.TimestampSecondsB\x04\n\x02idB&\n\"com.hederahashgraph.api.proto.javaP\x01\x62\x06proto3'
  ,
  dependencies=[basic__types__pb2.DESCRIPTOR,timestamp__pb2.DESCRIPTOR,])




_SYSTEMDELETETRANSACTIONBODY = _descriptor.Descriptor(
  name='SystemDeleteTransactionBody',
  full_name='proto.SystemDeleteTransactionBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fileID', full_name='proto.SystemDeleteTransactionBody.fileID', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contractID', full_name='proto.SystemDeleteTransactionBody.contractID', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='expirationTime', full_name='proto.SystemDeleteTransactionBody.expirationTime', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
      name='id', full_name='proto.SystemDeleteTransactionBody.id',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=67,
  serialized_end=225,
)

_SYSTEMDELETETRANSACTIONBODY.fields_by_name['fileID'].message_type = basic__types__pb2._FILEID
_SYSTEMDELETETRANSACTIONBODY.fields_by_name['contractID'].message_type = basic__types__pb2._CONTRACTID
_SYSTEMDELETETRANSACTIONBODY.fields_by_name['expirationTime'].message_type = timestamp__pb2._TIMESTAMPSECONDS
_SYSTEMDELETETRANSACTIONBODY.oneofs_by_name['id'].fields.append(
  _SYSTEMDELETETRANSACTIONBODY.fields_by_name['fileID'])
_SYSTEMDELETETRANSACTIONBODY.fields_by_name['fileID'].containing_oneof = _SYSTEMDELETETRANSACTIONBODY.oneofs_by_name['id']
_SYSTEMDELETETRANSACTIONBODY.oneofs_by_name['id'].fields.append(
  _SYSTEMDELETETRANSACTIONBODY.fields_by_name['contractID'])
_SYSTEMDELETETRANSACTIONBODY.fields_by_name['contractID'].containing_oneof = _SYSTEMDELETETRANSACTIONBODY.oneofs_by_name['id']
DESCRIPTOR.message_types_by_name['SystemDeleteTransactionBody'] = _SYSTEMDELETETRANSACTIONBODY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SystemDeleteTransactionBody = _reflection.GeneratedProtocolMessageType('SystemDeleteTransactionBody', (_message.Message,), {
  'DESCRIPTOR' : _SYSTEMDELETETRANSACTIONBODY,
  '__module__' : 'system_delete_pb2'
  # @@protoc_insertion_point(class_scope:proto.SystemDeleteTransactionBody)
  })
_sym_db.RegisterMessage(SystemDeleteTransactionBody)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
