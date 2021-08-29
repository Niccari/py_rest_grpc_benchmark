from concurrent import futures
import grpc
import time

import api_pb2
import api_pb2_grpc

from random_generator import generate_id
from random_generator import generate_string


class GrpcServer():
    class Service(api_pb2_grpc.ApiServicer):
        def GetEmpty(self, request, context):
            return api_pb2.EmptyResponse()

        def GetContent(self, request, context):
            count: int = request.count
            response_data = []
            for _ in range(count):
                response_data.append(api_pb2.Content(
                    id=generate_id(),
                    hoge=generate_string(),
                ))

            return api_pb2.ContentResponse(data=response_data)

        def UploadText(self, request_iterator, context):
            return api_pb2.EmptyResponse()

        def UploadImage(self, request_iterator, context):
            return api_pb2.EmptyResponse()

    def __init__(self) -> None:
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
        api_pb2_grpc.add_ApiServicer_to_server(
            GrpcServer.Service(), self.server)
        self.server.add_insecure_port('[::]:22312')
        self.server.start()

    def close(self) -> None:
        self.server.stop(0)


if __name__ == '__main__':
    grpc_server = GrpcServer()

    try:
        while True:
            time.sleep(60*60*24)
    except Exception:
        grpc_server.close()
