import unittest

from infra.api.api_wrapper import APIWrapper
from logic.api.search_employees import SearchEmployees


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self._api_request = APIWrapper()

    def test_search_employees(self):
        api_search_employees = SearchEmployees(self._api_request)
        result = api_search_employees.search_employees_api_get()
        body = result.json()
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(body["message"], "")
        self.assertTrue("success")


if __name__ == '__main__':
    unittest.main()
