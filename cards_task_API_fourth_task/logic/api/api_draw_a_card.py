from cards_task_API_fourth_task.infra.api.api_wrapper import APIWrapper
from cards_task_API_fourth_task.infra.config_provider import ConfigProvider


class APIDrawACard:
    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider.load_from_file('../../config.json')

    def get_draw_a_card(self):
        return self._request.get_request(f"{self.config['base_url']}/draw/?count={self.config['draw_a_card']}")

