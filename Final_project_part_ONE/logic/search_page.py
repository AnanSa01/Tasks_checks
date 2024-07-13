import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *

from logic.base_app_page import BaseAppPage


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

    # CURRENT_RATING = '//div[@class="BookRatingStars"]//span[@aria-label="Rating 5 out of 5"]'
    # ADD_TAGS_INPUT = '//div[@class="FormControl FormControl"]//input[@data-testid="input"]'
    # ADD_TAGS_BUTTON = '//button[@class="Button Button--primary Button--medium"]'

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._catch_results_in_page = self._driver.find_elements(By.XPATH, self.CATCH_RESULTS_IN_PAGE)
            self._author_name = self._driver.find_elements(By.XPATH, self.AUTHOR_NAME)
        except NoSuchElementException:
            print("Error in finding element in SearchPage")

    def first_result_in_search(self):
        self._catch_results_in_page[0].click()

    def rating_the_book(self, rating_input):
        self._rating_book = self._driver.find_elements(By.XPATH, self.RATING_BOOK)
        self._rating_book[rating_input - 1].click()

    def check_current_rating_of_the_book_open(self):
        self._current_rating = self._driver.find_elements(By.XPATH, self.CURRENT_RATING)
        attribute_value = self._current_rating[0].get_attribute("aria-label").split()
        return int(attribute_value[1])

    def change_rating_of_the_book(self):
        self._rating_book = self._driver.find_elements(By.XPATH, self.RATING_BOOK)
        current_rating = self.check_current_rating_of_the_book_open()
        if current_rating == 5:
            self._rating_book[3].click()
        else:
            self._rating_book[4].click()

    def open_more_option_to_book_lists(self):
        self._option_for_lists_button = self._driver.find_elements(By.XPATH, self.OPTION_FOR_LISTS_BUTTON)
        self._option_for_lists_button[0].click()

    def add_book_to_read_list(self):
        self._add_to_read_list_button = self._driver.find_element(By.XPATH, self.ADD_TO_READ_LIST_BUTTON)
        self._add_to_read_list_button.click()

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
