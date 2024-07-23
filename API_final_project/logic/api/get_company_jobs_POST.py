import logging

from requests import RequestException

from infra.logging_basicConfig import LoggingSetup
from infra.api.response_wrapper import ResponseWrapper
from logic.api.base_init import BaseInit


class GetCompanyJobs(BaseInit):

    ENDPOINT = "/company-jobs?"
    PARAM_username = "username="

    def __init__(self, request):
        super().__init__(request)

    def get_company_jobs_api_post(self, company_name, payload):
        """
        this function returns company jobs using POST
        """
        try:
            return self._request.post_request(f"{self.config["base_url"]}{self.ENDPOINT}{self.PARAM_username}"
                                                  f"{company_name}", self.config["header"], payload)

        except RequestException:
            logging.error("Error in receiving API data from 'get_company_jobs' function")
