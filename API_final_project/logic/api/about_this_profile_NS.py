from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider


class AboutThisProfile:
    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider.load_from_file("../../config.json")

    def about_this_profile(self):
        return self._request.get_request(
            f"{self.config["base_url"]}/about-this-profile?{self.config["about_this_profile_function"]}",
            self.config["header"])