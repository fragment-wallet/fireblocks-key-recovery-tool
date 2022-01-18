# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transaction_get_fast_record.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from utils.hbar_impl.gen import transaction_record_pb2 as transaction__record__pb2
from utils.hbar_impl.gen import basic_types_pb2 as basic__types__pb2
from utils.hbar_impl.gen import query_header_pb2 as query__header__pb2
from utils.hbar_impl.gen import response_header_pb2 as response__header__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='transaction_get_fast_record.proto',
  package='proto',
  syntax='proto3',
  serialized_options=b'\n\"com.hederahashgraph.api.proto.javaP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!transaction_get_fast_record.proto\x12\x05proto\x1a\x18transaction_record.proto\x1a\x11\x62\x61sic_types.proto\x1a\x12query_header.proto\x1a\x15response_header.proto\"p\n\x1dTransactionGetFastRecordQuery\x12\"\n\x06header\x18\x01 \x01(\x0b\x32\x12.proto.QueryHeader\x12+\n\rtransactionID\x18\x02 \x01(\x0b\x32\x14.proto.TransactionID\"~\n TransactionGetFastRecordResponse\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.proto.ResponseHeader\x12\x33\n\x11transactionRecord\x18\x02 \x01(\x0b\x32\x18.proto.TransactionRecordB&\n\"com.hederahashgraph.api.proto.javaP\x01\x62\x06proto3'
  ,
  dependencies=[transaction__record__pb2.DESCRIPTOR,basic__types__pb2.DESCRIPTOR,query__header__pb2.DESCRIPTOR,response__header__pb2.DESCRIPTOR,])




_TRANSACTIONGETFASTRECORDQUERY = _descriptor.Descriptor(
  name='TransactionGetFastRecordQuery',
  full_name='proto.TransactionGetFastRecordQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='proto.TransactionGetFastRecordQuery.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='transactionID', full_name='proto.TransactionGetFastRecordQuery.transactionID', index=1,
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
  serialized_start=132,
  serialized_end=244,
)


_TRANSACTIONGETFASTRECORDRESPONSE = _descriptor.Descriptor(
  name='TransactionGetFastRecordResponse',
  full_name='proto.TransactionGetFastRecordResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='proto.TransactionGetFastRecordResponse.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='transactionRecord', full_name='proto.TransactionGetFastRecordResponse.transactionRecord', index=1,
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
  serialized_start=246,
  serialized_end=372,
)

_TRANSACTIONGETFASTRECORDQUERY.fields_by_name['header'].message_type = query__header__pb2._QUERYHEADER
_TRANSACTIONGETFASTRECORDQUERY.fields_by_name['transactionID'].message_type = basic__types__pb2._TRANSACTIONID
_TRANSACTIONGETFASTRECORDRESPONSE.fields_by_name['header'].message_type = response__header__pb2._RESPONSEHEADER
_TRANSACTIONGETFASTRECORDRESPONSE.fields_by_name['transactionRecord'].message_type = transaction__record__pb2._TRANSACTIONRECORD
DESCRIPTOR.message_types_by_name['TransactionGetFastRecordQuery'] = _TRANSACTIONGETFASTRECORDQUERY
DESCRIPTOR.message_types_by_name['TransactionGetFastRecordResponse'] = _TRANSACTIONGETFASTRECORDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TransactionGetFastRecordQuery = _reflection.GeneratedProtocolMessageType('TransactionGetFastRecordQuery', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONGETFASTRECORDQUERY,
  '__module__' : 'transaction_get_fast_record_pb2'
  # @@protoc_insertion_point(class_scope:proto.TransactionGetFastRecordQuery)
  })
_sym_db.RegisterMessage(TransactionGetFastRecordQuery)

TransactionGetFastRecordResponse = _reflection.GeneratedProtocolMessageType('TransactionGetFastRecordResponse', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONGETFASTRECORDRESPONSE,
  '__module__' : 'transaction_get_fast_record_pb2'
  # @@protoc_insertion_point(class_scope:proto.TransactionGetFastRecordResponse)
  })
_sym_db.RegisterMessage(TransactionGetFastRecordResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
