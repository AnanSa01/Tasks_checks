import logging

from requests import RequestException

from infra.logging_basicConfig import LoggingSetup

from logic.api._base_init import BaseInit


class GetPostReactions(BaseInit):
    def __init__(self, request):
        super().__init__(request)

    def get_post_reactions_api_post(self):
        """
        this function returns post reactions using POST
        """
        try:
            response = self._request.post_request(f"{self.config["base_url"]}/get-post-reactions",
                                                  self.config["header"],
                                                  self.config["get_post_reactions_body"])
            #response_wrapper = ResponseWrapper(ok=response.ok, status_code=response.status_code, body=response.json())
            return response

        except RequestException:
            logging.error("Error in receiving API data from 'get_post_reactions' function")
