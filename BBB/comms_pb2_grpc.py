# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import comms_pb2 as comms__pb2


class WebserverStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.put_message = channel.unary_unary(
        '/Webserver/put_message',
        request_serializer=comms__pb2.server_req.SerializeToString,
        response_deserializer=comms__pb2.vessel_state.FromString,
        )


class WebserverServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def put_message(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_WebserverServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'put_message': grpc.unary_unary_rpc_method_handler(
          servicer.put_message,
          request_deserializer=comms__pb2.server_req.FromString,
          response_serializer=comms__pb2.vessel_state.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Webserver', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class TeensyserverStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.put_message = channel.unary_unary(
        '/Teensyserver/put_message',
        request_serializer=comms__pb2.vessel_state.SerializeToString,
        response_deserializer=comms__pb2.vessel_state.FromString,
        )


class TeensyserverServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def put_message(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TeensyserverServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'put_message': grpc.unary_unary_rpc_method_handler(
          servicer.put_message,
          request_deserializer=comms__pb2.vessel_state.FromString,
          response_serializer=comms__pb2.vessel_state.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Teensyserver', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
