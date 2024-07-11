import time

from selenium.webdriver.common.by import By

from logic.base_app_page import BaseAppPage


class SearchPage(BaseAppPage):
    CATCH_RESULTS_IN_PAGE = '//a[@class="bookTitle"]'
    RATING_BOOK = '//div[@class="Sticky"]//button[@class="baseClass RatingStar--medium RatingStar--selectable"]'
    AUTHOR_NAME = '//a[@class="authorName"]//span'

    EXPECTED_RESULT = '//div[@class="BookActions"]//span[@aria-label="Rating 5 out of 5"]'

    OPTION_FOR_LISTS_BUTTON = '//button[@aria-label="Tap to choose a shelf for this book"]'
    ADD_TO_READ_LIST_BUTTON = '//button[@aria-label="Read"]'

    DONE_BUTTON_IN_ADDING_TO_LIST = '//button//span[contains(text(), "Done")]'

    # ADD_TAGS_INPUT = '//div[@class="FormControl FormControl"]//input[@data-testid="input"]'
    # ADD_TAGS_BUTTON = '//button[@class="Button Button--primary Button--medium"]'


    def __init__(self, driver):
        super().__init__(driver)
        self._catch_results_in_page = self._driver.find_elements(By.XPATH, self.CATCH_RESULTS_IN_PAGE)
        self._author_name = self._driver.find_elements(By.XPATH, self.AUTHOR_NAME)

    def first_result_in_search(self):
        print(self._catch_results_in_page[0].text)
        self._catch_results_in_page[0].click()

    def rating_the_book(self, rating_input):
        self._rating_book = self._driver.find_elements(By.XPATH, self.RATING_BOOK)
        self._rating_book[rating_input - 1].click()

    def change_rating_of_the_book(self):
        self._expected_result = self._driver.find_elements(By.XPATH, self.EXPECTED_RESULT)

        self._rating_book = self._driver.find_elements(By.XPATH, self.RATING_BOOK)

        if self._expected_result:
            self._rating_book[3].click()
        else:
            self._rating_book[4].click()

    def open_more_option_to_book_lists(self):
        self._option_for_lists_button = self._driver.find_elements(By.XPATH, self.OPTION_FOR_LISTS_BUTTON)
        self._option_for_lists_button[0].click()

    def add_book_to_read_list(self):
        self._add_to_read_list_button = self._driver.find_element(By.XPATH, self.ADD_TO_READ_LIST_BUTTON)
        self._add_to_read_list_button.click()

    def click_done_button_after_adding_to_list(self):
        self._done_button_after_adding_to_list = self._driver.find_element(By.XPATH, self.DONE_BUTTON_IN_ADDING_TO_LIST)
        # self._add_tags_input = self._driver.find_element(By.XPATH, self.ADD_TAGS_INPUT)
        # self._add_tags_button = self._driver.find_element(By.XPATH, self.ADD_TAGS_BUTTON)
        #
        # self._add_tags_input.click()
        # self._add_tags_input.send_keys(tags_input)
        # self._add_tags_button.click()
        self._done_button_after_adding_to_list.click()

    def search_for_author_name(self):
        print(self._author_name[0].text)




