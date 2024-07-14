import logging
import time

from infra.logging_basicConfig import LoggingSetup
from infra.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *


class MyBooksPage(BasePage):
    ADD_SHELF_BUTTON = '//a[contains(text(),"Add shelf")]'
    ADD_SHELF_INPUT = '//input[@id="user_shelf_name"]'
    ADD_BUTTON_FINAL = '//input[@class="gr-form--compact__submitButton"]'
    AVG_RATING_BUTTON = '//th[@alt="avg_rating"]//a'
    MY_BOOKS_TITLES = '//td[@class="field title"]//a'
    WANT_TO_READ_BUTTON = '//a[contains(text(), "Want to Read")]'
    REMOVE_BUTTONS_FROM_MY_BOOKS = '//img[@alt="Remove from my books"]'
    EDIT_BOOK_SHELVES_BUTTON = '//div[@id="shelvesSection"]//div[@class="sectionHeader"]//a'
    LIST_OF_SHELVES = '//table[@id="shelfTable"]//tr[@class="elementList"]//div//a[@class="displayShelfNameLnk"]'
    LIST_OF_BOOKS_IN_WANT_TO_READ = '//td[@class="field title"]'

    def __init__(self, driver):
        super().__init__(driver)
        logging.info("Attempting to find elements in MyBooksPage")
        try:
            self._add_shelf_button = self._driver.find_element(By.XPATH, self.ADD_SHELF_BUTTON)
            self._avg_rating_button = self._driver.find_element(By.XPATH, self.AVG_RATING_BUTTON)
            self._my_books_titles = self._driver.find_elements(By.XPATH, self.MY_BOOKS_TITLES)
            self._want_to_read_button = self._driver.find_element(By.XPATH, self.WANT_TO_READ_BUTTON)
            self._edit_book_shelves_button = self._driver.find_element(By.XPATH, self.EDIT_BOOK_SHELVES_BUTTON)
        except NoSuchElementException:
            logging.error("Error in finding element in MyBooksPage")

    # this function is ensure that the user can change the order of how his books is displayed.
    def change_order_in_my_books(self):
        self._avg_rating_button.click()

    # this function is to return the first book displayed in the list - to check change order test.
    def return_first_book_of_the_list(self):
        logging.info("Attempting to find elements for returning first book of the list function")
        try:
            self._my_books_titles_dynamic = self._driver.find_elements(By.XPATH, self.MY_BOOKS_TITLES)
        except NoSuchElementException:
            logging.error("Error in finding element for returning first book of the list function")
        return self._my_books_titles_dynamic[0].text

    # this function checks if the book wanted from the user is actually in the list of books.
    def choose_one_of_my_books_by_title(self, title_input):
        for title in self._my_books_titles:
            if title_input.lower() in title.text.lower():
                return title.text
        logging.error("Error! book not found in my books")


