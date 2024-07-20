import unittest

from infra.api.api_wrapper import APIWrapper
from logic.utilities import LoadConfig
from logic.api.get_job_details import GetJobDetails


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self._api_request = APIWrapper()
        self.config = LoadConfig.return_file()

    def test_get_job_details(self):
        api_get_job_details = GetJobDetails(self._api_request)
        result = api_get_job_details.find_job_details_api_get()
        body = result.json()
        data = api_get_job_details.return_data_in_find_job_details(body)
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(data["title"], self.config["get_job_details_check_title"])



if __name__ == '__main__':
    unittest.main()