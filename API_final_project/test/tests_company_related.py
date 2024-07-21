import time
import unittest

import logging
from infra.logging_basicConfig import LoggingSetup

from infra.api.api_wrapper import APIWrapper
from logic.api.get_company_employees_count_POST import GetCompanyEmployeesCount
from logic.api.get_company_jobs_POST import GetCompanyJobs
from logic.api.get_hiring_team import GetHiringTeam
from logic.api.get_job_details import GetJobDetails
from logic.api.health_check import HealthCheck
from logic.utilities import LoadConfig


class MyTestCase(unittest.TestCase):

    def setUp(self):
        """
        request to get API data using APIWrapper, and load json file.
        """
        self._api_request = APIWrapper()
        self.config = LoadConfig.return_file()

    def tearDown(self):
        logging.info(f'---------- End of test.\n')

    def test_get_company_employees_count_POST(self):
        """
        this function tests returning company employees count using POST
        -----
        test case   #: 001
        requirement #: 001
        """
        logging.info("---------- Initialize Test: get company employees count (using POST) ----------")
        api_get_company_employees_count = GetCompanyEmployeesCount(self._api_request)
        query_string = self.config["get_company_employees_count_query_string"]
        result = api_get_company_employees_count.get_company_employees_count_api_post(query_string)
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.body["message"], "")

    def test_get_company_job_POST(self):
        """
        this function tests getting company job using POST
        -----
        test case   #: 002
        requirement #: 001
        """
        logging.info("---------- Initialize Test: get company job (using POST) ----------")
        api_get_company_jobs = GetCompanyJobs(self._api_request)
        company_name = self.config["get_company_jobs_name"]
        query_string = self.config["get_company_jobs_query_string"]
        result = api_get_company_jobs.get_company_jobs_api_post(company_name, query_string)
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.body["message"], "")

    def test_get_hiring_team_GET(self):
        """
        this function tests returning hiring team using GET
        -----
        test case   #: 003
        requirement #: 001
        """
        logging.info("---------- Initialize Test: get hiring team (using GET) ----------")
        api_get_hiring_team = GetHiringTeam(self._api_request)
        hiring_team_id = self.config["get_hiring_team_id"]
        result = api_get_hiring_team.get_hiring_team_api_get(hiring_team_id)
        body = result.json()
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(body["message"], self.config["get_hiring_team_message"])
        self.assertTrue(body["success"])

    def test_health_check_GET(self):
        """
        this function returns health check for employee using GET
        -----
        test case   #: 004
        requirement #: 001
        """
        logging.info("---------- Initialize Test: get health check (using GET) ----------")
        api_health_check = HealthCheck(self._api_request)
        result = api_health_check.health_check_api_get()
        body = result.json()
        data = api_health_check.return_data_in_health_check(body)
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(body["message"], self.config["test_health_check_message"])
        self.assertTrue(data["health"])

    def test_get_job_details_by_id_GET(self):
        """
        this function tests getting job details using GET
        -----
        test case   #: 005
        requirement #: 001
        """
        logging.info("---------- Initialize Test: get job details (using GET) ----------")
        api_get_job_details = GetJobDetails(self._api_request)
        job_id = self.config["get_job_detail_id"]
        result = api_get_job_details.find_job_details_api_get(job_id)
        body = result.json()
        data = api_get_job_details.return_data_in_find_job_details(body)
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(body["message"], "")
        self.assertEqual(data["id"], job_id)


if __name__ == '__main__':
    unittest.main()
