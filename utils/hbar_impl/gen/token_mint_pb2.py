# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: token_mint.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from utils.hbar_impl.gen import basic_types_pb2 as basic__types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='token_mint.proto',
  package='proto',
  syntax='proto3',
  serialized_options=b'\n\"com.hederahashgraph.api.proto.javaP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10token_mint.proto\x12\x05proto\x1a\x11\x62\x61sic_types.proto\"[\n\x18TokenMintTransactionBody\x12\x1d\n\x05token\x18\x01 \x01(\x0b\x32\x0e.proto.TokenID\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x04\x12\x10\n\x08metadata\x18\x03 \x03(\x0c\x42&\n\"com.hederahashgraph.api.proto.javaP\x01\x62\x06proto3'
  ,
  dependencies=[basic__types__pb2.DESCRIPTOR,])




_TOKENMINTTRANSACTIONBODY = _descriptor.Descriptor(
  name='TokenMintTransactionBody',
  full_name='proto.TokenMintTransactionBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='proto.TokenMintTransactionBody.token', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amount', full_name='proto.TokenMintTransactionBody.amount', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='proto.TokenMintTransactionBody.metadata', index=2,
      number=3, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=46,
  serialized_end=137,
)

_TOKENMINTTRANSACTIONBODY.fields_by_name['token'].message_type = basic__types__pb2._TOKENID
DESCRIPTOR.message_types_by_name['TokenMintTransactionBody'] = _TOKENMINTTRANSACTIONBODY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TokenMintTransactionBody = _reflection.GeneratedProtocolMessageType('TokenMintTransactionBody', (_message.Message,), {
  'DESCRIPTOR' : _TOKENMINTTRANSACTIONBODY,
  '__module__' : 'token_mint_pb2'
  # @@protoc_insertion_point(class_scope:proto.TokenMintTransactionBody)
  })
_sym_db.RegisterMessage(TokenMintTransactionBody)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
