import logging
import time
import unittest

from infra.logging_basicConfig import LoggingSetup
from infra.browser_wrapper import BrowserWrapper
from logic.home_page import HomePage
from logic.login_page import LoginPage
from logic.sign_up_page import SignUpPage


class MyTestCase(unittest.TestCase):

    # this setUp just for opening a browser with a selected driver
    def setUp(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver(self.browser.config["base_url"])
        logging.info(f'Opening a {self.browser.config["browser"]} web driver.')

    # this tearDown just for closing the browser after finishing testing.
    def tearDown(self):
        self.driver.quit()
        logging.info(f'{self.browser.config["browser"]} web driver is closed.\n')

    # This test is to ensure the basic activity of signing in.
    def test_valid_login(self):
        logging.info("*TEST* valid login -")
        login_page = LoginPage(self.driver)
        logging.info("Sending driver to LoginPage")
        login_page.write_in_email_input_field("aaafortesting@gmail.com")
        logging.info("Input valid Email address")
        login_page.write_in_password_input_field("aaafortesting123456789")
        logging.info("Input valid password")
        login_page.click_on_sign_in_button()
        logging.info("Click in sign in button function")
        home_page = HomePage(self.driver)
        logging.info("Switching driver to HomePage")
        self.assertTrue(home_page.check_if_header_displayed(), "Error! Should NOT be able to connect")
        logging.info("assertTrue if home header is displayed.")

    # This test is to ensure that the website does not let the user sign in with no password input.
    def test_not_adding_password_in_login(self):
        logging.info("*TEST* not adding password in login -")
        login_page = LoginPage(self.driver)
        logging.info("Sending driver to LoginPage")
        login_page.write_in_email_input_field("fortesting@gmail.com")
        logging.info("Input valid Email address")
        login_page.click_on_sign_in_button()
        logging.info("Click in sign in button function")
        home_page = HomePage(self.driver)
        logging.info("Switching driver to HomePage")
        self.assertTrue(login_page.alert_message_for_login(), "Error! Should NOT be able to connect")
        logging.info("assertTrue if alert message is displayed")

    # This test is to ensure that the website does not let the user sign in with no password nor email input.
    def test_not_adding_password_nor_email_in_login(self):
        logging.info("*TEST* not adding password in login -")
        login_page = LoginPage(self.driver)
        logging.info("Sending driver to LoginPage")
        login_page.click_on_sign_in_button()
        logging.info("Click in sign in button function")
        home_page = HomePage(self.driver)
        logging.info("Switching driver to HomePage")
        self.assertTrue(login_page.alert_message_for_login(), "Error! Should NOT be able to connect")
        logging.info("assertTrue if alert message is displayed")


if __name__ == '__main__':
    unittest.main()
