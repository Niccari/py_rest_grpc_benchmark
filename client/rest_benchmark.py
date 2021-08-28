import requests

from timeit import repeat


class RestBenchmark:
    DOMAIN = "http://server:8000"

    def __init__(self, repeat: int) -> None:
        self.repeat = repeat

    @classmethod
    def _run_empty_test(cls) -> None:
        url = f"{cls.DOMAIN}/"
        requests.get(url)

    @classmethod
    def _run_content_response_test(cls, count: int) -> None:
        url = f"{cls.DOMAIN}/contents?count={count}"
        requests.get(url)

    @classmethod
    def _run_post_text_test(cls, size_mb: int) -> None:
        url = f"{cls.DOMAIN}/texts"

        with open(f"mock_data/text_{size_mb}mb", "r") as f:
            requests.post(url, files={
                'file': f,
            })

    @classmethod
    def _run_post_bin_test(cls, size_mb: int) -> None:
        url = f"{cls.DOMAIN}/images"

        with open(f"mock_data/bin_{size_mb}mb", "rb") as f:
            requests.post(url, files={
                'file': f,
            })

    def _run_test(self, function: callable, trial_count: int) -> float:
        elapsed_secs = \
            repeat(function, number=trial_count, repeat=self.repeat)
        return sum(elapsed_secs) / len(elapsed_secs)

    def run(self, trial_count: int) -> dict:
        results = {}
        for _ in range(trial_count):
            results[f"rest_get_empty_{trial_count}"] = \
                self._run_test(lambda: self._run_empty_test(), trial_count)
            results[f"rest_get_content_{1}_{trial_count}"] = \
                self._run_test(
                    lambda: self._run_content_response_test(1), trial_count)
            results[f"rest_get_content_{10}_{trial_count}"] = \
                self._run_test(
                    lambda: self._run_content_response_test(10), trial_count)
            results[f"rest_get_content_{50}_{trial_count}"] = \
                self._run_test(
                    lambda: self._run_content_response_test(50), trial_count)
            results[f"rest_get_content_{100}_{trial_count}"] = \
                self._run_test(
                    lambda: self._run_content_response_test(100), trial_count)
            results[f"rest_post_text_{1}_{trial_count}"] = \
                self._run_test(
                    lambda: self._run_post_text_test(1), trial_count)
            results[f"rest_post_text_{5}_{trial_count}"] = \
                self._run_test(
                    lambda: self._run_post_text_test(5), trial_count)
            results[f"rest_post_text_{30}_{trial_count}"] = \
                self._run_test(
                    lambda: self._run_post_text_test(30), trial_count)
            results[f"rest_post_bin_{1}_{trial_count}"] = \
                self._run_test(
                    lambda: self._run_post_bin_test(1), trial_count)
            results[f"rest_post_bin_{5}_{trial_count}"] = \
                self._run_test(
                    lambda: self._run_post_bin_test(5), trial_count)
            results[f"rest_post_bin_{30}_{trial_count}"] = \
                self._run_test(
                    lambda: self._run_post_bin_test(30), trial_count)
        return results
