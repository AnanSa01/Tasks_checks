from infra.api.response_wrapper import ResponseWrapper
from logic.api._base_init import BaseInit


class SearchPostByKeyword(BaseInit):
    def __init__(self, request):
        super().__init__(request)

    def api_post_search_post_by_keyword(self):
        response = self._request.post_request(f"{self.config["base_url"]}/search-posts",
                                              self.config["header"],
                                              self.config["search_post_by_keyword_body"])
        response_wrapper = ResponseWrapper(ok=response.ok, status_code=response.status_code, body=response.json())
        return response_wrapper
