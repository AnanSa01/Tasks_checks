from infra.api.api_wrapper import APIWrapper
from infra.api.response_wrapper import ResponseWrapper
from infra.config_provider import ConfigProvider


class SearchPostByHashtag:

    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider.load_from_file('../../config.json')

    def api_post_search_post_by_hashtag(self):
        response = self._request.post_request(f"{self.config["base_url"]}/search-posts-by-hashtag",
                                              self.config["header"],
                                              self.config["search_post_by_hashtag_body"])
        response_wrapper = ResponseWrapper(ok=response.ok, status_code=response.status_code, body=response.json())
        return response_wrapper