






import unittest

from infra.api.api_wrapper import APIWrapper
from infra.both.config_provider import ConfigProvider
from logic.api.api_draw_a_card import APIDrawACard


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.api_request = APIWrapper()

    def test_draw_a_card(self):
        """
        this function tests drawing a card from deck and makes sure that the remaining card did change accordingly
        """
        api_draw_a_card = APIDrawACard(self.api_request)
        result = api_draw_a_card.get_draw_a_card()
        body = result.json()
        self.config = ConfigProvider.load_from_file('../../config.json')
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(body["remaining"], 52 - int(self.config['draw_a_card']))

        print(body["remaining"])


if __name__ == '__main__':
    unittest.main()
