import logging

from requests import RequestException

from infra.logging_basicConfig import LoggingSetup

from logic.api._base_init import BaseInit


class GetProfileData(BaseInit):
    def __init__(self, request):
        super().__init__(request)

    def get_profile_data_api_get(self):
        """
        this function returns profile data using GET
        """
        try:
            return self._request.get_request(
                f"{self.config["base_url"]}/?username={self.config["get_profile_data_function"]}",
                self.config["header"])

        except RequestException:
            logging.error("Error in receiving API data from 'get_profile_data' function")

    def return_geo_in_get_profile_data(self, body_of_get_profile_data):
        """
        this function returns the dict key to geo
        :param body_of_get_profile_data: body in json for get profile data function
        :return: body["geo"]
        """
        return body_of_get_profile_data["geo"]
