import logging

from requests import RequestException

from infra.api.response_wrapper import ResponseWrapper
from infra.logging_basicConfig import LoggingSetup

from logic.api.base_init import BaseInit


class FindEmailAddress(BaseInit):

    def __init__(self, request):
        super().__init__(request)

    def find_email_address_api_get(self, username):
        """
        this function returns email address using GET
        """
        try:
            response = self._request.get_request(
                f"{self.config["base_url"]}/linkedin-to-email?url=https://www.linkedin.com/in/{username}/",
                self.config["header"])

            return ResponseWrapper(ok=response.ok, status_code=response.status_code, body=response.json())

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
