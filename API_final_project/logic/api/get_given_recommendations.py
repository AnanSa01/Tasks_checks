import logging

from requests import RequestException

from infra.logging_basicConfig import LoggingSetup

from logic.api._base_init import BaseInit


class GetGivenRecommendations(BaseInit):
    def __init__(self, request):
        super().__init__(request)

    def get_given_recommendations_api_get(self):
        """
        this function returns given recommendations using GET
        """
        try:
            return self._request.get_request(
                f"{self.config["base_url"]}/get-given-recommendations?{self.config["get_given_recommendations_function"]}",
                self.config["header"])

        except RequestException:
            logging.error("Error in receiving API data from 'get_given_recommendations' function")
