






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
        self.assertEqual(body["remaining"], 52 - self.config['draw_a_card'])

        print(f"How many card to draw? {self.config['draw_a_card']}")
        print(f"Number of cards remained in deck: {body["remaining"]}")


if __name__ == '__main__':
    unittest.main()
