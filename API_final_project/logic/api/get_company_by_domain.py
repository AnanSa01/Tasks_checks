from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider


class GetCompanyByDomain:
    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider.load_from_file("../../config.json")

    def get_company_by_domain(self):
        return self._request.get_request(
            f"{self.config["base_url"]}/get-company-by-domain?{self.config["get_company_by_domain_function"]}",
            self.config["header"])