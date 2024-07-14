import logging

from infra.logging_basicConfig import LoggingSetup
from infra.base_page import BasePage
from logic.base_app_page import BaseAppPage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *


class HomePage(BaseAppPage):
    HEADER_IS_DISPLAYED = '//div[@class="siteHeader__contents"]'

    def __init__(self, driver):
        super().__init__(driver)
        logging.info("Attempting to find elements in HomePage")
        try:
            self._header_is_displayed = self._driver.find_element(By.XPATH, self.HEADER_IS_DISPLAYED)
        except NoSuchElementException:
            logging.error("Error in finding element in HomePage")

    # this function to ensure that the header is displayed for login test.
    def check_if_header_displayed(self):
        return self._header_is_displayed.is_displayed()
