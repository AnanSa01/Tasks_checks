import logging

from requests import RequestException

from infra.logging_basicConfig import LoggingSetup
from infra.api.response_wrapper import ResponseWrapper
from logic.api.base_init import BaseInit


class GetProfileLikes(BaseInit):
    def __init__(self, request):
        super().__init__(request)

    def get_profile_likes_api_get(self, profile_username):
        """
        this function returns profile likes using GET
        """
        try:
            return self._request.get_request(f"{self.config["base_url"]}/get-profile-likes?"
                                                 f"username={profile_username}&start=0", self.config["header"])

        except RequestException:
            logging.error("Error in receiving API data from 'get_profile_likes' function")
