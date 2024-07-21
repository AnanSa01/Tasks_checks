import logging

from requests import RequestException

from infra.logging_basicConfig import LoggingSetup

from logic.api.base_init import BaseInit


class GetProfilePosts(BaseInit):
    def __init__(self, request):
        super().__init__(request)

    def get_profile_posts_api_get(self, profile_username):
        """
        this function returns profile posts using GET
        """
        try:
            return self._request.get_request(
                f"{self.config["base_url"]}/get-profile-posts?username={profile_username}",
                self.config["header"])

        except RequestException:
            logging.error("Error in receiving API data from 'get_profile_posts' function")

    def return_user_in_get_profile_posts(self, body_of_get_profile_posts):
        """
        this function returns the dict key to user
        :param body_of_get_profile_posts: body in json for "get profile posts" function
        :return: author["username"]
        """
        data = body_of_get_profile_posts["data"]
        author = data[0]["author"]
        return author["username"]