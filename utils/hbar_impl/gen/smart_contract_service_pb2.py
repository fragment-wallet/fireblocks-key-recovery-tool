# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: smart_contract_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from utils.hbar_impl.gen import transaction_response_pb2 as transaction__response__pb2
from utils.hbar_impl.gen import query_pb2 as query__pb2
from utils.hbar_impl.gen import response_pb2 as response__pb2
from utils.hbar_impl.gen import transaction_pb2 as transaction__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='smart_contract_service.proto',
  package='proto',
  syntax='proto3',
  serialized_options=b'\n&com.hederahashgraph.service.proto.java',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1csmart_contract_service.proto\x12\x05proto\x1a\x1atransaction_response.proto\x1a\x0bquery.proto\x1a\x0eresponse.proto\x1a\x11transaction.proto2\xb7\x05\n\x14SmartContractService\x12@\n\x0e\x63reateContract\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponse\x12@\n\x0eupdateContract\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponse\x12\x44\n\x12\x63ontractCallMethod\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponse\x12\x30\n\x0fgetContractInfo\x12\x0c.proto.Query\x1a\x0f.proto.Response\x12\x38\n\x17\x63ontractCallLocalMethod\x12\x0c.proto.Query\x1a\x0f.proto.Response\x12\x34\n\x13\x43ontractGetBytecode\x12\x0c.proto.Query\x1a\x0f.proto.Response\x12\x30\n\x0fgetBySolidityID\x12\x0c.proto.Query\x1a\x0f.proto.Response\x12=\n\x17getTxRecordByContractID\x12\x0c.proto.Query\x1a\x0f.proto.Response\"\x03\x88\x02\x01\x12@\n\x0e\x64\x65leteContract\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponse\x12>\n\x0csystemDelete\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponse\x12@\n\x0esystemUndelete\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponseB(\n&com.hederahashgraph.service.proto.javab\x06proto3'
  ,
  dependencies=[transaction__response__pb2.DESCRIPTOR,query__pb2.DESCRIPTOR,response__pb2.DESCRIPTOR,transaction__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_SMARTCONTRACTSERVICE = _descriptor.ServiceDescriptor(
  name='SmartContractService',
  full_name='proto.SmartContractService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=116,
  serialized_end=811,
  methods=[
  _descriptor.MethodDescriptor(
    name='createContract',
    full_name='proto.SmartContractService.createContract',
    index=0,
    containing_service=None,
    input_type=transaction__pb2._TRANSACTION,
    output_type=transaction__response__pb2._TRANSACTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='updateContract',
    full_name='proto.SmartContractService.updateContract',
    index=1,
    containing_service=None,
    input_type=transaction__pb2._TRANSACTION,
    output_type=transaction__response__pb2._TRANSACTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='contractCallMethod',
    full_name='proto.SmartContractService.contractCallMethod',
    index=2,
    containing_service=None,
    input_type=transaction__pb2._TRANSACTION,
    output_type=transaction__response__pb2._TRANSACTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getContractInfo',
    full_name='proto.SmartContractService.getContractInfo',
    index=3,
    containing_service=None,
    input_type=query__pb2._QUERY,
    output_type=response__pb2._RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='contractCallLocalMethod',
    full_name='proto.SmartContractService.contractCallLocalMethod',
    index=4,
    containing_service=None,
    input_type=query__pb2._QUERY,
    output_type=response__pb2._RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ContractGetBytecode',
    full_name='proto.SmartContractService.ContractGetBytecode',
    index=5,
    containing_service=None,
    input_type=query__pb2._QUERY,
    output_type=response__pb2._RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getBySolidityID',
    full_name='proto.SmartContractService.getBySolidityID',
    index=6,
    containing_service=None,
    input_type=query__pb2._QUERY,
    output_type=response__pb2._RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getTxRecordByContractID',
    full_name='proto.SmartContractService.getTxRecordByContractID',
    index=7,
    containing_service=None,
    input_type=query__pb2._QUERY,
    output_type=response__pb2._RESPONSE,
    serialized_options=b'\210\002\001',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='deleteContract',
    full_name='proto.SmartContractService.deleteContract',
    index=8,
    containing_service=None,
    input_type=transaction__pb2._TRANSACTION,
    output_type=transaction__response__pb2._TRANSACTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='systemDelete',
    full_name='proto.SmartContractService.systemDelete',
    index=9,
    containing_service=None,
    input_type=transaction__pb2._TRANSACTION,
    output_type=transaction__response__pb2._TRANSACTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='systemUndelete',
    full_name='proto.SmartContractService.systemUndelete',
    index=10,
    containing_service=None,
    input_type=transaction__pb2._TRANSACTION,
    output_type=transaction__response__pb2._TRANSACTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SMARTCONTRACTSERVICE)

DESCRIPTOR.services_by_name['SmartContractService'] = _SMARTCONTRACTSERVICE

# @@protoc_insertion_point(module_scope)
