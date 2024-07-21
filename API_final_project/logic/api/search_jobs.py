import logging

from requests import RequestException

from infra.logging_basicConfig import LoggingSetup

from logic.api.base_init import BaseInit


class SearchJobs(BaseInit):
    def __init__(self, request):
        super().__init__(request)

    def search_jobs_api_get(self, search_jobs_keyword, search_jobs_location_id):
        """
        this function returns search jobs using GET
        """
        try:
            return self._request.get_request(
                f"{self.config["base_url"]}/search-jobs?keywords={search_jobs_keyword}&locationId="
                f"{search_jobs_location_id}&datePosted=anyTime&sort=mostRelevant", self.config["header"])

        except RequestException:
            logging.error("Error in receiving API data from 'search_jobs' function")

    def search_jobs_v2_api_get(self, search_jobs_keyword, search_jobs_location_id):
        """
        this function returns search jobs using GET
        """
        try:
            return self._request.get_request(
                f"{self.config["base_url"]}/search-jobs-v2?keywords={search_jobs_keyword}&locationId="
                f"{search_jobs_location_id}&datePosted=anyTime&sort=mostRelevant", self.config["header"])

        except RequestException:
            logging.error("Error in receiving API data from 'get_company_employees_count' function")
