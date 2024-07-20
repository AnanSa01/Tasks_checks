import logging

from requests import RequestException

from infra.logging_basicConfig import LoggingSetup

from infra.api.response_wrapper import ResponseWrapper
from logic.api._base_init import BaseInit


class GetCompanyJobs(BaseInit):
    def __init__(self, request):
        super().__init__(request)

    def get_company_jobs_api_post(self):
        """
        this function returns company jobs using POST
        """
        try:
            response = self._request.post_request(
                f"{self.config["base_url"]}/company-jobs?{self.config["get_company_jobs_function"]}",
                self.config["header"], self.config["get_company_jobs_body"])
            return ResponseWrapper(ok=response.ok, status_code=response.status_code, body=response.json())

        except RequestException:
            logging.error("Error in receiving API data from 'get_company_jobs' function")
