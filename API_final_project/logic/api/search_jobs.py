from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider


class SearchJobs:
    def __init__(self, request: APIWrapper):
        self._request = APIWrapper()
        self.config = ConfigProvider.load_from_file("../../config.json")

    def search_jobs_api_get(self):
        return self._request.get_request(f"{self.config["base_url"]}/search-jobs?{self.config["search_jobs_function"]}", self.config["header"])

    def search_jobs_v2_api_get(self):
        return self._request.get_request(f"{self.config["base_url"]}/search-jobs_v2?{self.config["search_jobs_function"]}", self.config["header"])