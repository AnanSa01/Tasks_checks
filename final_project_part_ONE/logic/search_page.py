import logging
import time

from infra.logging_basicConfig import LoggingSetup
from logic.base_app_page import BaseAppPage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *


class SearchPage(BaseAppPage):
    CATCH_RESULTS_IN_PAGE = '//a[@class="bookTitle"]'
    RATING_BOOK = '//div[@class="Sticky"]//button[@class="baseClass RatingStar--medium RatingStar--selectable"]'
    AUTHOR_NAME = '//a[@class="authorName"]//span'
    ADD_TO_READ_LIST_FROM_SEARCH_RESULTS = '//button[@class="wtrToRead"]//span'
    EXPECTED_RESULT = '//div[@class="BookActions"]//span[@aria-label="Rating 5 out of 5"]'
    OPTION_FOR_LISTS_BUTTON = '//button[@aria-label="Tap to choose a shelf for this book"]'
    ADD_TO_READ_LIST_BUTTON = '//button[@aria-label="Read"]'
    DONE_BUTTON_IN_ADDING_TO_LIST = '//button//span[contains(text(), "Done")]'
    CURRENT_RATING = f'//div[@class="Sticky"]//div[@class="BookActions"]//div[@class="BookRatingStars"]//span'

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._catch_results_in_page = self._driver.find_elements(By.XPATH, self.CATCH_RESULTS_IN_PAGE)
            self._author_name = self._driver.find_elements(By.XPATH, self.AUTHOR_NAME)
        except NoSuchElementException:
            logging.error("Error in finding element in SearchPage")

    def first_result_in_search(self):
        """
        this function clicks on the first result in the search - which is the most relevant search.
        """
        self._catch_results_in_page[0].click()

    def rating_the_book(self, rating_input):
        """
        this function does a flow of rating a book from the user input.
        :param rating_input: rating number of the opened book profile.
        """
        try:
            self._rating_book = self._driver.find_elements(By.XPATH, self.RATING_BOOK)
        except NoSuchElementException:
            logging.error("Error in finding element for rating book function")
        self._rating_book[rating_input - 1].click()

    def clear_rating_of_the_book(self, rating_input):
        self.rating_the_book(rating_input)

    def check_current_rating_of_the_book_open(self):
        """
        this function returns the current rating of book input in integer.
        :return: rating of the book in integer number.
        """
        try:
            self._current_rating = self._driver.find_elements(By.XPATH, self.CURRENT_RATING)
        except NoSuchElementException:
            logging.error("Error in finding element for checking current rating book function")
        attribute_value = self._current_rating[0].get_attribute("aria-label").split()
        return int(attribute_value[1])

    def change_rating_of_the_book(self):
        """
        this function is to check the user current rating and changing it based on the previous rating.
        """
        try:
            self._rating_book = self._driver.find_elements(By.XPATH, self.RATING_BOOK)
        except NoSuchElementException:
            logging.error("Error in finding element for changing rating book function")
        current_rating = self.check_current_rating_of_the_book_open()
        if current_rating == 5:
            self._rating_book[3].click()
        else:
            self._rating_book[4].click()

    def search_for_author_name(self):
        """
        this function is to take the author name of the result and to return the first one - also most relevant.
        :return: the author of the first book displayed
        """
        return self._author_name[0].text
