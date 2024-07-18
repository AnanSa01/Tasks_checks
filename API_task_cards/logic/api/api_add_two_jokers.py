from infra.api.api_wrapper import APIWrapper
from infra.api.response_wrapper import ResponseWrapper
from infra.config_provider import ConfigProvider


class APIAddTwoJokers:
    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider.load_from_file('../../config.json')

    def api_post_add_two_jokers(self, data):
        #response = requests.post(f"{self.config['base_url']}/?{data}")
        response = self._request.post_request(f"{self.config['base_url']}/?{data}")
        response_wrapper = ResponseWrapper(ok=response.ok, status_code=response.status_code, body=response.json())
        return response_wrapper
