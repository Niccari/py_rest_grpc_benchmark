import grpc
from timeit import repeat

from def_proto import api_pb2
from def_proto import api_pb2_grpc


class GrpcBenchmark:
    CHUNK_SIZE = 1024 * 512

    def __init__(self, repeat: int) -> None:
        self.channel = grpc.insecure_channel("server:22312")
        self.stub = api_pb2_grpc.ApiStub(self.channel)
        self.repeat = repeat

    def _run_empty_test(self) -> None:
        self.stub.GetEmpty(api_pb2.EmptyRequest())

    def _run_content_response_test(self, count: int) -> None:
        self.stub.GetContent(api_pb2.ContentRequest(count=count))

    @classmethod
    def _load_file(cls, file_path: str, mode: str) -> list:
        items = []
        with open(file_path, mode) as f:
            while True:
                item = f.read(cls.CHUNK_SIZE)
                items.append(item)
                if len(item) < cls.CHUNK_SIZE:
                    break
        return items

    def _run_post_text_test(self, size_mb: int) -> None:
        texts = GrpcBenchmark._load_file(f"mock_data/text_{size_mb}mb", "r")

        def stream():
            for text in texts:
                yield api_pb2.TextRequest(text=text)
        self.stub.UploadText(stream())

    def _run_post_bin_test(self, size_mb: int) -> None:
        images = GrpcBenchmark._load_file(f"mock_data/bin_{size_mb}mb", "rb")

        def stream():
            for image in images:
                yield api_pb2.ImageRequest(image=image)
        self.stub.UploadImage(stream())

    def _run_test(self, function: callable, trial_count: int) -> float:
        elapsed_secs = \
            repeat(function, number=trial_count, repeat=self.repeat)
        return sum(elapsed_secs) / len(elapsed_secs)

    def run(self, trial_count: int) -> dict:
        results = {}
        for _ in range(trial_count):
            results[f"grpc_get_empty_{trial_count}"] = \
                self._run_test(
                    lambda: self._run_empty_test(), trial_count)
            results[f"grpc_get_content_{1}_{trial_count}"] = \
                self._run_test(
                    lambda: self._run_content_response_test(1), trial_count)
            results[f"grpc_get_content_{10}_{trial_count}"] = \
                self._run_test(
                    lambda: self._run_content_response_test(10), trial_count)
            results[f"grpc_get_content_{50}_{trial_count}"] = \
                self._run_test(
                    lambda: self._run_content_response_test(50), trial_count)
            results[f"grpc_get_content_{100}_{trial_count}"] = \
                self._run_test(
                    lambda: self._run_content_response_test(100), trial_count)
            results[f"grpc_post_text_{1}_{trial_count}"] = \
                self._run_test(
                    lambda: self._run_post_text_test(1), trial_count)
            results[f"grpc_post_text_{5}_{trial_count}"] = \
                self._run_test(
                    lambda: self._run_post_text_test(5), trial_count)
            results[f"grpc_post_text_{30}_{trial_count}"] = \
                self._run_test(
                    lambda: self._run_post_text_test(30), trial_count)
            results[f"grpc_post_bin_{1}_{trial_count}"] = \
                self._run_test(
                    lambda: self._run_post_bin_test(1), trial_count)
            results[f"grpc_post_bin_{5}_{trial_count}"] = \
                self._run_test(
                    lambda: self._run_post_bin_test(5), trial_count)
            results[f"grpc_post_bin_{30}_{trial_count}"] = \
                self._run_test(
                    lambda: self._run_post_bin_test(30), trial_count)
        return results
