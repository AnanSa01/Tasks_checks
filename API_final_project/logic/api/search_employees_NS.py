from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider


class SearchEmployees:
    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider.load_from_file("../../config.json")

    def search_employees_api_get(self):
        return self._request.get_request(f"{self.config["base_url"]}/search-employees?{self.config["search_employees_function"]}", self.config["header"])
