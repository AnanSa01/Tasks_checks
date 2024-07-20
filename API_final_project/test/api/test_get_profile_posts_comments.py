import unittest

from infra.api.api_wrapper import APIWrapper
from logic.api.get_profile_posts_comments import GetProfilePostsComments


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self._api_request = APIWrapper()

    def test_profile_posts_comments(self):
        api_profile_posts_comments = GetProfilePostsComments(self._api_request)
        result = api_profile_posts_comments.get_profile_posts_comments_api_get()
        body = result.json()
        print(body)
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(body["message"], "")


if __name__ == '__main__':
    unittest.main()
