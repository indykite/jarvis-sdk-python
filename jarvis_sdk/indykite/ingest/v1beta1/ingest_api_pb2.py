# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: indykite/ingest/v1beta1/ingest_api.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from jarvis_sdk.indykite.objects.v1beta1 import struct_pb2 as indykite_dot_objects_dot_v1beta1_dot_struct__pb2
from jarvis_sdk.validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(indykite/ingest/v1beta1/ingest_api.proto\x12\x17indykite.ingest.v1beta1\x1a%indykite/objects/v1beta1/struct.proto\x1a\x17validate/validate.proto\"\xa1\x02\n\x14StreamRecordsRequest\x12P\n\x11mapping_config_id\x18\x01 \x01(\tB$\xfa\x42!r\x1f\x10\x16\x18\xfe\x01\x32\x18^[A-Za-z0-9-_:]{22,254}$R\x0fmappingConfigId\x12[\n\x06record\x18\x02 \x03(\x0b\x32\x39.indykite.ingest.v1beta1.StreamRecordsRequest.RecordEntryB\x08\xfa\x42\x05\x9a\x01\x02\x08\x01R\x06record\x1aZ\n\x0bRecordEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x35\n\x05value\x18\x02 \x01(\x0b\x32\x1f.indykite.objects.v1beta1.ValueR\x05value:\x02\x38\x01\"8\n\x15StreamRecordsResponse\x12\x1f\n\x0bnum_records\x18\x01 \x01(\rR\nnumRecords2}\n\tIngestAPI\x12p\n\rStreamRecords\x12-.indykite.ingest.v1beta1.StreamRecordsRequest\x1a..indykite.ingest.v1beta1.StreamRecordsResponse(\x01\x42\xab\x01\n\x1b\x63om.indykite.ingest.v1beta1B\x0eIngestApiProtoP\x01\xa2\x02\x03IIX\xaa\x02\x17Indykite.Ingest.V1beta1\xca\x02\x17Indykite\\Ingest\\V1beta1\xe2\x02#Indykite\\Ingest\\V1beta1\\GPBMetadata\xea\x02\x19Indykite::Ingest::V1beta1b\x06proto3')



_STREAMRECORDSREQUEST = DESCRIPTOR.message_types_by_name['StreamRecordsRequest']
_STREAMRECORDSREQUEST_RECORDENTRY = _STREAMRECORDSREQUEST.nested_types_by_name['RecordEntry']
_STREAMRECORDSRESPONSE = DESCRIPTOR.message_types_by_name['StreamRecordsResponse']
StreamRecordsRequest = _reflection.GeneratedProtocolMessageType('StreamRecordsRequest', (_message.Message,), {

  'RecordEntry' : _reflection.GeneratedProtocolMessageType('RecordEntry', (_message.Message,), {
    'DESCRIPTOR' : _STREAMRECORDSREQUEST_RECORDENTRY,
    '__module__' : 'indykite.ingest.v1beta1.ingest_api_pb2'
    # @@protoc_insertion_point(class_scope:indykite.ingest.v1beta1.StreamRecordsRequest.RecordEntry)
    })
  ,
  'DESCRIPTOR' : _STREAMRECORDSREQUEST,
  '__module__' : 'indykite.ingest.v1beta1.ingest_api_pb2'
  # @@protoc_insertion_point(class_scope:indykite.ingest.v1beta1.StreamRecordsRequest)
  })
_sym_db.RegisterMessage(StreamRecordsRequest)
_sym_db.RegisterMessage(StreamRecordsRequest.RecordEntry)

StreamRecordsResponse = _reflection.GeneratedProtocolMessageType('StreamRecordsResponse', (_message.Message,), {
  'DESCRIPTOR' : _STREAMRECORDSRESPONSE,
  '__module__' : 'indykite.ingest.v1beta1.ingest_api_pb2'
  # @@protoc_insertion_point(class_scope:indykite.ingest.v1beta1.StreamRecordsResponse)
  })
_sym_db.RegisterMessage(StreamRecordsResponse)

_INGESTAPI = DESCRIPTOR.services_by_name['IngestAPI']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033com.indykite.ingest.v1beta1B\016IngestApiProtoP\001\242\002\003IIX\252\002\027Indykite.Ingest.V1beta1\312\002\027Indykite\\Ingest\\V1beta1\342\002#Indykite\\Ingest\\V1beta1\\GPBMetadata\352\002\031Indykite::Ingest::V1beta1'
  _STREAMRECORDSREQUEST_RECORDENTRY._options = None
  _STREAMRECORDSREQUEST_RECORDENTRY._serialized_options = b'8\001'
  _STREAMRECORDSREQUEST.fields_by_name['mapping_config_id']._options = None
  _STREAMRECORDSREQUEST.fields_by_name['mapping_config_id']._serialized_options = b'\372B!r\037\020\026\030\376\0012\030^[A-Za-z0-9-_:]{22,254}$'
  _STREAMRECORDSREQUEST.fields_by_name['record']._options = None
  _STREAMRECORDSREQUEST.fields_by_name['record']._serialized_options = b'\372B\005\232\001\002\010\001'
  _STREAMRECORDSREQUEST._serialized_start=134
  _STREAMRECORDSREQUEST._serialized_end=423
  _STREAMRECORDSREQUEST_RECORDENTRY._serialized_start=333
  _STREAMRECORDSREQUEST_RECORDENTRY._serialized_end=423
  _STREAMRECORDSRESPONSE._serialized_start=425
  _STREAMRECORDSRESPONSE._serialized_end=481
  _INGESTAPI._serialized_start=483
  _INGESTAPI._serialized_end=608
# @@protoc_insertion_point(module_scope)
