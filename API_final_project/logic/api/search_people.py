from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider


class SearchPeople:
    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider.load_from_file('../../config.json')

    def search_people_api_get(self):
        return self._request.get_request(f"{self.config["base_url"]}/search-people?{self.config["search_people_function"]}", self.config["header"])
