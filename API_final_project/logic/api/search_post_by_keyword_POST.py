import logging

from requests import RequestException

from infra.logging_basicConfig import LoggingSetup

from infra.api.response_wrapper import ResponseWrapper
from logic.api.base_init import BaseInit


class SearchPostByKeyword(BaseInit):
    def __init__(self, request):
        super().__init__(request)

    def search_post_by_keyword_api_post(self, query_string):
        """
        this function returns search post by hashtag using POST
        """
        try:
            response = self._request.post_request(f"{self.config["base_url"]}/search-posts",
                                                  self.config["header"], query_string)
            response_wrapper = ResponseWrapper(ok=response.ok, status_code=response.status_code, body=response.json())
            return response_wrapper

        except RequestException:
            logging.error("Error in receiving API data from 'search_post_by_keyword' function")
