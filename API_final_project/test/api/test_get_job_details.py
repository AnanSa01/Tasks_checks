import unittest

from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from logic.api.get_job_details import GetJobDetails


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self._api_request = APIWrapper()
        self.config = ConfigProvider.load_from_file('../../config.json')

    def test_get_job_details(self):
        api_get_job_details = GetJobDetails(self._api_request)
        result = api_get_job_details.find_job_details_api_get()
        body = result.json()
        data = body["data"]
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(data["title"], self.config["get_job_details_check_title"])



if __name__ == '__main__':
    unittest.main()
