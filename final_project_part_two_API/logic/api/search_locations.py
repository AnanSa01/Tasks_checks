import logging

from requests import RequestException

from final_project_part_two_API.infra.logging_basicConfig import LoggingSetup
from final_project_part_two_API.infra.api.response_wrapper import ResponseWrapper
from final_project_part_two_API.logic.api.base_init import BaseInit


class SearchLocations(BaseInit):
    def __init__(self, request):
        super().__init__(request)

    def search_locations_api_get(self, location_name):
        """
        this function returns search locations using GET
        """
        try:
            return self._request.get_request(f"{self.config["base_url"]}/search-locations?keyword={location_name}",
                                                    self.config["header"])

        except RequestException:
            logging.error("Error in receiving API data from 'search_locations' function")

    def return_items_in_search_locations(self, body_of_search_locations):
        """
        this function returns the dict key to items
        :param body_of_search_locations: body in json for find search locations function
        :return: data["items"]
        """
        data = body_of_search_locations["data"]
        return data["items"]
