import time
import unittest

from infra.browser_wrapper import BrowserWrapper
from logic.home_page import HomePage
from logic.login_page import LoginPage
from logic.sign_up_page import SignUpPage


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver(self.browser.config["base_url"])

    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        login_page.write_in_email_input_field("aaafortesting@gmail.com")
        login_page.write_in_password_input_field("aaafortesting123456789")
        login_page.click_on_sign_in_button()
        home_page = HomePage(self.driver)
        self.assertTrue(home_page.check_if_header_displayed(), "Login FAILED!")

    def test_sign_up_with_already_connected_user(self):
        login_page = LoginPage(self.driver)
        login_page.click_on_sign_up_button_in_login_window()
        sign_up_page = SignUpPage(self.driver)
        sign_up_page.write_in_your_name_field("A S")
        sign_up_page.write_in_email_input("aaafortesting@gmail.com")
        sign_up_page.write_in_password_and_re_enter_password_flow("aaafortesting123456789")
        sign_up_page.click_on_create_account_button()
        self.assertTrue(sign_up_page.alert_message_for_sign_up(), "Error! Shouldn't be able to connect")

    def test_invalid_email_sign_up(self):
        login_page = LoginPage(self.driver)
        login_page.click_on_sign_up_button_in_login_window()
        sign_up_page = SignUpPage(self.driver)
        sign_up_page.write_in_your_name_field("A S")
        sign_up_page.write_in_email_input("@@@@@@@@@@@@@@@")
        sign_up_page.write_in_password_and_re_enter_password_flow("0000000000")
        sign_up_page.click_on_create_account_button()
        self.assertTrue(sign_up_page.alert_message_for_sign_up(), "Error! Shouldn't be able to connect")

    def test_password_not_match_re_enter_password(self):
        login_page = LoginPage(self.driver)
        login_page.click_on_sign_up_button_in_login_window()
        sign_up_page = SignUpPage(self.driver)
        sign_up_page.write_in_your_name_field("A S")
        sign_up_page.write_in_email_input("aaafortesting@gmail.com")
        sign_up_page.write_in_just_password_input("123456789")
        sign_up_page.write_in_just_re_enter_password_input("987654321")
        sign_up_page.click_on_create_account_button()
        self.assertTrue(sign_up_page.alert_message_for_sign_up(), "Error! Shouldn't be able to connect")


if __name__ == '__main__':
    unittest.main()
