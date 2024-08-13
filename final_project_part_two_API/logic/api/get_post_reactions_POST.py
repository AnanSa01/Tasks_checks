import logging

from requests import RequestException

from final_project_part_two_API.infra.logging_basicConfig import LoggingSetup
from final_project_part_two_API.infra.api.response_wrapper import ResponseWrapper
from final_project_part_two_API.logic.api.base_init import BaseInit


class GetPostReactions(BaseInit):
    def __init__(self, request):
        super().__init__(request)

    def get_post_reactions_api_post(self, payload):
        """
        this function returns post reactions using POST
        """
        try:
            return self._request.post_request(f"{self.config["base_url"]}/get-post-reactions",
                                                     self.config["header"], payload)

        except RequestException:
            logging.error("Error in receiving API data from 'get_post_reactions' function")
