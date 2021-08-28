from time import sleep

from grpc_benchmark import GrpcBenchmark
from rest_benchmark import RestBenchmark

INITIAL_WAIT_SEC = 10
TRIAL_COUNTS = [1, 10, 40, 70]
REPEAT = 5


if __name__ == "__main__":
    print(f"start gRPC, REST benchmark... wait {INITIAL_WAIT_SEC} sec.")
    sleep(INITIAL_WAIT_SEC)
    results = {}
    for trial_count in TRIAL_COUNTS:
        results.update(GrpcBenchmark(REPEAT).run(trial_count))
        results.update(RestBenchmark(REPEAT).run(trial_count))
    print(results)
