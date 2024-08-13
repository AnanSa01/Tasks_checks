import logging
import unittest

from final_project_part_one_UI.infra.config_provider import ConfigProvider
from final_project_part_one_UI.infra.logging_basicConfig import LoggingSetup
from final_project_part_one_UI.infra.utilities import Utilities
from final_project_part_one_UI.infra.browser_wrapper import BrowserWrapper
from final_project_part_one_UI.logic.login_page import LoginPage
from final_project_part_one_UI.logic.sign_up_page import SignUpPage


class MyTestCase(unittest.TestCase):

    def setUp(self):
        """
        this setUp for opening a browser with a selected driver and going to the Sign-Up page.
        """
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver(self.browser.config["base_url"])
        logging.info(f'Opening a {self.browser.config["browser"]} web driver.')
        self.login_page = LoginPage(self.driver)
        self.login_page.click_on_sign_up_button_in_login_window()
        self.sign_up_page = SignUpPage(self.driver)

    def tearDown(self):
        """
        this tearDown just for closing the browser after finishing testing.
        """
        self.driver.quit()
        logging.info(f'---------- End of test. {self.browser.config["browser"]} web driver is closed. ----------\n')

    def test_sign_up_with_already_connected_user(self):
        """
        this function tests trying to sign up with input of an already connected user.
        -----
        test case   #: 004
        requirement #: 003
        """
        logging.info("---------- Initialize Test: signing up with already connected user ----------")
        self.config = ConfigProvider.load_from_file('../config.json')
        self.sign_up_page.write_in_your_name_field(self.config["your_name_input"])
        self.sign_up_page.write_in_email_input(self.config["email"])
        self.sign_up_page.write_in_password_and_re_enter_password_flow(self.config["password"])
        self.sign_up_page.click_on_create_account_button()
        self.assertTrue(self.sign_up_page.alert_message_for_sign_up(), "Error! Should NOT be able to connect")
        logging.info("assertTrue if alert message is displayed")

    def test_invalid_email_sign_up(self):
        """
        this function tests signing up with invalid email input.
        -----
        test case   #: 005
        requirement #: 003
        """
        logging.info("---------- Initialize Test: invalid Email sign up ----------")
        self.sign_up_page.write_in_your_name_field(Utilities.generate_random_string_just_text(5))
        self.sign_up_page.write_in_email_input(Utilities.generate_random_string_just_punctuation(10))
        self.sign_up_page.write_in_password_and_re_enter_password_flow(Utilities.generate_random_string_just_numbers(8))
        self.sign_up_page.click_on_create_account_button()
        self.assertTrue(self.sign_up_page.alert_message_for_sign_up(), "Error! Should NOT be able to connect")
        logging.info("assertTrue if alert message is displayed")

    def test_password_not_match_re_enter_password(self):
        """
        this function tests input of password not matching input of re-enter password.
        -----
        test case   #: 006
        requirement #: 003
        """
        logging.info("---------- Initialize Test: password not matching re-entering password ----------")
        self.sign_up_page.write_in_your_name_field(Utilities.generate_random_string_just_text(5))
        self.config = ConfigProvider.load_from_file('../config.json')
        self.sign_up_page.write_in_email_input(self.config["invalid_email"])
        self.sign_up_page.write_in_just_password_input(Utilities.generate_random_string_just_numbers(8))
        self.sign_up_page.write_in_just_re_enter_password_input(Utilities.generate_random_string_just_numbers(9))
        self.sign_up_page.click_on_create_account_button()
        self.assertTrue(self.sign_up_page.alert_message_for_sign_up(), "Error! Should NOT be able to connect")
        logging.info("assertTrue if alert message is displayed")

    def test_password_too_short_to_enter(self):
        """
        this function tests entering password that is too short (less than 6 characters).
        -----
        test case   #: 007
        requirement #: 003
        """
        logging.info("---------- Initialize Test: password too short (at least 6 characters) ----------")
        self.sign_up_page.write_in_your_name_field(Utilities.generate_random_string_just_text(5))
        self.config = ConfigProvider.load_from_file('../config.json')        
        self.sign_up_page.write_in_email_input(self.config["invalid_email"]) 
        self.sign_up_page.write_in_password_and_re_enter_password_flow(Utilities.generate_random_string_just_numbers(4))
        self.sign_up_page.click_on_create_account_button()
        self.assertTrue(self.sign_up_page.alert_message_for_sign_up(), "Error! Should NOT be able to connect")
        logging.info("assertTrue if alert message is displayed")


if __name__ == '__main__':
    unittest.main()
