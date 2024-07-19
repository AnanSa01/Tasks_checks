from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider


class GetProfilePosts:
    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider.load_from_file('../../config.json')

    def get_profile_posts_api_get(self):
        return self._request.get_request(f"{self.config["base_url"]}/get-profile-posts?username={self.config["get_profile_posts_function"]}", self.config["header"])