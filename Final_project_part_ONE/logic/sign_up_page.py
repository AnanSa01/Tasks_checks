from selenium.webdriver.common.by import By

from infra.base_page import BasePage


class SignUpPage(BasePage):
    YOUR_NAME_INPUT = '//input[@id="ap_customer_name"]'
    EMAIL_INPUT = '//input[@id="ap_email"]'
    PASSWORD_INPUT = '//input[@id="ap_password"]'
    RE_ENTER_PASSWORD_INPUT = '//input[@id="ap_password_check"]'
    CREATE_ACCOUNT_BUTTON = '//input[@id="continue"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._your_name_input = self._driver.find_element(By.XPATH, self.YOUR_NAME_INPUT)
        self._email_input = self._driver.find_element(By.XPATH, self.EMAIL_INPUT)
        self._password_input = self._driver.find_element(By.XPATH, self.PASSWORD_INPUT)
        self._re_enter_password_input = self._driver.find_element(By.XPATH, self.RE_ENTER_PASSWORD_INPUT)
        self._create_account_button = self._driver.find_element(By.XPATH, self.CREATE_ACCOUNT_BUTTON)

    def write_in_your_name_field(self, user_input):
        self._your_name_input.click()
        self._your_name_input.send_keys(user_input)

    def write_in_email_input(self, email_input):
        self._email_input.click()
        self._email_input.send_keys(email_input)

    def write_in_password_and_re_enter_password(self, password_input):
        self._password_input.click()
        self._password_input.send_keys(password_input)
        self._re_enter_password_input.click()
        self._re_enter_password_input.send_keys(password_input)

    def click_on_create_account_button(self):
        self._create_account_button.click()