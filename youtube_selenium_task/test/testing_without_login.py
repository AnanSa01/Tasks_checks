import unittest

from youtube_selenium_task.infra.browser_wrapper import BrowserWrapper
from youtube_selenium_task.infra.config_provider import ConfigProvider
from youtube_selenium_task.logic.history_page import HistoryPage
from youtube_selenium_task.logic.home_page import HomePage
from youtube_selenium_task.logic.login_page import LoginPage


class MyTestCase(unittest.TestCase):

    def setUp(self):
        """
        this function sets up all tests below
        """
        # ARRANGE
        self.config = ConfigProvider.load_from_file('../config.json')
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver(self.browser.config["base_url"])
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        """
        this function closes driver
        """
        self.driver.close()

    def test_switch_to_dark_mode(self):
        """
        this function tests turning YouTube into dark mode
        """
        # ACT
        self.home_page.click_on_settings_button()
        self.home_page.click_on_settings_appearance_button()
        self.home_page.click_on_settings_appearance_dark_mode_button()
        self.home_page.click_on_dark_settings_button()
        # ASSERT
        self.assertIn(self.config["switch_to_dark_mode_check"], self.home_page.return_status_appearance_button())

    def test_search_in_different_languages(self):
        """
        this function tests getting results in different languages other than english
        """
        # ACT
        self.home_page.click_on_search_input()
        self.home_page.write_in_search_input(self.config["search_in_arabic_input"])
        self.home_page.click_on_search_logo_button()
        # ASSERT
        self.assertIn(self.config["search_in_arabic_input"], self.home_page.return_first_video_text())

    def test_invalid_input_for_login(self):
        """
        this function tests negative response for invalid login
        """
        # ACT
        self.home_page.click_on_sign_in_button()
        login_page = LoginPage(self.driver)
        login_page.click_on_sign_in_field()
        login_page.write_input_in_sign_in_field(self.config["invalid_input_login"])  # invalid input
        login_page.click_on_next_button_on_first_page()
        # ASSERT
        self.assertEqual(login_page.return_login_logo(), self.config["invalid_input_login_logo"])

    def test_clear_search_history(self):
        """
        this function tests clearing search history
        """
        # ACT
        self.home_page.click_on_history_button()
        history_page = HistoryPage(self.driver)
        history_page.click_on_clear_history_button()
        history_page.click_on_pop_clear_history_button()
        # ASSERT
        self.assertEqual(history_page.return_text_message_clear_history(), self.config["clear_search_history_message"])

    def test_change_language_to_hebrew(self):
        """
        this function tests changing text language of website
        """
        # ACT
        self.home_page.click_on_settings_button()
        self.home_page.click_on_language_button()
        self.home_page.click_on_hebrew_language()
        # ASSERT
        self.assertEqual(self.home_page.return_hebrew_message(), self.config["change_language_to_hebrew_message"])


if __name__ == '__main__':
    unittest.main()

