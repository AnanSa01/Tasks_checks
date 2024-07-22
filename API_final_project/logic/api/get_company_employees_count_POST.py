import logging

from requests import RequestException

from infra.logging_basicConfig import LoggingSetup

from infra.api.response_wrapper import ResponseWrapper
from logic.api.base_init import BaseInit


class GetCompanyEmployeesCount(BaseInit):

    def __init__(self, request):
        super().__init__(request)

    def get_company_employees_count_api_post(self, payload):
        """
        this function returns company employees count using POST
        """
        try:
            response = self._request.post_request(f"{self.config["base_url"]}/get-company-employees-count",
                                                  self.config["header"], payload)
            return ResponseWrapper(ok=response.ok, status_code=response.status_code, body=response.json())

        except RequestException:
            logging.error("Error in receiving API data from 'get_company_employees_count' function")
