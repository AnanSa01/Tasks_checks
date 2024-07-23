import logging

from requests import RequestException

from infra.logging_basicConfig import LoggingSetup
from infra.api.response_wrapper import ResponseWrapper
from logic.api.base_init import BaseInit


class FindEmailAddress(BaseInit):

    ENDPOINT = "/linkedin-to-email?"
    PARAM_username = 'url=https://www.linkedin.com/in/'

    def __init__(self, request):
        super().__init__(request)

    def find_email_address_api_get(self, username):
        """
        this function returns email address using GET
        """
        try:
            return self._request.get_request(f"{self.config["base_url"]}{self.ENDPOINT}{self.PARAM_username}{username}/"
                                              , self.config["header"])

        except RequestException:
            logging.error("Error in receiving API data from 'find_email_address' function")

    def return_profile_data_in_find_email_address(self, body_of_find_email_address):
        """
        this function returns the dict key to profile data
        :param body_of_find_email_address:  body in json for find email address function
        :return: data["profileData"]
        """
        data = body_of_find_email_address["data"]
        return data["profileData"]
