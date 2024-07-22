import logging

from requests import RequestException

from infra.api.response_wrapper import ResponseWrapper
from infra.logging_basicConfig import LoggingSetup

from logic.api.base_init import BaseInit


class HealthCheck(BaseInit):
    def __init__(self, request):
        super().__init__(request)

    def health_check_api_get(self):
        """
        this function returns health check using GET
        """
        try:
            response = self._request.get_request(f"{self.config["base_url"]}/health", self.config["header"])

            return ResponseWrapper(ok=response.ok, status_code=response.status_code, body=response.json())

        except RequestException:
            logging.error("Error in receiving API data from 'health_check' function")

