import unittest

from infra.api.api_wrapper import APIWrapper
from logic.api.search_people import SearchPeople


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.api_request = APIWrapper()

    def test_search_people(self):
        api_search_for_people = SearchPeople(self.api_request)
        result = api_search_for_people.search_people_api_get()
        body = result.json()
        data = body["data"]
        items = data["items"]
        print(body)
        first_item = items[2]["fullName"]
        print(first_item)
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(body["message"], "")


if __name__ == '__main__':
    unittest.main()
