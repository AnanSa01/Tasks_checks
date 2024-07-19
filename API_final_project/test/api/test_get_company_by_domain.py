import unittest

from infra.api.api_wrapper import APIWrapper
from logic.api.get_company_by_domain import GetCompanyByDomain


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self._api_request = APIWrapper()

    def test_get_company_by_domain(self):
        api_get_company_by_domain = GetCompanyByDomain(self._api_request)
        result = api_get_company_by_domain.get_company_by_domain()
        body = result.json()
        print(body)
        # data = body["data"]  it changes everytime
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(body["message"], "")


if __name__ == '__main__':
    unittest.main()
