import unittest

from infra.api.api_wrapper import APIWrapper
from logic.utilities import LoadConfig
from logic.api.get_company_by_domain import GetCompanyByDomain


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self._api_request = APIWrapper()
        self.config = LoadConfig.return_file()

    def test_get_company_by_domain(self):
        api_get_company_by_domain = GetCompanyByDomain(self._api_request)
        result = api_get_company_by_domain.get_company_by_domain()
        body = result.json()
        data = api_get_company_by_domain.return_data_in_get_company_by_domain(body)
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(body["message"], "")
        self.assertEqual(data["name"], self.config["get_company_by_domain_check_name"])


if __name__ == '__main__':
    unittest.main()
