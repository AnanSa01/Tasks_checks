import unittest

from infra.api.api_wrapper import APIWrapper
from logic.utilities import LoadConfig
from logic.api.health_check import HealthCheck


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self._api_request = APIWrapper()
        self.config = LoadConfig.return_file()

    def test_health_check(self):
        api_health_check = HealthCheck(self._api_request)
        result = api_health_check.health_check_api_get()
        body = result.json()
        data = api_health_check.return_data_in_health_check(body)
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(body["message"], self.config["test_health_check_message"])
        self.assertTrue(data["health"])


if __name__ == '__main__':
    unittest.main()
