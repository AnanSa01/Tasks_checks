from logic.api._base_init import BaseInit


class GetPostReactions(BaseInit):
    def __init__(self, request):
        super().__init__(request)

    def api_post_get_post_reactions(self):
        response = self._request.post_request(f"{self.config["base_url"]}/get-post-reactions",
                                              self.config["header"],
                                              self.config["get_post_reactions_body"])
        #response_wrapper = ResponseWrapper(ok=response.ok, status_code=response.status_code, body=response.json())
        return response
