# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='service.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rservice.proto\"2\n\x0f\x45quationMessage\x12\t\n\x01\x41\x18\x01 \x01(\x01\x12\t\n\x01\x42\x18\x02 \x01(\x01\x12\t\n\x01\x43\x18\x03 \x01(\x01\"O\n\x19\x45quationCalculatedMessage\x12\n\n\x02x1\x18\x01 \x01(\x01\x12\n\n\x02x2\x18\x02 \x01(\x01\x12\x1a\n\x12realSolutionExists\x18\x03 \x01(\x08\x32\x45\n\nCalculator\x12\x37\n\x05Solve\x12\x10.EquationMessage\x1a\x1a.EquationCalculatedMessage\"\x00\x62\x06proto3'
)




_EQUATIONMESSAGE = _descriptor.Descriptor(
  name='EquationMessage',
  full_name='EquationMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='A', full_name='EquationMessage.A', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='B', full_name='EquationMessage.B', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='C', full_name='EquationMessage.C', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=17,
  serialized_end=67,
)


_EQUATIONCALCULATEDMESSAGE = _descriptor.Descriptor(
  name='EquationCalculatedMessage',
  full_name='EquationCalculatedMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x1', full_name='EquationCalculatedMessage.x1', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='x2', full_name='EquationCalculatedMessage.x2', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='realSolutionExists', full_name='EquationCalculatedMessage.realSolutionExists', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=69,
  serialized_end=148,
)

DESCRIPTOR.message_types_by_name['EquationMessage'] = _EQUATIONMESSAGE
DESCRIPTOR.message_types_by_name['EquationCalculatedMessage'] = _EQUATIONCALCULATEDMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EquationMessage = _reflection.GeneratedProtocolMessageType('EquationMessage', (_message.Message,), {
  'DESCRIPTOR' : _EQUATIONMESSAGE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:EquationMessage)
  })
_sym_db.RegisterMessage(EquationMessage)

EquationCalculatedMessage = _reflection.GeneratedProtocolMessageType('EquationCalculatedMessage', (_message.Message,), {
  'DESCRIPTOR' : _EQUATIONCALCULATEDMESSAGE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:EquationCalculatedMessage)
  })
_sym_db.RegisterMessage(EquationCalculatedMessage)



_CALCULATOR = _descriptor.ServiceDescriptor(
  name='Calculator',
  full_name='Calculator',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=150,
  serialized_end=219,
  methods=[
  _descriptor.MethodDescriptor(
    name='Solve',
    full_name='Calculator.Solve',
    index=0,
    containing_service=None,
    input_type=_EQUATIONMESSAGE,
    output_type=_EQUATIONCALCULATEDMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CALCULATOR)

DESCRIPTOR.services_by_name['Calculator'] = _CALCULATOR

# @@protoc_insertion_point(module_scope)
