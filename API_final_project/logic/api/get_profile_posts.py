from logic.api._base_init import BaseInit


class GetProfilePosts(BaseInit):
    def __init__(self, request):
        super().__init__(request)

    def get_profile_posts_api_get(self):
        return self._request.get_request(
            f"{self.config["base_url"]}/get-profile-posts?username={self.config["get_profile_posts_function"]}",
            self.config["header"])

    def return_user_in_get_profile_posts(self, body_of_get_profile_posts):
        data = body_of_get_profile_posts["data"]
        author = data[0]["author"]
        return author["username"]