from logic.api._base_init import BaseInit


class GetProfilePostsComments(BaseInit):
    def __init__(self, request):
        super().__init__(request)

    def get_profile_posts_comments_api_get(self):
        return self._request.get_request(
            f"{self.config["base_url"]}/get-profile-posts-comments?{self.config["get_profile_posts_comments_function"]}",
            self.config["header"])
