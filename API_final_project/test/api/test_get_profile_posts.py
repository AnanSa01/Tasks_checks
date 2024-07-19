import unittest

from infra.api.api_wrapper import APIWrapper
from logic.api.get_profile_posts import GetProfilePosts


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.api_request = APIWrapper()

    def test_get_profile_posts(self):
        api_get_profile_posts = GetProfilePosts(self.api_request)
        result = api_get_profile_posts.get_profile_posts_api_get()
        body = result.json()
        data = body["data"]
        author = data[0]["author"]
        username = author["username"]
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(username, "adamselipsky")

        print(body)


if __name__ == '__main__':
    unittest.main()
