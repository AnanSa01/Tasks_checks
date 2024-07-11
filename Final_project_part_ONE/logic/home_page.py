from selenium.webdriver.common.by import By

from infra.base_page import BasePage
from logic.base_app_page import BaseAppPage


class HomePage(BaseAppPage):
    HEADER_IS_DISPLAYED = '//div[@class="siteHeader__contents"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._header_is_displayed = self._driver.find_element(By.XPATH, self.HEADER_IS_DISPLAYED)

    def check_if_header_displayed(self):
        return self._header_is_displayed.is_displayed()





