import logging

from requests import RequestException

from infra.logging_basicConfig import LoggingSetup
from infra.api.response_wrapper import ResponseWrapper
from logic.api.base_init import BaseInit


class SearchPeople(BaseInit):
    def __init__(self, request):
        super().__init__(request)

    def search_people_api_get(self, name_for_search, place_for_search):
        """
        this function returns search people using GET
        """
        try:
            return self._request.get_request(f"{self.config["base_url"]}/search-people?keywords={name_for_search}"
                                                 f"&start=0&geo={place_for_search}", self.config["header"])

        except RequestException:
            logging.error("Error in receiving API data from 'search_people' function")

    def return_items_in_search_people(self, body_of_search_people):
        """
        this function returns the dict key to items
        :param body_of_search_people: body in json for find search people function
        :return: data["items"]
        """
        data = body_of_search_people["data"]
        return data["items"]
