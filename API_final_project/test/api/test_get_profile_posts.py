import unittest

from infra.api.api_wrapper import APIWrapper
from logic.utilities import LoadConfig
from logic.api.get_profile_posts import GetProfilePosts


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.api_request = APIWrapper()
        self.config = LoadConfig.return_file()

    def test_get_profile_posts(self):
        api_get_profile_posts = GetProfilePosts(self.api_request)
        result = api_get_profile_posts.get_profile_posts_api_get()
        body = result.json()
        username = api_get_profile_posts.return_user_in_get_profile_posts(body)
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(body["message"], "")
        self.assertEqual(username, self.config["get_profile_posts_check_username"])


if __name__ == '__main__':
    unittest.main()
