import logging

from infra.logging_basicConfig import LoggingSetup
from infra.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *


class BaseAppPage(BasePage):
    MY_BOOKS_BUTTON = '//li[@class="siteHeader__topLevelItem"]//a[contains(text(),"My Books")]'
    FRIENDS_BUTTON = '//div[@class="siteHeader__personal"]//a[@title="Friends"]'
    SEARCH_BAR = '//input[@class="searchBox__input searchBox__input--navbar"]'
    SEARCH_BAR_BUTTON = ('//BUTTON[@class="searchBox__icon--magnifyingGlass gr-iconButton searchBox__icon '
                         'searchBox__icon--navbar"]')

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._my_books_button = self._driver.find_element(By.XPATH, self.MY_BOOKS_BUTTON)
            self._search_bar = self._driver.find_element(By.XPATH, self.SEARCH_BAR)
            self._search_bar_button = self._driver.find_element(By.XPATH, self.SEARCH_BAR_BUTTON)
            self._friend_button = self._driver.find_element(By.XPATH, self.FRIENDS_BUTTON)
        except NoSuchElementException:
            logging.error("Error in finding element in BaseAppPage")

    def click_on_my_books_button(self):
        """
        this function is to click on my books button in the header
        """
        self._my_books_button.click()

    def search_for_a_book(self, user_input):
        """
        this function is to search for a book in the search bar
        :param user_input: input of the book to be searched.
        """
        self._search_bar.send_keys(user_input)
        self._search_bar_button.click()

    def click_on_friends_button(self):
        """
        this function is to click on friends button in the header
        """
        self._friend_button.click()
