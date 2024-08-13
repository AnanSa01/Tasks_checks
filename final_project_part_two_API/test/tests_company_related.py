import unittest

import logging

from final_project_part_two_API.infra.logging_basicConfig import LoggingSetup
from final_project_part_two_API.infra.api.api_wrapper import APIWrapper
from final_project_part_two_API.logic.api.get_company_employees_count_POST import GetCompanyEmployeesCount
from final_project_part_two_API.logic.api.get_company_jobs_POST import GetCompanyJobs
from final_project_part_two_API.logic.api.get_hiring_team import GetHiringTeam
from final_project_part_two_API.logic.api.get_job_details import GetJobDetails
from final_project_part_two_API.logic.api.health_check import HealthCheck
from final_project_part_two_API.logic.utilities import LoadConfig


class MyTestCase(unittest.TestCase):

    def setUp(self):
        """
        request to get API data using APIWrapper, and load json file.
        """
        self._api_request = APIWrapper()
        self.config = LoadConfig.return_file()

    def tearDown(self):
        logging.info(f'End of test.\n')

    def test_get_company_employees_count_POST(self):
        """
        this function tests returning company employees count using POST
        -----
        test case   #: 001
        requirement #: 001
        """
        logging.info("---------- Initialize Test: get company employees count (using POST) ----------")
        api_get_company_employees_count = GetCompanyEmployeesCount(self._api_request)
        payload = self.config["get_company_employees_count_payload"]
        result = api_get_company_employees_count.get_company_employees_count_api_post(payload)
        self.assertEqual(result.status_code, self.config["status_code_passed"])
        self.assertEqual(result.body["message"], self.config["valid_empty_message"])

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
        payload = self.config["get_company_jobs_payload"]
        result = api_get_company_jobs.get_company_jobs_api_post(company_name, payload)
        self.assertEqual(result.status_code, self.config["status_code_passed"])
        self.assertEqual(result.body["message"], self.config["valid_empty_message"])

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
        self.assertEqual(result.status_code, self.config["status_code_passed"])
        self.assertEqual(result.body["message"], self.config["valid_success_message"])

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
        self.assertEqual(result.status_code, self.config["status_code_passed"])
        self.assertEqual(result.body["message"], self.config["valid_success_message"])

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
        data = api_get_job_details.return_data_in_find_job_details(result.body)
        self.assertEqual(result.status_code, self.config["status_code_passed"])
        self.assertEqual(data["id"], job_id)


if __name__ == '__main__':
    unittest.main()
