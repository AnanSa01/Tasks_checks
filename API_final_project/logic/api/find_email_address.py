from logic.api._base_init import BaseInit


class FindEmailAddress(BaseInit):

    def __init__(self, request):
        super().__init__(request)

    def find_email_address_api_get(self):
        return self._request.get_request(
            f"{self.config["base_url"]}/linkedin-to-email?{self.config["find_email_address_function"]}",
            self.config["header"])

    def return_profile_data_in_find_email_address(self, body_of_find_email_address):
        data = body_of_find_email_address["data"]
        return data["profileData"]
