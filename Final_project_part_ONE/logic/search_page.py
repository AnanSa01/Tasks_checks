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

    # ADD_TAGS_INPUT = '//div[@class="FormControl FormControl"]//input[@data-testid="input"]'
    # ADD_TAGS_BUTTON = '//button[@class="Button Button--primary Button--medium"]'

    def __init__(self, driver):
        super().__init__(driver)
        logging.info("Attempting to find elements in SearchPage")
        try:
            self._catch_results_in_page = self._driver.find_elements(By.XPATH, self.CATCH_RESULTS_IN_PAGE)
            self._author_name = self._driver.find_elements(By.XPATH, self.AUTHOR_NAME)
        except NoSuchElementException:
            logging.error("Error in finding element in SearchPage")

        # this function clicks on the first result in the search - which is the most relevant search.
    def first_result_in_search(self):
        self._catch_results_in_page[0].click()

        # this function does a flow of rating a book from the user input.
    def rating_the_book(self, rating_input):
        logging.info("Attempting to find elements for rating book function")
        try:
            self._rating_book = self._driver.find_elements(By.XPATH, self.RATING_BOOK)
        except NoSuchElementException:
            logging.error("Error in finding element for rating book function")
        self._rating_book[rating_input - 1].click()

        # this function returns the current rating of book input in integer.
    def check_current_rating_of_the_book_open(self):
        logging.info("Attempting to find elements for checking current rating of book function")
        try:
            self._current_rating = self._driver.find_elements(By.XPATH, self.CURRENT_RATING)
        except NoSuchElementException:
            logging.error("Error in finding element for checking current rating book function")
        attribute_value = self._current_rating[0].get_attribute("aria-label").split()
        return int(attribute_value[1])

        # this function is to check the user current rating and changing it based on the previous rating.
    def change_rating_of_the_book(self):
        logging.info("Attempting to find elements for changing rating of book function")
        try:
            self._rating_book = self._driver.find_elements(By.XPATH, self.RATING_BOOK)
        except NoSuchElementException:
            logging.error("Error in finding element for changing rating book function")
        current_rating = self.check_current_rating_of_the_book_open()
        if current_rating == 5:
            self._rating_book[3].click()
        else:
            self._rating_book[4].click()

        # this function is to open more options to which list to add the book.
    def open_more_option_to_book_lists(self):
        logging.info("Attempting to find elements for more options to book function")
        try:
            self._option_for_lists_button = self._driver.find_elements(By.XPATH, self.OPTION_FOR_LISTS_BUTTON)
        except NoSuchElementException:
            logging.error("Error in finding element for more options to book function")
        self._option_for_lists_button[0].click()

        # this function is to add a book to read list after opening more options from the previous function.
    def add_book_to_read_list(self):
        logging.info("Attempting to find elements for adding book to reading list function")
        try:
            self._add_to_read_list_button = self._driver.find_element(By.XPATH, self.ADD_TO_READ_LIST_BUTTON)
        except NoSuchElementException:
            logging.error("Error in finding element for adding book to reading list function")
        self._add_to_read_list_button.click()

        # this function is to take the author name of the result and to return the first one - also most relevant.
    def search_for_author_name(self):
        return self._author_name[0].text

    def add_multiple_books_at_once(self, how_many):
        for i in range(how_many):
            self._add_to_read_list_from_search_results = self._driver.find_element(By.XPATH,
                                                         self.ADD_TO_READ_LIST_FROM_SEARCH_RESULTS)
            self._add_to_read_list_from_search_results.click()
            time.sleep(1)

    def click_done_button_after_adding_to_list(self):
        self._done_button_after_adding_to_list = self._driver.find_element(By.XPATH, self.DONE_BUTTON_IN_ADDING_TO_LIST)
        # self._add_tags_input = self._driver.find_element(By.XPATH, self.ADD_TAGS_INPUT)
        # self._add_tags_button = self._driver.find_element(By.XPATH, self.ADD_TAGS_BUTTON)
        #
        # self._add_tags_input.click()
        # self._add_tags_input.send_keys(tags_input)
        # self._add_tags_button.click()
        self._done_button_after_adding_to_list.click()
