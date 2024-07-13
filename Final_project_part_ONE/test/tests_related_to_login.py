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
        print("Test valid login -")
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
        print("Test not adding password in login -")
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
        print("Test not adding password in login -")
        logging.info("*TEST* not adding password in login -")
        login_page = LoginPage(self.driver)
        logging.info("Sending driver to LoginPage")
        login_page.click_on_sign_in_button()
        logging.info("Click in sign in button function")
        home_page = HomePage(self.driver)
        logging.info("Switching driver to HomePage")
        self.assertTrue(login_page.alert_message_for_login(), "Error! Should NOT be able to connect")
        logging.info("assertTrue if alert message is displayed")

        # This test is to ensure that the website does not let the user sign up with input of an already connected user.
    def test_sign_up_with_already_connected_user(self):
        print("Test signing up with already connected user -")
        logging.info("*TEST* signing up with already connected user -")
        login_page = LoginPage(self.driver)
        logging.info("Sending driver to LoginPage")
        login_page.click_on_sign_up_button_in_login_window()
        logging.info("Click on sign up function")
        sign_up_page = SignUpPage(self.driver)
        logging.info("Switching Driver to SignUpPage")
        sign_up_page.write_in_your_name_field("A S")
        logging.info("Input valid name")
        sign_up_page.write_in_email_input("aaafortesting@gmail.com")
        logging.info("Input valid Email address")
        sign_up_page.write_in_password_and_re_enter_password_flow("aaafortesting123456789")
        logging.info("Input valid password")
        sign_up_page.click_on_create_account_button()
        logging.info("Click on create account function")
        self.assertTrue(sign_up_page.alert_message_for_sign_up(), "Error! Should NOT be able to connect")
        logging.info("assertTrue if alert message is displayed")

        # This test is to ensure that the website does not accept invalid Email input.
    def test_invalid_email_sign_up(self):
        print("Test invalid Email sign up -")
        logging.info("*TEST* invalid Email sign up -")
        login_page = LoginPage(self.driver)
        logging.info("Sending driver to LoginPage")
        login_page.click_on_sign_up_button_in_login_window()
        logging.info("Click on sign up function")
        sign_up_page = SignUpPage(self.driver)
        logging.info("Switching Driver to SignUpPage")
        sign_up_page.write_in_your_name_field("A S")
        logging.info("Input valid name")
        sign_up_page.write_in_email_input("@@@@@@@@@@@@@@@")
        logging.info("Input INVALID Email address")
        sign_up_page.write_in_password_and_re_enter_password_flow("0000000000")
        logging.info("Input valid password")
        sign_up_page.click_on_create_account_button()
        logging.info("Click on create account function")
        self.assertTrue(sign_up_page.alert_message_for_sign_up(), "Error! Should NOT be able to connect")
        logging.info("assertTrue if alert message is displayed")

        # This test is to ensure that the website does not connect when entering unmatched passwords input.
    def test_password_not_match_re_enter_password(self):
        print("Test password not matching re-entering password -")
        logging.info("*TEST* password not matching re-entering password -")
        login_page = LoginPage(self.driver)
        logging.info("Sending driver to LoginPage")
        login_page.click_on_sign_up_button_in_login_window()
        logging.info("Click on sign up function")
        sign_up_page = SignUpPage(self.driver)
        logging.info("Switching Driver to SignUpPage")
        sign_up_page.write_in_your_name_field("A S")
        logging.info("Input valid name")
        sign_up_page.write_in_email_input("fortesting@gmail.com")
        logging.info("Input valid Email address")
        sign_up_page.write_in_just_password_input("123456789")
        logging.info("Input password")
        sign_up_page.write_in_just_re_enter_password_input("987654321")
        logging.info("Re-enter password not matching the previous password")
        sign_up_page.click_on_create_account_button()
        logging.info("Click on create account function")
        self.assertTrue(sign_up_page.alert_message_for_sign_up(), "Error! Should NOT be able to connect")
        logging.info("assertTrue if alert message is displayed")

        # This test is to ensure that the website does not connect when entering too short password input.
    def test_password_too_short_to_enter(self):
        print("Test password too short (at least 6 characters) -")
        logging.info("*TEST* password too short (at least 6 characters) -")
        login_page = LoginPage(self.driver)
        logging.info("Sending driver to LoginPage")
        login_page.click_on_sign_up_button_in_login_window()
        logging.info("Click on sign up function")
        sign_up_page = SignUpPage(self.driver)
        logging.info("Switching Driver to SignUpPage")
        sign_up_page.write_in_your_name_field("A S")
        logging.info("Input valid Email address")
        sign_up_page.write_in_email_input("fortesting@gmail.com")
        logging.info("Input valid Email address")
        sign_up_page.write_in_password_and_re_enter_password_flow("00000")
        logging.info("Input TOO SHORT password")
        sign_up_page.click_on_create_account_button()
        logging.info("Click on create account function")
        self.assertTrue(sign_up_page.alert_message_for_sign_up(), "Error! Should NOT be able to connect")
        logging.info("assertTrue if alert message is displayed")


if __name__ == '__main__':
    unittest.main()
