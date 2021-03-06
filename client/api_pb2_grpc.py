# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import api_pb2 as api__pb2


class ApiStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetEmpty = channel.unary_unary(
                '/niccari_test.Api/GetEmpty',
                request_serializer=api__pb2.EmptyRequest.SerializeToString,
                response_deserializer=api__pb2.EmptyResponse.FromString,
                )
        self.GetContent = channel.unary_unary(
                '/niccari_test.Api/GetContent',
                request_serializer=api__pb2.ContentRequest.SerializeToString,
                response_deserializer=api__pb2.ContentResponse.FromString,
                )
        self.PostEmpty = channel.unary_unary(
                '/niccari_test.Api/PostEmpty',
                request_serializer=api__pb2.EmptyRequest.SerializeToString,
                response_deserializer=api__pb2.EmptyResponse.FromString,
                )
        self.PostContent = channel.unary_unary(
                '/niccari_test.Api/PostContent',
                request_serializer=api__pb2.Content.SerializeToString,
                response_deserializer=api__pb2.EmptyResponse.FromString,
                )
        self.UploadText = channel.stream_unary(
                '/niccari_test.Api/UploadText',
                request_serializer=api__pb2.TextRequest.SerializeToString,
                response_deserializer=api__pb2.EmptyResponse.FromString,
                )
        self.UploadImage = channel.stream_unary(
                '/niccari_test.Api/UploadImage',
                request_serializer=api__pb2.ImageRequest.SerializeToString,
                response_deserializer=api__pb2.EmptyResponse.FromString,
                )


class ApiServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetEmpty(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetContent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PostEmpty(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PostContent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UploadText(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UploadImage(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ApiServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetEmpty': grpc.unary_unary_rpc_method_handler(
                    servicer.GetEmpty,
                    request_deserializer=api__pb2.EmptyRequest.FromString,
                    response_serializer=api__pb2.EmptyResponse.SerializeToString,
            ),
            'GetContent': grpc.unary_unary_rpc_method_handler(
                    servicer.GetContent,
                    request_deserializer=api__pb2.ContentRequest.FromString,
                    response_serializer=api__pb2.ContentResponse.SerializeToString,
            ),
            'PostEmpty': grpc.unary_unary_rpc_method_handler(
                    servicer.PostEmpty,
                    request_deserializer=api__pb2.EmptyRequest.FromString,
                    response_serializer=api__pb2.EmptyResponse.SerializeToString,
            ),
            'PostContent': grpc.unary_unary_rpc_method_handler(
                    servicer.PostContent,
                    request_deserializer=api__pb2.Content.FromString,
                    response_serializer=api__pb2.EmptyResponse.SerializeToString,
            ),
            'UploadText': grpc.stream_unary_rpc_method_handler(
                    servicer.UploadText,
                    request_deserializer=api__pb2.TextRequest.FromString,
                    response_serializer=api__pb2.EmptyResponse.SerializeToString,
            ),
            'UploadImage': grpc.stream_unary_rpc_method_handler(
                    servicer.UploadImage,
                    request_deserializer=api__pb2.ImageRequest.FromString,
                    response_serializer=api__pb2.EmptyResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'niccari_test.Api', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Api(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetEmpty(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/niccari_test.Api/GetEmpty',
            api__pb2.EmptyRequest.SerializeToString,
            api__pb2.EmptyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetContent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/niccari_test.Api/GetContent',
            api__pb2.ContentRequest.SerializeToString,
            api__pb2.ContentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PostEmpty(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/niccari_test.Api/PostEmpty',
            api__pb2.EmptyRequest.SerializeToString,
            api__pb2.EmptyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PostContent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/niccari_test.Api/PostContent',
            api__pb2.Content.SerializeToString,
            api__pb2.EmptyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UploadText(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/niccari_test.Api/UploadText',
            api__pb2.TextRequest.SerializeToString,
            api__pb2.EmptyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UploadImage(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/niccari_test.Api/UploadImage',
            api__pb2.ImageRequest.SerializeToString,
            api__pb2.EmptyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
