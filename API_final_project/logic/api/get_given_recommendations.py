from logic.api._base_init import BaseInit


class GetGivenRecommendations(BaseInit):
    def __init__(self, request):
        super().__init__(request)

    def get_given_recommendations_api_get(self):
        return self._request.get_request(
            f"{self.config["base_url"]}/get-given-recommendations?{self.config["get_given_recommendations_function"]}",
            self.config["header"])
