import logging

from requests import RequestException

from infra.logging_basicConfig import LoggingSetup

from infra.api.response_wrapper import ResponseWrapper
from logic.api._base_init import BaseInit


class SearchPostByHashtag(BaseInit):
    def __init__(self, request):
        super().__init__(request)

    def search_post_by_hashtag_api_post(self):
        """
        this function returns search post by hashtag using POST
        """
        try:
            response = self._request.post_request(f"{self.config["base_url"]}/search-posts-by-hashtag",
                                                  self.config["header"],
                                                  self.config["search_post_by_hashtag_body"])
            return ResponseWrapper(ok=response.ok, status_code=response.status_code, body=response.json())

        except RequestException:
            logging.error("Error in receiving API data from 'search_post_by_hashtag' function")