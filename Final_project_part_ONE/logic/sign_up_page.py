import logging

from infra.base_page import BasePage
from infra.logging_basicConfig import LoggingSetup
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *


class SignUpPage(BasePage):
    YOUR_NAME_INPUT = '//input[@id="ap_customer_name"]'
    EMAIL_INPUT = '//input[@id="ap_email"]'
    PASSWORD_INPUT = '//input[@id="ap_password"]'
    RE_ENTER_PASSWORD_INPUT = '//input[@id="ap_password_check"]'
    CREATE_ACCOUNT_BUTTON = '//input[@id="continue"]'
    ALERT_MESSAGE_FOR_SIGN_UP = '//h4[@class="a-alert-heading"]'

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._your_name_input = self._driver.find_element(By.XPATH, self.YOUR_NAME_INPUT)
            self._email_input = self._driver.find_element(By.XPATH, self.EMAIL_INPUT)
            self._password_input = self._driver.find_element(By.XPATH, self.PASSWORD_INPUT)
            self._re_enter_password_input = self._driver.find_element(By.XPATH, self.RE_ENTER_PASSWORD_INPUT)
            self._create_account_button = self._driver.find_element(By.XPATH, self.CREATE_ACCOUNT_BUTTON)
        except NoSuchElementException:
            logging.error("Error in finding element in SignUpPage")

    def write_in_your_name_field(self, user_input):
        """
        this function is to write in "Your name" field in sign up.
        :param user_input: input for "Your name" field.
        """
        self._your_name_input.click()
        self._your_name_input.send_keys(user_input)

    def write_in_email_input(self, email_input):
        """
        this function is to write in "Your Email address" field in sign up.
        :param email_input: input for "Email" field.
        """
        self._email_input.click()
        self._email_input.send_keys(email_input)

    def write_in_password_and_re_enter_password_flow(self, password_input):
        """
        this function is to write in "Your password" and "Re-enter password" fields in sign up.
        :param password_input: input for "Password" and "Re-enter password" field.
        """
        self._password_input.click()
        self._password_input.send_keys(password_input)
        self._re_enter_password_input.click()
        self._re_enter_password_input.send_keys(password_input)

    def write_in_just_password_input(self, password):
        """
        this function is JUST to write in "Your password" field in sign up.
        :param password: input for "Password" field.
        """
        self._password_input.click()
        self._password_input.send_keys(password)

    def write_in_just_re_enter_password_input(self, re_enter_password):
        """
        this function is JUST to write in "Re-enter password" field in sign up.
        :param re_enter_password: input for "Re-enter password" field.
        """
        self._re_enter_password_input.click()
        self._re_enter_password_input.send_keys(re_enter_password)

    def click_on_create_account_button(self):
        """
        this function is to press on create account button in sign up page.
        """
        self._create_account_button.click()

    def alert_message_for_sign_up(self):
        """
        this function to check for alert message for invalid input in sign up and return it to the tests pages.
        :return: True/False if alert message is displayed.
        """
        try:
            self._alert_message_for_sign_up = self._driver.find_element(By.XPATH, self.ALERT_MESSAGE_FOR_SIGN_UP)
        except NoSuchElementException:
            logging.error("Error in finding element for sign up function")
        return self._alert_message_for_sign_up.is_displayed()
