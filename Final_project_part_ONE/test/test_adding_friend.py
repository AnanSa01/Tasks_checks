import time
import unittest

from infra.browser_wrapper import BrowserWrapper
from logic.friends_page import FriendsPage
from logic.home_page import HomePage
from logic.login_page import LoginPage


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver(self.browser.config["base_url"])
        self.login_page = LoginPage(self.driver)
        self.login_page.valid_login_flow()
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_add_a_friend_and_then_delete_request(self):
        print("Test adding a friend and then deleting the request -")
        self.home_page.click_on_friends_button()
        friends_page = FriendsPage(self.driver)
        search_friend_name = "Tzahi"
        friends_page.search_for_a_person_flow(search_friend_name)
        friends_page.add_as_a_friend_first_person()
        time.sleep(2)
        friends_page.click_on_pictures_button()
        friends_page.click_on_unfollow_button()
        time.sleep(2)
        friends_page.click_on_unfollow_confirm_button()
        time.sleep(2)
        self.assertEqual(friends_page.return_follow_button_state(), "Follow", "Error! still followed.")


if __name__ == '__main__':
    unittest.main()
