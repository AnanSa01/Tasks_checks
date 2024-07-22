import logging

from requests import RequestException

from infra.api.response_wrapper import ResponseWrapper
from infra.logging_basicConfig import LoggingSetup

from logic.api.base_init import BaseInit


class GetHiringTeam(BaseInit):
    def __init__(self, request):
        super().__init__(request)

    def get_hiring_team_api_get(self, hiring_team_id):
        """
        this function returns hiring team using GET
        """
        try:
            response = self._request.get_request(f"{self.config["base_url"]}/get-hiring-team?id={hiring_team_id}"
                                             f"&url=https://www.linkedin.com/jobs/view/{hiring_team_id}/",
                                             self.config["header"])

            return ResponseWrapper(ok=response.ok, status_code=response.status_code, body=response.json())

        except RequestException:
            logging.error("Error in receiving API data from 'get_hiring_team' function")
