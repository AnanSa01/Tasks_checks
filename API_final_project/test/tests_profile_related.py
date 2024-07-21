import unittest

import logging
from infra.logging_basicConfig import LoggingSetup

from infra.api.api_wrapper import APIWrapper
from logic.api.get_given_recommendations import GetGivenRecommendations
from logic.api.get_post_reactions_POST import GetPostReactions
from logic.api.get_profile_data import GetProfileData
from logic.api.get_profile_likes import GetProfileLikes
from logic.api.get_profile_posts import GetProfilePosts
from logic.api.get_profile_posts_comments import GetProfilePostsComments
from logic.api.search_people import SearchPeople
from logic.utilities import LoadConfig


class MyTestCase(unittest.TestCase):
    def setUp(self):
        """
        request to get API data using APIWrapper, and load json file.
        """
        self._api_request = APIWrapper()
        self.config = LoadConfig.return_file()

    def tearDown(self):
        logging.info(f'---------- End of test.\n')

    def test_get_profile_data_GET(self):
        """
        this function tests getting profile data using GET
        -----
        test case   #: 006
        requirement #: 002
        """
        logging.info("---------- Initialize Test: get company by domain (using GET) ----------")
        api_get_profile_data = GetProfileData(self._api_request)
        profile_username = self.config["get_profile_data_username"]
        result = api_get_profile_data.get_profile_data_api_get(profile_username)
        body = result.json()
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(body["username"], profile_username)

        geo = api_get_profile_data.return_geo_in_get_profile_data(body)
        self.assertEqual(body["firstName"], self.config["get_profile_data_check_first_name"])
        self.assertEqual(geo["country"], self.config["get_profile_data_check_country"])

    def test_search_people_GET(self):
        """
        this function tests searching people using GET
        -----
        test case   #: 007
        requirement #: 002
        """
        logging.info("---------- Initialize Test: search people (using GET) ----------")
        api_search_for_people = SearchPeople(self._api_request)
        name_for_search = self.config["search_people_name"]
        place_for_search = self.config["search_people_place_wp"]
        result = api_search_for_people.search_people_api_get(name_for_search, place_for_search)
        body = result.json()
        items = api_search_for_people.return_items_in_search_people(body)
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(body["message"], "")
        self.assertIn(name_for_search, items[0]["fullName"])

    def test_get_profile_posts_GET(self):
        """
        this function tests getting profile posts using GET
        -----
        test case   #: 008
        requirement #: 002
        """
        logging.info("---------- Initialize Test: get profile posts (using GET) ----------")
        api_get_profile_posts = GetProfilePosts(self._api_request)
        profile_username_request = self.config["get_profile_posts_username"]
        result = api_get_profile_posts.get_profile_posts_api_get(profile_username_request)
        body = result.json()
        username_from_response = api_get_profile_posts.return_user_in_get_profile_posts(body)
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(body["message"], "")
        self.assertEqual(profile_username_request, username_from_response)

    def test_get_profile_likes_GET(self):
        """
        this function tests getting profile likes using GET
        -----
        test case   #: 009
        requirement #: 002
        """
        logging.info("---------- Initialize Test: get profile likes (using GET) ----------")
        api_get_profile_likes = GetProfileLikes(self._api_request)
        profile_username_request = self.config["get_profile_likes_username"]
        result = api_get_profile_likes.get_profile_likes_api_get(profile_username_request)
        body = result.json()
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(body["message"], "")

    def test_profile_posts_comments_by_urn_GET(self):
        """
        this function tests getting posts comments using GET
        -----
        test case   #: 010
        requirement #: 002
        """
        logging.info("---------- Initialize Test: profile posts comments (using GET) ----------")
        api_profile_posts_comments = GetProfilePostsComments(self._api_request)
        profile_urn = self.config["get_profile_posts_comments_urn"]
        result = api_profile_posts_comments.get_profile_posts_comments_api_get(profile_urn)
        body = result.json()
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(body["message"], "")
        self.assertTrue(body["success"])

    def test_get_given_recommendations_GET(self):
        """
        this function tests giving recommendations using GET
        -----
        test case   #: 011
        requirement #: 002
        """
        logging.info("---------- Initialize Test: get given recommendations (using GET) ----------")
        api_get_given_recommendations = GetGivenRecommendations(self._api_request)
        profile_username = self.config["get_given_recommendations_username"]
        result = api_get_given_recommendations.get_given_recommendations_api_get(profile_username)
        body = result.json()
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(body["message"], "")

    def test_get_post_reactions_POST(self):
        """
        this function tests getting post reaction using POST
        -----
        test case   #: 012
        requirement #: 002
        """
        logging.info("---------- Initialize Test: get post reactions (using POST) ----------")
        api_get_post_reactions = GetPostReactions(self._api_request)
        query_string = self.config["get_post_reactions_query_string"]
        result = api_get_post_reactions.get_post_reactions_api_post(query_string)
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.body["message"], "")


if __name__ == '__main__':
    unittest.main()
