import unittest

from infra.api.api_wrapper import APIWrapper
from logic.api.get_company_employees_count_POST import GetCompanyEmployeesCount


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.api_request = APIWrapper()

    def test_get_company_employees_count(self):
        api_get_company_employees_count = GetCompanyEmployeesCount(self.api_request)
        result = api_get_company_employees_count.api_post_get_company_employees_count()
        print(result.body)
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.body["message"], "")


if __name__ == '__main__':
    unittest.main()
