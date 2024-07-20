import logging

from requests import RequestException

from infra.logging_basicConfig import LoggingSetup

from logic.api._base_init import BaseInit


class GetHiringTeam(BaseInit):
    def __init__(self, request):
        super().__init__(request)

    def get_hiring_team_api_get(self):
        """
        this function returns hiring team using GET
        """
        try:
            return self._request.get_request(
                f"{self.config["base_url"]}/get-hiring-team?{self.config["get_hiring_team_function"]}",
                self.config["header"])

        except RequestException:
            logging.error("Error in receiving API data from 'get_hiring_team' function")