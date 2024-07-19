import unittest

from infra.api.api_wrapper import APIWrapper
from logic.api.search_employees_NS import SearchEmployees


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self._api_request = APIWrapper()

    def test_search_employees(self):
        api_search_employees = SearchEmployees(self._api_request)
        result = api_search_employees.search_employees_api_get()
        body = result.json()
        print(body)
        # data = body["data"]
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(body["message"], "")

if __name__ == '__main__':
    unittest.main()
