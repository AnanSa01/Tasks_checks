from selenium.webdriver.common.by import By

from infra.base_page import BasePage
from logic.base_app_page import BaseAppPage


class HomePage(BaseAppPage):
    # MY_BOOKS_BUTTON = '//li[@class="siteHeader__topLevelItem"]//a[contains(text(),"My Books")]'
    # SEARCH_BAR = '//input[@class="searchBox__input searchBox__input--navbar"]'
    # SEARCH_BAR_BUTTON = '//BUTTON[@class="searchBox__icon--magnifyingGlass gr-iconButton searchBox__icon searchBox__icon--navbar"]'

    def __init__(self, driver):
        super().__init__(driver)
        # self._my_books_button = self._driver.find_element(By.XPATH, self.MY_BOOKS_BUTTON)
        # self._search_bar = self._driver.find_element(By.XPATH, self.SEARCH_BAR)
        # self._search_bar_button = self._driver.find_element(By.XPATH, self.SEARCH_BAR_BUTTON)




