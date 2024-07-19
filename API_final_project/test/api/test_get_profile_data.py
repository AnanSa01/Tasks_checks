import unittest

from infra.api.api_wrapper import APIWrapper
from logic.api.get_profile_data import GetProfileData


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.api_request = APIWrapper()

    def test_get_profile_data(self):
        api_get_profile_data = GetProfileData(self.api_request)
        result = api_get_profile_data.get_profile_data_api_get()
        body = result.json()
        geo = body["geo"]
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(body["firstName"], "Yogesh")
        self.assertEqual(geo["country"], "India")


if __name__ == '__main__':
    unittest.main()
