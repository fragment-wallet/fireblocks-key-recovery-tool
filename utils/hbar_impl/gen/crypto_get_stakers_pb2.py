# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: crypto_get_stakers.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from utils.hbar_impl.gen import basic_types_pb2 as basic__types__pb2
from utils.hbar_impl.gen import query_header_pb2 as query__header__pb2
from utils.hbar_impl.gen import response_header_pb2 as response__header__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='crypto_get_stakers.proto',
  package='proto',
  syntax='proto3',
  serialized_options=b'\n\"com.hederahashgraph.api.proto.javaP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18\x63rypto_get_stakers.proto\x12\x05proto\x1a\x11\x62\x61sic_types.proto\x1a\x12query_header.proto\x1a\x15response_header.proto\"`\n\x15\x43ryptoGetStakersQuery\x12\"\n\x06header\x18\x01 \x01(\x0b\x32\x12.proto.QueryHeader\x12#\n\taccountID\x18\x02 \x01(\x0b\x32\x10.proto.AccountID\"B\n\x0bProxyStaker\x12#\n\taccountID\x18\x01 \x01(\x0b\x32\x10.proto.AccountID\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x03\"_\n\x0f\x41llProxyStakers\x12#\n\taccountID\x18\x01 \x01(\x0b\x32\x10.proto.AccountID\x12\'\n\x0bproxyStaker\x18\x02 \x03(\x0b\x32\x12.proto.ProxyStaker\"j\n\x18\x43ryptoGetStakersResponse\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.proto.ResponseHeader\x12\'\n\x07stakers\x18\x03 \x01(\x0b\x32\x16.proto.AllProxyStakersB&\n\"com.hederahashgraph.api.proto.javaP\x01\x62\x06proto3'
  ,
  dependencies=[basic__types__pb2.DESCRIPTOR,query__header__pb2.DESCRIPTOR,response__header__pb2.DESCRIPTOR,])




_CRYPTOGETSTAKERSQUERY = _descriptor.Descriptor(
  name='CryptoGetStakersQuery',
  full_name='proto.CryptoGetStakersQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='proto.CryptoGetStakersQuery.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='accountID', full_name='proto.CryptoGetStakersQuery.accountID', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=97,
  serialized_end=193,
)


_PROXYSTAKER = _descriptor.Descriptor(
  name='ProxyStaker',
  full_name='proto.ProxyStaker',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='accountID', full_name='proto.ProxyStaker.accountID', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amount', full_name='proto.ProxyStaker.amount', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=195,
  serialized_end=261,
)


_ALLPROXYSTAKERS = _descriptor.Descriptor(
  name='AllProxyStakers',
  full_name='proto.AllProxyStakers',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='accountID', full_name='proto.AllProxyStakers.accountID', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='proxyStaker', full_name='proto.AllProxyStakers.proxyStaker', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=263,
  serialized_end=358,
)


_CRYPTOGETSTAKERSRESPONSE = _descriptor.Descriptor(
  name='CryptoGetStakersResponse',
  full_name='proto.CryptoGetStakersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='proto.CryptoGetStakersResponse.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stakers', full_name='proto.CryptoGetStakersResponse.stakers', index=1,
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
  ],
  serialized_start=360,
  serialized_end=466,
)

_CRYPTOGETSTAKERSQUERY.fields_by_name['header'].message_type = query__header__pb2._QUERYHEADER
_CRYPTOGETSTAKERSQUERY.fields_by_name['accountID'].message_type = basic__types__pb2._ACCOUNTID
_PROXYSTAKER.fields_by_name['accountID'].message_type = basic__types__pb2._ACCOUNTID
_ALLPROXYSTAKERS.fields_by_name['accountID'].message_type = basic__types__pb2._ACCOUNTID
_ALLPROXYSTAKERS.fields_by_name['proxyStaker'].message_type = _PROXYSTAKER
_CRYPTOGETSTAKERSRESPONSE.fields_by_name['header'].message_type = response__header__pb2._RESPONSEHEADER
_CRYPTOGETSTAKERSRESPONSE.fields_by_name['stakers'].message_type = _ALLPROXYSTAKERS
DESCRIPTOR.message_types_by_name['CryptoGetStakersQuery'] = _CRYPTOGETSTAKERSQUERY
DESCRIPTOR.message_types_by_name['ProxyStaker'] = _PROXYSTAKER
DESCRIPTOR.message_types_by_name['AllProxyStakers'] = _ALLPROXYSTAKERS
DESCRIPTOR.message_types_by_name['CryptoGetStakersResponse'] = _CRYPTOGETSTAKERSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CryptoGetStakersQuery = _reflection.GeneratedProtocolMessageType('CryptoGetStakersQuery', (_message.Message,), {
  'DESCRIPTOR' : _CRYPTOGETSTAKERSQUERY,
  '__module__' : 'crypto_get_stakers_pb2'
  # @@protoc_insertion_point(class_scope:proto.CryptoGetStakersQuery)
  })
_sym_db.RegisterMessage(CryptoGetStakersQuery)

ProxyStaker = _reflection.GeneratedProtocolMessageType('ProxyStaker', (_message.Message,), {
  'DESCRIPTOR' : _PROXYSTAKER,
  '__module__' : 'crypto_get_stakers_pb2'
  # @@protoc_insertion_point(class_scope:proto.ProxyStaker)
  })
_sym_db.RegisterMessage(ProxyStaker)

AllProxyStakers = _reflection.GeneratedProtocolMessageType('AllProxyStakers', (_message.Message,), {
  'DESCRIPTOR' : _ALLPROXYSTAKERS,
  '__module__' : 'crypto_get_stakers_pb2'
  # @@protoc_insertion_point(class_scope:proto.AllProxyStakers)
  })
_sym_db.RegisterMessage(AllProxyStakers)

CryptoGetStakersResponse = _reflection.GeneratedProtocolMessageType('CryptoGetStakersResponse', (_message.Message,), {
  'DESCRIPTOR' : _CRYPTOGETSTAKERSRESPONSE,
  '__module__' : 'crypto_get_stakers_pb2'
  # @@protoc_insertion_point(class_scope:proto.CryptoGetStakersResponse)
  })
_sym_db.RegisterMessage(CryptoGetStakersResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
