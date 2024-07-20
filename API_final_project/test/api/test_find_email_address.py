import unittest

from infra.api.api_wrapper import APIWrapper
from logic.utilities import LoadConfig
from logic.api.find_email_address import FindEmailAddress


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.api_request = APIWrapper()
        self.config = LoadConfig.return_file()

    def test_find_email_address(self):
        api_find_email_address = FindEmailAddress(self.api_request)
        result = api_find_email_address.find_email_address_api_get()
        body = result.json()
        profile_data = api_find_email_address.return_profile_data_in_find_email_address(body)
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(profile_data["username"], self.config["find_email_address_check_username"])


if __name__ == '__main__':
    unittest.main()
