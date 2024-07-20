import unittest

from infra.api.api_wrapper import APIWrapper
from logic.api.get_given_recommendations import GetGivenRecommendations


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self._api_request = APIWrapper()

    def test_get_given_recommendations(self):
        api_get_given_recommendations = GetGivenRecommendations(self._api_request)
        result = api_get_given_recommendations.get_given_recommendations_api_get()
        body = result.json()
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(body["message"], "")


if __name__ == '__main__':
    unittest.main()
