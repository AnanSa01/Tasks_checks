import time
import unittest

from infra.browser_wrapper import BrowserWrapper
from logic.login_page import LoginPage
from logic.sign_up_page import SignUpPage


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver(self.browser.config["base_url"])

    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        time.sleep(1)
        login_page.write_in_email_input_field("aaafortesting@gmail.com")
        time.sleep(1)
        login_page.write_in_password_input_field("aaafortesting123456789")
        time.sleep(1)
        login_page.click_on_sign_in_button()
        time.sleep(5)

    def test_sign_up_with_already_connected_user(self):
        login_page = LoginPage(self.driver)
        login_page.click_on_sign_up_button_in_login_window()
        time.sleep(5)
        sign_up_page = SignUpPage(self.driver)
        sign_up_page.write_in_your_name_field("A S")
        sign_up_page.write_in_email_input("aaafortesting@gmail.com")
        sign_up_page.write_in_password_and_re_enter_password("aaafortesting123456789")
        sign_up_page.click_on_create_account_button()
        time.sleep(5)

    def test_invalid_email_sign_up(self):
        login_page = LoginPage(self.driver)
        login_page.click_on_sign_up_button_in_login_window()
        time.sleep(5)
        sign_up_page = SignUpPage(self.driver)
        sign_up_page.write_in_your_name_field("A S")
        sign_up_page.write_in_email_input("@@@@@@@@@@@@@@@")
        sign_up_page.write_in_password_and_re_enter_password("0000000000")
        sign_up_page.click_on_create_account_button()
        time.sleep(5)

    def test_invalid_login_with_wrong_password(self):
        login_page = LoginPage(self.driver)
        time.sleep(1)
        login_page.write_in_email_input_field("aaafortesting@gmail.com")
        time.sleep(1)
        login_page.write_in_password_input_field("@@@@@@@@@@@@@@@@@@@@@@@@@")
        time.sleep(1)
        login_page.click_on_sign_in_button()
        time.sleep(5)







if __name__ == '__main__':
    unittest.main()
