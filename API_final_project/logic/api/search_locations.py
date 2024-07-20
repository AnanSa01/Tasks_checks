from logic.api._base_init import BaseInit


class SearchLocations(BaseInit):
    def __init__(self, request):
        super().__init__(request)

    def search_locations_api_get(self):
        return self._request.get_request(
            f"{self.config["base_url"]}/search-locations?{self.config["search_locations_function"]}",
            self.config["header"])

    def return_items_in_search_locations(self, body_of_search_locations):
        data = body_of_search_locations["data"]
        return data["items"]


