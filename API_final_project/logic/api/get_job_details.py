import logging

from requests import RequestException

from infra.api.response_wrapper import ResponseWrapper
from infra.logging_basicConfig import LoggingSetup

from logic.api.base_init import BaseInit


class GetJobDetails(BaseInit):
    def __init__(self, request):
        super().__init__(request)

    def find_job_details_api_get(self, job_id):
        """
        this function returns job details using GET
        """
        try:
            response = self._request.get_request(
                f"{self.config["base_url"]}/get-job-details?id={job_id}", self.config["header"])

            return ResponseWrapper(ok=response.ok, status_code=response.status_code, body=response.json())

        except RequestException:
            logging.error("Error in receiving API data from 'find_job_details' function")

    def return_data_in_find_job_details(self, body_of_find_job_details):
        """
        this function returns the dict key to data
        :param body_of_find_job_details: body in json for find job details function
        :return: data key
        """
        return body_of_find_job_details["data"]
