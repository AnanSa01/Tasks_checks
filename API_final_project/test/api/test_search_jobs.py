import unittest

from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from logic.api.search_jobs import SearchJobs


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self._api_request = APIWrapper()
        self.config = ConfigProvider.load_from_file('../../config.json')

    def test_search_jobs(self):
        api_search_jobs = SearchJobs(self._api_request)
        result = api_search_jobs.search_jobs_api_get()
        body = result.json()
        print(body)
        #data = body["data"]  it changes everytime
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(body["message"], "")

    def test_search_jobs_v2(self):
        api_search_jobs_v2 = SearchJobs(self._api_request)
        result = api_search_jobs_v2.search_jobs_v2_api_get()
        body = result.json()
        print(body)
        # data = body["data"]  it changes everytime
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(body["message"], "")



if __name__ == '__main__':
    unittest.main()
