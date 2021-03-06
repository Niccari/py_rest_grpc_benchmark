# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='api.proto',
  package='niccari_test',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tapi.proto\x12\x0cniccari_test\"\x0e\n\x0c\x45mptyRequest\"\x0f\n\rEmptyResponse\"#\n\x07\x43ontent\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04hoge\x18\x02 \x01(\t\"\x1f\n\x0e\x43ontentRequest\x12\r\n\x05\x63ount\x18\x01 \x01(\x05\"6\n\x0f\x43ontentResponse\x12#\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x15.niccari_test.Content\"\x1b\n\x0bTextRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\"\x1d\n\x0cImageRequest\x12\r\n\x05image\x18\x01 \x01(\x0c\x32\xbc\x03\n\x03\x41pi\x12\x45\n\x08GetEmpty\x12\x1a.niccari_test.EmptyRequest\x1a\x1b.niccari_test.EmptyResponse\"\x00\x12K\n\nGetContent\x12\x1c.niccari_test.ContentRequest\x1a\x1d.niccari_test.ContentResponse\"\x00\x12\x46\n\tPostEmpty\x12\x1a.niccari_test.EmptyRequest\x1a\x1b.niccari_test.EmptyResponse\"\x00\x12\x43\n\x0bPostContent\x12\x15.niccari_test.Content\x1a\x1b.niccari_test.EmptyResponse\"\x00\x12H\n\nUploadText\x12\x19.niccari_test.TextRequest\x1a\x1b.niccari_test.EmptyResponse\"\x00(\x01\x12J\n\x0bUploadImage\x12\x1a.niccari_test.ImageRequest\x1a\x1b.niccari_test.EmptyResponse\"\x00(\x01\x62\x06proto3'
)




_EMPTYREQUEST = _descriptor.Descriptor(
  name='EmptyRequest',
  full_name='niccari_test.EmptyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=27,
  serialized_end=41,
)


_EMPTYRESPONSE = _descriptor.Descriptor(
  name='EmptyResponse',
  full_name='niccari_test.EmptyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=43,
  serialized_end=58,
)


_CONTENT = _descriptor.Descriptor(
  name='Content',
  full_name='niccari_test.Content',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='niccari_test.Content.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hoge', full_name='niccari_test.Content.hoge', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=60,
  serialized_end=95,
)


_CONTENTREQUEST = _descriptor.Descriptor(
  name='ContentRequest',
  full_name='niccari_test.ContentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='count', full_name='niccari_test.ContentRequest.count', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=97,
  serialized_end=128,
)


_CONTENTRESPONSE = _descriptor.Descriptor(
  name='ContentResponse',
  full_name='niccari_test.ContentResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='niccari_test.ContentResponse.data', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=130,
  serialized_end=184,
)


_TEXTREQUEST = _descriptor.Descriptor(
  name='TextRequest',
  full_name='niccari_test.TextRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='niccari_test.TextRequest.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=186,
  serialized_end=213,
)


_IMAGEREQUEST = _descriptor.Descriptor(
  name='ImageRequest',
  full_name='niccari_test.ImageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='image', full_name='niccari_test.ImageRequest.image', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=215,
  serialized_end=244,
)

_CONTENTRESPONSE.fields_by_name['data'].message_type = _CONTENT
DESCRIPTOR.message_types_by_name['EmptyRequest'] = _EMPTYREQUEST
DESCRIPTOR.message_types_by_name['EmptyResponse'] = _EMPTYRESPONSE
DESCRIPTOR.message_types_by_name['Content'] = _CONTENT
DESCRIPTOR.message_types_by_name['ContentRequest'] = _CONTENTREQUEST
DESCRIPTOR.message_types_by_name['ContentResponse'] = _CONTENTRESPONSE
DESCRIPTOR.message_types_by_name['TextRequest'] = _TEXTREQUEST
DESCRIPTOR.message_types_by_name['ImageRequest'] = _IMAGEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EmptyRequest = _reflection.GeneratedProtocolMessageType('EmptyRequest', (_message.Message,), {
  'DESCRIPTOR' : _EMPTYREQUEST,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:niccari_test.EmptyRequest)
  })
_sym_db.RegisterMessage(EmptyRequest)

EmptyResponse = _reflection.GeneratedProtocolMessageType('EmptyResponse', (_message.Message,), {
  'DESCRIPTOR' : _EMPTYRESPONSE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:niccari_test.EmptyResponse)
  })
_sym_db.RegisterMessage(EmptyResponse)

Content = _reflection.GeneratedProtocolMessageType('Content', (_message.Message,), {
  'DESCRIPTOR' : _CONTENT,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:niccari_test.Content)
  })
_sym_db.RegisterMessage(Content)

ContentRequest = _reflection.GeneratedProtocolMessageType('ContentRequest', (_message.Message,), {
  'DESCRIPTOR' : _CONTENTREQUEST,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:niccari_test.ContentRequest)
  })
_sym_db.RegisterMessage(ContentRequest)

ContentResponse = _reflection.GeneratedProtocolMessageType('ContentResponse', (_message.Message,), {
  'DESCRIPTOR' : _CONTENTRESPONSE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:niccari_test.ContentResponse)
  })
_sym_db.RegisterMessage(ContentResponse)

TextRequest = _reflection.GeneratedProtocolMessageType('TextRequest', (_message.Message,), {
  'DESCRIPTOR' : _TEXTREQUEST,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:niccari_test.TextRequest)
  })
_sym_db.RegisterMessage(TextRequest)

ImageRequest = _reflection.GeneratedProtocolMessageType('ImageRequest', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEREQUEST,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:niccari_test.ImageRequest)
  })
_sym_db.RegisterMessage(ImageRequest)



_API = _descriptor.ServiceDescriptor(
  name='Api',
  full_name='niccari_test.Api',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=247,
  serialized_end=691,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetEmpty',
    full_name='niccari_test.Api.GetEmpty',
    index=0,
    containing_service=None,
    input_type=_EMPTYREQUEST,
    output_type=_EMPTYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetContent',
    full_name='niccari_test.Api.GetContent',
    index=1,
    containing_service=None,
    input_type=_CONTENTREQUEST,
    output_type=_CONTENTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='PostEmpty',
    full_name='niccari_test.Api.PostEmpty',
    index=2,
    containing_service=None,
    input_type=_EMPTYREQUEST,
    output_type=_EMPTYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='PostContent',
    full_name='niccari_test.Api.PostContent',
    index=3,
    containing_service=None,
    input_type=_CONTENT,
    output_type=_EMPTYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UploadText',
    full_name='niccari_test.Api.UploadText',
    index=4,
    containing_service=None,
    input_type=_TEXTREQUEST,
    output_type=_EMPTYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UploadImage',
    full_name='niccari_test.Api.UploadImage',
    index=5,
    containing_service=None,
    input_type=_IMAGEREQUEST,
    output_type=_EMPTYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_API)

DESCRIPTOR.services_by_name['Api'] = _API

# @@protoc_insertion_point(module_scope)
