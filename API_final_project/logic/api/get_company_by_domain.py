from logic.api._base_init import BaseInit


class GetCompanyByDomain(BaseInit):
    def __init__(self, request):
        super().__init__(request)

    def get_company_by_domain(self):
        return self._request.get_request(
            f"{self.config["base_url"]}/get-company-by-domain?{self.config["get_company_by_domain_function"]}",
            self.config["header"])

    def return_data_in_get_company_by_domain(self, body_of_get_company_by_domain):
        return body_of_get_company_by_domain["data"]
