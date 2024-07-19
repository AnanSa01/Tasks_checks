from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider


class GetGivenRecommendations:
    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider.load_from_file("../../config.json")

    def get_given_recommendations_api_get(self):
        return self._request.get_request(
            f"{self.config["base_url"]}/get-given-recommendations?{self.config["get_given_recommendations_function"]}",
            self.config["header"])