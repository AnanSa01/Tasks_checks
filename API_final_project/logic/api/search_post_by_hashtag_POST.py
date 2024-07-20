from infra.api.response_wrapper import ResponseWrapper
from logic.api._base_init import BaseInit


class SearchPostByHashtag(BaseInit):
    def __init__(self, request):
        super().__init__(request)

    def api_post_search_post_by_hashtag(self):
        response = self._request.post_request(f"{self.config["base_url"]}/search-posts-by-hashtag",
                                              self.config["header"],
                                              self.config["search_post_by_hashtag_body"])
        return ResponseWrapper(ok=response.ok, status_code=response.status_code, body=response.json())