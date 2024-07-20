from logic.api._base_init import BaseInit


class GetProfileData(BaseInit):
    def __init__(self, request):
        super().__init__(request)

    def get_profile_data_api_get(self):
        return self._request.get_request(
            f"{self.config["base_url"]}/?username={self.config["get_profile_data_function"]}", self.config["header"])

    def return_geo_in_get_profile_data(self, body_of_get_profile_data):
        return body_of_get_profile_data["geo"]
