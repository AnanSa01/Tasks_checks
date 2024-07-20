import logging

from requests import RequestException

from infra.logging_basicConfig import LoggingSetup

from logic.api._base_init import BaseInit


class GetProfilePostsComments(BaseInit):
    def __init__(self, request):
        super().__init__(request)

    def get_profile_posts_comments_api_get(self):
        """
        this function returns profile posts comments using GET
        """
        try:
            return self._request.get_request(
                f"{self.config["base_url"]}/get-profile-posts-comments?{self.config["get_profile_posts_comments_function"]}",
                self.config["header"])

        except RequestException:
            logging.error("Error in receiving API data from 'get_profile_posts_comments' function")
