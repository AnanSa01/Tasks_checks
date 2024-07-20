from logic.api._base_init import BaseInit


class SearchJobs(BaseInit):
    def __init__(self, request):
        super().__init__(request)

    def search_jobs_api_get(self):
        return self._request.get_request(f"{self.config["base_url"]}/search-jobs?{self.config["search_jobs_function"]}",
                                         self.config["header"])

    def search_jobs_v2_api_get(self):
        return self._request.get_request(
            f"{self.config["base_url"]}/search-jobs-v2?{self.config["search_jobs_function"]}", self.config["header"])
