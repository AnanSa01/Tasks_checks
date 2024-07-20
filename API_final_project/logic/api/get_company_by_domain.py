import logging

from requests import RequestException

from infra.logging_basicConfig import LoggingSetup

from logic.api._base_init import BaseInit


class GetCompanyByDomain(BaseInit):
    def __init__(self, request):
        super().__init__(request)

    def get_company_by_domain_api_get(self):
        """
        this function returns company information by domain using GET
        """
        try:
            return self._request.get_request(
                f"{self.config["base_url"]}/get-company-by-domain?{self.config["get_company_by_domain_function"]}",
                self.config["header"])

        except RequestException:
            logging.error("Error in receiving API data from 'get_company_by_domain' function")

    def return_data_in_get_company_by_domain(self, body_of_get_company_by_domain):
        """
        this function returns the dict key to data
        :param body_of_get_company_by_domain: body in json for company by domain function
        :return: data key
        """
        return body_of_get_company_by_domain["data"]
