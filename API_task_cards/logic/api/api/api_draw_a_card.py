from infra.api.api_wrapper import APIWrapper
from infra.both.config_provider import ConfigProvider


class APIDrawACard:
    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider.load_from_file('../../config.json')

    def get_draw_a_card(self):
        return self._request.get_request(f"{self.config['base_url']}api/deck/new/draw/?count={self.config['draw_a_card']}")

