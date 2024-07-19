import unittest

from infra.api.api_wrapper import APIWrapper
from logic.api.search_post_by_hashtag_POST import SearchPostByHashtag


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.api_request = APIWrapper()

    def test_search_post_by_hashtag(self):
        api_search_post_by_hashtag = SearchPostByHashtag(self.api_request)
        result = api_search_post_by_hashtag.api_post_search_post_by_hashtag()
        print(result.body)
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.body["message"], "")


if __name__ == '__main__':
    unittest.main()
