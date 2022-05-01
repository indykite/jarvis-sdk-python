# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: indykite/identity/v1beta1/document.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from jarvis_sdk.indykite.objects.v1beta1 import struct_pb2 as indykite_dot_objects_dot_v1beta1_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(indykite/identity/v1beta1/document.proto\x12\x19indykite.identity.v1beta1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a%indykite/objects/v1beta1/struct.proto\"\xbd\x02\n\x08\x44ocument\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12G\n\x06\x66ields\x18\x02 \x03(\x0b\x32/.indykite.identity.v1beta1.Document.FieldsEntryR\x06\x66ields\x12;\n\x0b\x63reate_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\x12;\n\x0bupdate_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nupdateTime\x1aZ\n\x0b\x46ieldsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x35\n\x05value\x18\x02 \x01(\x0b\x32\x1f.indykite.objects.v1beta1.ValueR\x05value:\x02\x38\x01\"/\n\x0c\x44ocumentMask\x12\x1f\n\x0b\x66ield_paths\x18\x01 \x03(\tR\nfieldPaths\"y\n\x0cPrecondition\x12\x18\n\x06\x65xists\x18\x01 \x01(\x08H\x00R\x06\x65xists\x12=\n\x0bupdate_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00R\nupdateTimeB\x10\n\x0e\x63ondition_type\"\xc3\x03\n\x05Write\x12=\n\x06update\x18\x01 \x01(\x0b\x32#.indykite.identity.v1beta1.DocumentH\x00R\x06update\x12\x18\n\x06\x64\x65lete\x18\x02 \x01(\tH\x00R\x06\x64\x65lete\x12L\n\ttransform\x18\x06 \x01(\x0b\x32,.indykite.identity.v1beta1.DocumentTransformH\x00R\ttransform\x12H\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\'.indykite.identity.v1beta1.DocumentMaskR\nupdateMask\x12h\n\x11update_transforms\x18\x07 \x03(\x0b\x32;.indykite.identity.v1beta1.DocumentTransform.FieldTransformR\x10updateTransforms\x12R\n\x10\x63urrent_document\x18\x04 \x01(\x0b\x32\'.indykite.identity.v1beta1.PreconditionR\x0f\x63urrentDocumentB\x0b\n\toperation\"J\n\x0bWriteResult\x12;\n\x0bupdate_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nupdateTime\"\x96\x03\n\x11\x44ocumentTransform\x12\x1a\n\x08\x64ocument\x18\x01 \x01(\tR\x08\x64ocument\x12\x66\n\x10\x66ield_transforms\x18\x02 \x03(\x0b\x32;.indykite.identity.v1beta1.DocumentTransform.FieldTransformR\x0f\x66ieldTransforms\x1a\xfc\x01\n\x0e\x46ieldTransform\x12\x1d\n\nfield_path\x18\x01 \x01(\tR\tfieldPath\x12^\n\x17\x61ppend_missing_elements\x18\x06 \x01(\x0b\x32$.indykite.objects.v1beta1.ArrayValueH\x00R\x15\x61ppendMissingElements\x12Y\n\x15remove_all_from_array\x18\x07 \x01(\x0b\x32$.indykite.objects.v1beta1.ArrayValueH\x00R\x12removeAllFromArrayB\x10\n\x0etransform_typeB\xb4\x01\n\x1d\x63om.indykite.identity.v1beta1B\rDocumentProtoP\x01\xa2\x02\x03IIX\xaa\x02\x19Indykite.Identity.V1beta1\xca\x02\x19Indykite\\Identity\\V1beta1\xe2\x02%Indykite\\Identity\\V1beta1\\GPBMetadata\xea\x02\x1bIndykite::Identity::V1beta1b\x06proto3')



_DOCUMENT = DESCRIPTOR.message_types_by_name['Document']
_DOCUMENT_FIELDSENTRY = _DOCUMENT.nested_types_by_name['FieldsEntry']
_DOCUMENTMASK = DESCRIPTOR.message_types_by_name['DocumentMask']
_PRECONDITION = DESCRIPTOR.message_types_by_name['Precondition']
_WRITE = DESCRIPTOR.message_types_by_name['Write']
_WRITERESULT = DESCRIPTOR.message_types_by_name['WriteResult']
_DOCUMENTTRANSFORM = DESCRIPTOR.message_types_by_name['DocumentTransform']
_DOCUMENTTRANSFORM_FIELDTRANSFORM = _DOCUMENTTRANSFORM.nested_types_by_name['FieldTransform']
Document = _reflection.GeneratedProtocolMessageType('Document', (_message.Message,), {

  'FieldsEntry' : _reflection.GeneratedProtocolMessageType('FieldsEntry', (_message.Message,), {
    'DESCRIPTOR' : _DOCUMENT_FIELDSENTRY,
    '__module__' : 'indykite.identity.v1beta1.document_pb2'
    # @@protoc_insertion_point(class_scope:indykite.identity.v1beta1.Document.FieldsEntry)
    })
  ,
  'DESCRIPTOR' : _DOCUMENT,
  '__module__' : 'indykite.identity.v1beta1.document_pb2'
  # @@protoc_insertion_point(class_scope:indykite.identity.v1beta1.Document)
  })
