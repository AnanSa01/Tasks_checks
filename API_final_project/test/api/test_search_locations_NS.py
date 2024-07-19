import unittest

from infra.api.api_wrapper import APIWrapper
from logic.api.search_locations_NS import SearchLocations


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self._api_request = APIWrapper()

    def test_search_locations(self):
        api_search_locations = SearchLocations(self._api_request)
        result = api_search_locations.search_locations_api_get()
        body = result.json()
        print(body)
        # data = body["data"]  check for berlin
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(body["message"], "")


if __name__ == '__main__':
    unittest.main()
