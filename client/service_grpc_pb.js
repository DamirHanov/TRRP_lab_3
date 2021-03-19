// GENERATED CODE -- DO NOT EDIT!

'use strict';
var grpc = require('@grpc/grpc-js');
var service_pb = require('./service_pb.js');

function serialize_EquationCalculatedMessage(arg) {
  if (!(arg instanceof service_pb.EquationCalculatedMessage)) {
    throw new Error('Expected argument of type EquationCalculatedMessage');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_EquationCalculatedMessage(buffer_arg) {
  return service_pb.EquationCalculatedMessage.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_EquationMessage(arg) {
  if (!(arg instanceof service_pb.EquationMessage)) {
    throw new Error('Expected argument of type EquationMessage');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_EquationMessage(buffer_arg) {
  return service_pb.EquationMessage.deserializeBinary(new Uint8Array(buffer_arg));
}


var CalculatorService = exports.CalculatorService = {
  solve: {
    path: '/Calculator/Solve',
    requestStream: false,
    responseStream: false,
    requestType: service_pb.EquationMessage,
    responseType: service_pb.EquationCalculatedMessage,
    requestSerialize: serialize_EquationMessage,
    requestDeserialize: deserialize_EquationMessage,
    responseSerialize: serialize_EquationCalculatedMessage,
    responseDeserialize: deserialize_EquationCalculatedMessage,
  },
};

exports.CalculatorClient = grpc.makeGenericClientConstructor(CalculatorService);
