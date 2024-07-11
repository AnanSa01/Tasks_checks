import time
import unittest

from selenium.webdriver.common.by import By

from infra.browser_wrapper import BrowserWrapper
from logic.base_app_page import BaseAppPage
from logic.home_page import HomePage
from logic.login_page import LoginPage


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver(self.browser.config["base_url"])

    def test_switch_to_dark_mode(self):
        home_page = HomePage(self.driver)
        home_page.click_on_settings_button()
        time.sleep(2)
        home_page.click_on_settings_appearance_button()
        home_page.click_on_settings_appearance_dark_mode_button()

    def test_search_in_arabic(self):
        home_page = HomePage(self.driver)
        home_page.click_on_search_input()
        home_page.write_in_search_input("يورو")
        home_page.click_on_search_logo_button()

    def test_invalid_input_for_login(self):
        home_page = HomePage(self.driver)
        home_page.click_on_sign_in_button()
        login_page = LoginPage(self.driver)
        login_page.click_on_sign_in_field()
        login_page.write_input_in_sign_in_field("@@@@@")  # invalid input
        login_page.click_on_next_button_on_first_page()

    def test_like_and_dislike_functionality(self):
        home_page = HomePage(self.driver)
        home_page.click_on_explore_sports_button()


