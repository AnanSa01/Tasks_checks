from infra.api.api_wrapper import APIWrapper
from infra.api.response_wrapper import ResponseWrapper
from infra.config_provider import ConfigProvider


class APIShuffle:
    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider.load_from_file('../../config.json')

    def get_shuffle_the_deck_get(self):
        return self._request.get_request(f"{self.config['base_url']}/shuffle/?deck_count={self.config['deck_count']}")

    def get_shuffle_the_deck_post(self):
        #response = requests.post(f"{self.config['base_url']}/shuffle/?deck_count={self.config['deck_count']}")
        response = self._request.post_request(f"{self.config['base_url']}/shuffle/?deck_count={self.config['deck_count']}")
        response_wrapper = ResponseWrapper(ok=response.ok, status_code=response.status_code, body=response.json())
        return response_wrapper
