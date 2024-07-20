from logic.api._base_init import BaseInit


class GetJobDetails(BaseInit):
    def __init__(self, request):
        super().__init__(request)

    def find_job_details_api_get(self):
        return self._request.get_request(
            f"{self.config["base_url"]}/get-job-details?{self.config["get_job_details_function"]}",
            self.config["header"])

    def return_data_in_find_job_details(self, body_of_find_job_details):
        return body_of_find_job_details["data"]
