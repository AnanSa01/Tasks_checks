import logging

from requests import RequestException

from infra.logging_basicConfig import LoggingSetup

from logic.api._base_init import BaseInit


class SearchPeople(BaseInit):
    def __init__(self, request):
        super().__init__(request)

    def search_people_api_get(self):
        """
        this function returns search people using GET
        """
        try:
            return self._request.get_request(
                f"{self.config["base_url"]}/search-people?{self.config["search_people_function"]}",
                self.config["header"])

        except RequestException:
            logging.error("Error in receiving API data from 'search_people' function")
