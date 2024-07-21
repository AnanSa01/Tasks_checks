import unittest

import logging
from infra.logging_basicConfig import LoggingSetup

from infra.api.api_wrapper import APIWrapper
from logic.api.find_email_address import FindEmailAddress
from logic.api.search_employees import SearchEmployees
from logic.api.search_jobs import SearchJobs
from logic.api.search_locations import SearchLocations
from logic.api.search_post_by_hashtag_POST import SearchPostByHashtag
from logic.api.search_post_by_keyword_POST import SearchPostByKeyword
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

    def test_search_employees_GET(self):
        """
        this function tests searching for employees using GET
        -----
        test case   #: 013
        requirement #: 003
        """
        logging.info("---------- Initialize Test: search employees (using GET) ----------")
        api_search_employees = SearchEmployees(self._api_request)
        company_id = self.config["search_employees_companyId"]
        company_place_wp = self.config["search_employees_place_wp"]
        result = api_search_employees.search_employees_api_get(company_id, company_place_wp)
        body = result.json()
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertTrue("success")

    def test_find_email_address_GET(self):
        """
        this function tests returning email address using GET
        -----
        test case   #: 014
        requirement #: 003
        """
        logging.info("---------- Initialize Test: find email address (using GET) ----------")
        api_find_email_address = FindEmailAddress(self._api_request)
        find_username = self.config["find_email_address_username"]
        result = api_find_email_address.find_email_address_api_get(find_username)
        body = result.json()
        profile_data = api_find_email_address.return_profile_data_in_find_email_address(body)
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(profile_data["username"], find_username)

    def test_search_jobs_GET(self):
        """
        this function tests searching for jobs using GET
        -----
        test case   #: 015
        requirement #: 003
        """
        logging.info("---------- Initialize Test: search jobs (using GET) ----------")
        api_search_jobs = SearchJobs(self._api_request)
        search_jobs_keyword = self.config["search_jobs_keyword"]
        search_jobs_location_id = self.config["search_jobs_locationId"]
        result = api_search_jobs.search_jobs_api_get(search_jobs_keyword, search_jobs_location_id)
        body = result.json()
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(body["message"], "")

    def test_search_jobs_v2_GET(self):
        """
        this function tests searching for jobs using GET
        -----
        test case   #: 016
        requirement #: 003
        """
        logging.info("---------- Initialize Test: search jobs v2 (using GET) ----------")
        api_search_jobs_v2 = SearchJobs(self._api_request)
        search_jobs_keyword = self.config["search_jobs_keyword"]
        search_jobs_location_id = self.config["search_jobs_locationId"]
        result = api_search_jobs_v2.search_jobs_v2_api_get(search_jobs_keyword, search_jobs_location_id)
        body = result.json()
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(body["message"], "")

    def test_search_locations_GET(self):
        """
        this function tests searching locations using GET
        -----
        test case   #: 017
        requirement #: 003
        """
        logging.info("---------- Initialize Test: search locations (using GET) ----------")
        api_search_locations = SearchLocations(self._api_request)
        location_name = self.config["search_locations_place"]
        result = api_search_locations.search_locations_api_get(location_name)
        body = result.json()
        items = api_search_locations.return_items_in_search_locations(body)
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(body["message"], "")
        self.assertTrue("success")
        self.assertIn(location_name, items[0]["name"])

    def test_search_post_by_hashtag_POST(self):
        """
        this function tests searching post by hashtag using POST
        -----
        test case   #: 018
        requirement #: 003
        """
        logging.info("---------- Initialize Test: search post by hashtag (using POST) ----------")
        api_search_post_by_hashtag = SearchPostByHashtag(self._api_request)
        query_string = self.config["search_post_by_hashtag_query_string"]
        result = api_search_post_by_hashtag.search_post_by_hashtag_api_post(query_string)
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.body["message"], "")
        self.assertTrue(result.body["success"])

    def test_search_post_by_keyword_POST(self):
        """
        this function tests searching post by keyword using POST
        -----
        test case   #: 019
        requirement #: 003
        """
        logging.info("---------- Initialize Test: search post by keyword (using POST) ----------")
        api_search_post_by_keyword = SearchPostByKeyword(self._api_request)
        query_string = self.config["search_post_by_keyword_query_string"]
        result = api_search_post_by_keyword.search_post_by_keyword_api_post(query_string)
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.body["message"], "")
        self.assertTrue(result.body["success"])


if __name__ == '__main__':
    unittest.main()
