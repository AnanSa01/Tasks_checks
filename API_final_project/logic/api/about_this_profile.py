from logic.api._base_init import BaseInit


class AboutThisProfile(BaseInit):
    def __init__(self, request):
        super().__init__(request)

    def about_this_profile(self):
        return self._request.get_request(
            f"{self.config["base_url"]}/about-this-profile?{self.config["about_this_profile_function"]}",
            self.config["header"])
