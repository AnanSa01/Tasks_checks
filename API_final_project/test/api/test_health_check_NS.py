import unittest

from infra.api.api_wrapper import APIWrapper
from logic.api.health_check_NS import HealthCheck


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self._api_request = APIWrapper()

    def test_health_check(self):
        api_health_check = HealthCheck(self._api_request)
        result = api_health_check.health_check_api_get()
        body = result.json()
        print(body)
        # data = body["data"]
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        #self.assertEqual(body["message"], "") should have other message


if __name__ == '__main__':
    unittest.main()
