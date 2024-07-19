from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider


class FindEmailAddress:

    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider.load_from_file('../../config.json')

    def find_email_address_api_get(self):
        return self._request.get_request(f"{self.config["base_url"]}/linkedin-to-email?{self.config["find_email_address_function"]}",
                                                         self.config["header"])