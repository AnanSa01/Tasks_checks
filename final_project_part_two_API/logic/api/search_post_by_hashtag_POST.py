import logging

from requests import RequestException

from final_project_part_two_API.infra.logging_basicConfig import LoggingSetup
from final_project_part_two_API.infra.api.response_wrapper import ResponseWrapper
from final_project_part_two_API.logic.api.base_init import BaseInit


class SearchPostByHashtag(BaseInit):
    def __init__(self, request):
        super().__init__(request)

    def search_post_by_hashtag_api_post(self, payload):
        """
        this function returns search post by hashtag using POST
        """
        try:
            return self._request.post_request(f"{self.config["base_url"]}/search-posts-by-hashtag",
                                                     self.config["header"], payload)

        except RequestException:
            logging.error("Error in receiving API data from 'search_post_by_hashtag' function")