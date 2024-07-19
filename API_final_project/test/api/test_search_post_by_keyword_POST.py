import unittest

from infra.api.api_wrapper import APIWrapper
from logic.api.search_post_by_keyword_POST import SearchPostByKeyword


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.api_request = APIWrapper()

    def test_search_post_by_keyword(self):
        api_search_post_by_keyword = SearchPostByKeyword(self.api_request)
        result = api_search_post_by_keyword.api_post_search_post_by_keyword()
        print(result.body)
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.body["message"], "")


if __name__ == '__main__':
    unittest.main()
