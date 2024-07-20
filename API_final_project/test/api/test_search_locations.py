import unittest

from infra.api.api_wrapper import APIWrapper
from logic.utilities import LoadConfig
from logic.api.search_locations import SearchLocations


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self._api_request = APIWrapper()
        self.config = LoadConfig.return_file()

    def test_search_locations(self):
        api_search_locations = SearchLocations(self._api_request)
        result = api_search_locations.search_locations_api_get()
        body = result.json()
        items = api_search_locations.return_items_in_search_locations(body)
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(body["message"], "")
        self.assertTrue("success")
        self.assertIn(self.config["search_locations_check_name"], items[0]["name"])


if __name__ == '__main__':
    unittest.main()
