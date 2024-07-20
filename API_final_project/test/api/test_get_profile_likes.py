import unittest

from infra.api.api_wrapper import APIWrapper
from logic.api.get_profile_likes import GetProfileLikes


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self._api_request = APIWrapper()

    def test_get_profile_likes(self):
        api_get_profile_likes = GetProfileLikes(self._api_request)
        result = api_get_profile_likes.get_profile_likes_api_get()
        body = result.json()
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(body["message"], "")


if __name__ == '__main__':
    unittest.main()