_sym_db.RegisterMessage(Document)
_sym_db.RegisterMessage(Document.FieldsEntry)

DocumentMask = _reflection.GeneratedProtocolMessageType('DocumentMask', (_message.Message,), {
  'DESCRIPTOR' : _DOCUMENTMASK,
  '__module__' : 'indykite.identity.v1beta1.document_pb2'
  # @@protoc_insertion_point(class_scope:indykite.identity.v1beta1.DocumentMask)
  })
_sym_db.RegisterMessage(DocumentMask)

Precondition = _reflection.GeneratedProtocolMessageType('Precondition', (_message.Message,), {
  'DESCRIPTOR' : _PRECONDITION,
  '__module__' : 'indykite.identity.v1beta1.document_pb2'
  # @@protoc_insertion_point(class_scope:indykite.identity.v1beta1.Precondition)
  })
_sym_db.RegisterMessage(Precondition)

Write = _reflection.GeneratedProtocolMessageType('Write', (_message.Message,), {
  'DESCRIPTOR' : _WRITE,
  '__module__' : 'indykite.identity.v1beta1.document_pb2'
  # @@protoc_insertion_point(class_scope:indykite.identity.v1beta1.Write)
  })
_sym_db.RegisterMessage(Write)

WriteResult = _reflection.GeneratedProtocolMessageType('WriteResult', (_message.Message,), {
  'DESCRIPTOR' : _WRITERESULT,
  '__module__' : 'indykite.identity.v1beta1.document_pb2'
  # @@protoc_insertion_point(class_scope:indykite.identity.v1beta1.WriteResult)
  })
_sym_db.RegisterMessage(WriteResult)

DocumentTransform = _reflection.GeneratedProtocolMessageType('DocumentTransform', (_message.Message,), {

  'FieldTransform' : _reflection.GeneratedProtocolMessageType('FieldTransform', (_message.Message,), {
    'DESCRIPTOR' : _DOCUMENTTRANSFORM_FIELDTRANSFORM,
    '__module__' : 'indykite.identity.v1beta1.document_pb2'
    # @@protoc_insertion_point(class_scope:indykite.identity.v1beta1.DocumentTransform.FieldTransform)
    })
  ,
  'DESCRIPTOR' : _DOCUMENTTRANSFORM,
  '__module__' : 'indykite.identity.v1beta1.document_pb2'
  # @@protoc_insertion_point(class_scope:indykite.identity.v1beta1.DocumentTransform)
  })
_sym_db.RegisterMessage(DocumentTransform)
_sym_db.RegisterMessage(DocumentTransform.FieldTransform)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\035com.indykite.identity.v1beta1B\rDocumentProtoP\001\242\002\003IIX\252\002\031Indykite.Identity.V1beta1\312\002\031Indykite\\Identity\\V1beta1\342\002%Indykite\\Identity\\V1beta1\\GPBMetadata\352\002\033Indykite::Identity::V1beta1'
  _DOCUMENT_FIELDSENTRY._options = None
  _DOCUMENT_FIELDSENTRY._serialized_options = b'8\001'
  _DOCUMENT._serialized_start=144
  _DOCUMENT._serialized_end=461
  _DOCUMENT_FIELDSENTRY._serialized_start=371
  _DOCUMENT_FIELDSENTRY._serialized_end=461
  _DOCUMENTMASK._serialized_start=463
  _DOCUMENTMASK._serialized_end=510
  _PRECONDITION._serialized_start=512
  _PRECONDITION._serialized_end=633
  _WRITE._serialized_start=636
  _WRITE._serialized_end=1087
  _WRITERESULT._serialized_start=1089
  _WRITERESULT._serialized_end=1163
  _DOCUMENTTRANSFORM._serialized_start=1166
  _DOCUMENTTRANSFORM._serialized_end=1572
  _DOCUMENTTRANSFORM_FIELDTRANSFORM._serialized_start=1320
  _DOCUMENTTRANSFORM_FIELDTRANSFORM._serialized_end=1572
# @@protoc_insertion_point(module_scope)
