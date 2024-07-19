import unittest

from infra.api.api_wrapper import APIWrapper
from logic.api.get_post_reactions_POST import GetPostReactions


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self._api_request = APIWrapper()

    def test_get_post_reactions(self):
        api_get_post_reactions = GetPostReactions(self._api_request)
        result = api_get_post_reactions.api_post_get_post_reactions()
        print(result)
        print(result.ok)
        print(result.status_code)
        print(result.json())
        body = result.json()
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(body["message"], "")


if __name__ == '__main__':
    unittest.main()
