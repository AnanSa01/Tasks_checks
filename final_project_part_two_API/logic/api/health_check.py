import logging

from requests import RequestException

from final_project_part_two_API.infra.logging_basicConfig import LoggingSetup
from final_project_part_two_API.infra.api.response_wrapper import ResponseWrapper
from final_project_part_two_API.logic.api.base_init import BaseInit


class HealthCheck(BaseInit):
    def __init__(self, request):
        super().__init__(request)

    def health_check_api_get(self):
        """
        this function returns health check using GET
        """
        try:
            return self._request.get_request(f"{self.config["base_url"]}/health", self.config["header"])

        except RequestException:
            logging.error("Error in receiving API data from 'health_check' function")

