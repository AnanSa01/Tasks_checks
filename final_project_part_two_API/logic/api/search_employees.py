import logging

from requests import RequestException

from final_project_part_two_API.infra.logging_basicConfig import LoggingSetup
from final_project_part_two_API.infra.api.response_wrapper import ResponseWrapper
from final_project_part_two_API.logic.api.base_init import BaseInit


class SearchEmployees(BaseInit):
    def __init__(self, request):
        super().__init__(request)

    def search_employees_api_get(self, company_id, company_place_wp):
        """
        this function returns search employees using GET
        """
        try:
            return self._request.get_request(f"{self.config["base_url"]}/search-employees?companyId={company_id}"
                                                 f"&start=0&geoIds={company_place_wp}", self.config["header"])

        except RequestException:
            logging.error("Error in receiving API data from 'search_employees' function")
