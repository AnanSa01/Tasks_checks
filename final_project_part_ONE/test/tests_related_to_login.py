import logging
import time
import unittest

from infra.config_provider import ConfigProvider
from infra.logging_basicConfig import LoggingSetup
from infra.browser_wrapper import BrowserWrapper
from logic.home_page import HomePage
from logic.login_page import LoginPage
from logic.sign_up_page import SignUpPage


class MyTestCase(unittest.TestCase):

    def setUp(self):
        """
        this setUp just for opening a browser with a selected driver
        """
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver(self.browser.config["base_url"])
        logging.info(f'Opening a {self.browser.config["browser"]} web driver.')
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        """
        this tearDown just for closing the browser after finishing testing.
        """
        self.driver.quit()
        logging.info(f'---------- End of test. {self.browser.config["browser"]} web driver is closed. ----------\n')

    def test_valid_login(self):
        """
        this function tests valid login input for a user.
        -----
        test case   #: 001
        requirement #: 001
        """
        logging.info("---------- Initialize Test: valid login ----------")
        self.config = ConfigProvider.load_from_file('../config.json')
        self.login_page.write_in_email_input_field(self.config["email"])
        self.login_page.write_in_password_input_field(self.config["password"])
        self.login_page.click_on_sign_in_button()
        home_page = HomePage(self.driver)
        self.assertTrue(home_page.check_if_header_displayed(), "Error! Should NOT be able to connect")
        logging.info("assertTrue if home header is displayed.")

    def test_not_adding_password_in_login(self):
        """
        this function ensures the website does not connect when only entering user input without password.
        -----
        test case   #: 002
        requirement #: 002
        """
        logging.info("---------- Initialize Test: not adding password in login ----------")
        self.config = ConfigProvider.load_from_file('../config.json')
        self.login_page.write_in_email_input_field(self.config["invalid_email"])
        self.login_page.click_on_sign_in_button()
        self.assertTrue(self.login_page.alert_message_for_login(), "Error! Should NOT be able to connect")
        logging.info("assertTrue if alert message is displayed")

    def test_not_adding_password_nor_email_in_login(self):
        """
        this function ensures the website does not connect when NOT entering user input nor password.
        -----
        test case   #: 003
        requirement #: 002
        """
        logging.info("---------- Initialize Test: not adding password in login ----------")
        self.login_page.click_on_sign_in_button()
        self.assertTrue(self.login_page.alert_message_for_login(), "Error! Should NOT be able to connect")
        logging.info("assertTrue if alert message is displayed")


if __name__ == '__main__':
    unittest.main()
