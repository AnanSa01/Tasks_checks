import time

from infra.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    EMAIL_INPUT = '//input[@id="ap_email"]'
    PASSWORD_INPUT = '//input[@id="ap_password"]'
    SIGN_IN_BUTTON = '//input[@id="signInSubmit"]'

    SIGN_UP_BUTTON = '//a[@id="createAccountSubmit"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._email_input_field = self._driver.find_element(By.XPATH, self.EMAIL_INPUT)
        self._password_input_field = self._driver.find_element(By.XPATH, self.PASSWORD_INPUT)
        self._sign_in_button = self._driver.find_element(By.XPATH, self.SIGN_IN_BUTTON)

        self._sign_up_button = self._driver.find_element(By.XPATH, self.SIGN_UP_BUTTON)


    def write_in_email_input_field(self, user_email_input):
        self._email_input_field.click()
        self._email_input_field.send_keys(user_email_input)

    def write_in_password_input_field(self, user_password_input):
        self._password_input_field.click()
        self._password_input_field.send_keys(user_password_input)

    def click_on_sign_in_button(self):
        self._sign_in_button.click()

    def click_on_sign_up_button_in_login_window(self):
        self._sign_up_button.click()

    def valid_login_flow(self):
        self.write_in_email_input_field("aaafortesting@gmail.com")
        self.write_in_password_input_field("aaafortesting123456789")
        self.click_on_sign_in_button()

