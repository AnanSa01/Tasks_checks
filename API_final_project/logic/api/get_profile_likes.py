from logic.api._base_init import BaseInit


class GetProfileLikes(BaseInit):
    def __init__(self, request):
        super().__init__(request)

    def get_profile_likes_api_get(self):
        return self._request.get_request(
            f"{self.config["base_url"]}/get-profile-likes?{self.config["get_profile_likes_function"]}",
            self.config["header"])
