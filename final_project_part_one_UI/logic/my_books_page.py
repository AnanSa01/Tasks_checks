import logging
import time

from final_project_part_one_UI.infra.logging_basicConfig import LoggingSetup
from final_project_part_one_UI.infra.base_page import BasePage
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
        try:
            self._add_shelf_button = self._driver.find_element(By.XPATH, self.ADD_SHELF_BUTTON)
            self._avg_rating_button = self._driver.find_element(By.XPATH, self.AVG_RATING_BUTTON)
            self._my_books_titles = self._driver.find_elements(By.XPATH, self.MY_BOOKS_TITLES)
            self._want_to_read_button = self._driver.find_element(By.XPATH, self.WANT_TO_READ_BUTTON)
            self._edit_book_shelves_button = self._driver.find_element(By.XPATH, self.EDIT_BOOK_SHELVES_BUTTON)
        except NoSuchElementException:
            logging.error("Error in finding element in MyBooksPage")

    def change_order_in_my_books(self):
        """
        this function is ensure that the user can change the order of how his books is displayed.
        """
        self._avg_rating_button.click()

    def return_first_book_of_the_list(self):
        """
        this function is to return the first book displayed in the list - to check change order test.
        :return: the first book displayed
        """
        try:
            self._my_books_titles_dynamic = self._driver.find_elements(By.XPATH, self.MY_BOOKS_TITLES)
        except NoSuchElementException:
            logging.error("Error in finding element for returning first book of the list function")
        return self._my_books_titles_dynamic[0].text

    def choose_one_of_my_books_by_title(self, title_input):
        """
        this function checks if the book wanted from the user is actually in the list of books.
        :param title_input: to check if this title exist in the list
        :return: the book title how it was found in the list
        """
        for title in self._my_books_titles:
            if title_input.lower() in title.text.lower():
                return title.text
        logging.error("Error! book not found in my books")


