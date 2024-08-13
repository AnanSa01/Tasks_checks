import logging

from requests import RequestException

from final_project_part_two_API.infra.logging_basicConfig import LoggingSetup
from final_project_part_two_API.infra.api.response_wrapper import ResponseWrapper
from final_project_part_two_API.logic.api.base_init import BaseInit


class GetCompanyEmployeesCount(BaseInit):

    ENDPOINT = "/get-company-employees-count"

    def __init__(self, request):
        super().__init__(request)

    def get_company_employees_count_api_post(self, payload):
        """
        this function returns company employees count using POST
        """
        try:
            return self._request.post_request(f"{self.config["base_url"]}{self.ENDPOINT}",
                                                  self.config["header"], payload)

        except RequestException:
            logging.error("Error in receiving API data from 'get_company_employees_count' function")
