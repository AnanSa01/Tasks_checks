import unittest

from infra.api.api_wrapper import APIWrapper
from logic.api.get_company_jobs_POST import GetCompanyJobs


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.api_request = APIWrapper()

    def test_get_company_job(self):
        api_get_company_jobs = GetCompanyJobs(self.api_request)
        result = api_get_company_jobs.api_post_get_company_jobs()
        print(result.body)
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.body["message"], "")


if __name__ == '__main__':
    unittest.main()
