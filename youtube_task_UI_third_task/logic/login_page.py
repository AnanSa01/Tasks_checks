from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from youtube_task_UI_third_task.infra.base_page import BasePage


class LoginPage(BasePage):
    SIGN_IN_INPUT = '//input[@id="identifierId"]'
    FIRST_PAGE_NEXT_BUTTON = '//span[contains(text(),"Next")]'
    LOGIN_PAGE_LOGO = '//h1//span'

    def __init__(self, driver):
        super().__init__(driver)
        self._sign_in_input = self._driver.find_element(By.XPATH, self.SIGN_IN_INPUT)
        self._first_page_next_button = self._driver.find_element(By.XPATH, self.FIRST_PAGE_NEXT_BUTTON)
        self._login_page_logo = self._driver.find_element(By.XPATH, self.LOGIN_PAGE_LOGO)

    def click_on_sign_in_field(self):
        self._sign_in_input.click()

    def write_input_in_sign_in_field(self, user_input):
        self._sign_in_input.send_keys(user_input)

    def click_on_next_button_on_first_page(self):
        self._first_page_next_button.click()

    def return_login_logo(self):
        WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.LOGIN_PAGE_LOGO)))
        return self._login_page_logo.text

