import unittest
from infra.api.api_wrapper import APIWrapper
from logic.api.api_shuffle_the_cards import APIShuffle


class MyTestCase(unittest.TestCase):

    def setUp(self):
        api_request = APIWrapper()
        self.api_shuffle = APIShuffle(api_request)
        self.api_shuffle = APIShuffle(api_request)

    def test_shuffle_the_cards_get(self):
        """
        this function tests shuffling card with GET
        """
        result = self.api_shuffle.get_shuffle_the_deck_get()
        body = result.json()
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(body["remaining"], 52)

    def test_shuffle_the_cards_post(self):
        """
        this function tests shuffling card with POST
        """
        result = self.api_shuffle.get_shuffle_the_deck_post()
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.body['remaining'], 52)


if __name__ == '__main__':
    unittest.main()
