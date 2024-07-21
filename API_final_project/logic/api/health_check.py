import logging

from requests import RequestException

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
            return self._request.get_request(f"{self.config["base_url"]}/health", self.config["header"])

        except RequestException:
            logging.error("Error in receiving API data from 'health_check' function")

    def return_data_in_health_check(self, body_of_health_check):
        """
        this function returns the dict key to data
        :param body_of_health_check: body in json for find "health check" function
        :return: body["data"]
        """
        return body_of_health_check["data"]
