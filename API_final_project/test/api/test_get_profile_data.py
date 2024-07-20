import unittest

from infra.api.api_wrapper import APIWrapper
from logic.utilities import LoadConfig
from logic.api.get_profile_data import GetProfileData


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.api_request = APIWrapper()
        self.config = LoadConfig.return_file()

    def test_get_profile_data(self):
        api_get_profile_data = GetProfileData(self.api_request)
        result = api_get_profile_data.get_profile_data_api_get()
        body = result.json()
        geo = api_get_profile_data.return_geo_in_get_profile_data(body)
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(body["firstName"], self.config["get_profile_data_check_first_name"])
        self.assertEqual(geo["country"], self.config["get_profile_data_check_country"])


if __name__ == '__main__':
    unittest.main()
