import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *

from infra.base_page import BasePage


class MyBooksPage(BasePage):
    ADD_SHELF_BUTTON = '//a[contains(text(),"Add shelf")]'
    ADD_SHELF_INPUT = '//input[@id="user_shelf_name"]'
    ADD_BUTTON_FINAL = '//input[@class="gr-form--compact__submitButton"]'
    AVG_RATING_BUTTON = '//th[@alt="avg_rating"]//a'
    MY_BOOKS_TITLES = '//td[@class="field title"]//a'
    WANT_TO_READ_BUTTON = '//a[contains(text(), "Want to Read")]'
    REMOVE_BUTTONS_FROM_MY_BOOKS = '//img[@alt="Remove from my books"]'

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._add_shelf_button = self._driver.find_element(By.XPATH, self.ADD_SHELF_BUTTON)
            self._avg_rating_button = self._driver.find_element(By.XPATH, self.AVG_RATING_BUTTON)
            self._my_books_titles = self._driver.find_elements(By.XPATH, self.MY_BOOKS_TITLES)
            self._want_to_read_button = self._driver.find_element(By.XPATH, self.WANT_TO_READ_BUTTON)
        except NoSuchElementException:
            print("Error in finding element in MyBooksPage")

    def add_new_shelf_functionality(self, user_input):
        self._add_shelf_input = self._driver.find_element(By.XPATH, self.ADD_SHELF_INPUT)
        self._add_button_final = self._driver.find_element(By.XPATH, self.ADD_BUTTON_FINAL)

        self._add_shelf_button.click()
        time.sleep(3)
        self._add_shelf_input.click()
        self._add_shelf_input.send_keys(user_input)
        self._add_button_final.click()

    def change_order_in_my_books(self):
        self._avg_rating_button.click()

    def choose_one_of_my_books_by_title(self, title_input):
        for title in self._my_books_titles:
            print(title.text.lower())
            if title_input.lower() in title.text.lower():
                print(title_input)
                title.click()
        print("this means we didnt find anything")

    def click_on_want_to_read_list(self):
        self._want_to_read_button.click()

    # def click_on_remove_button_in_my_books_chosen(self, remove_input):
    #     self._remove_buttons_from_my_books = self._driver.find_elements(By.XPATH, self.REMOVE_BUTTONS_FROM_MY_BOOKS)
    #     self._remove_buttons_from_my_books[remove_input - 1].click()

    # def click_window(self):
    #     AAA ='//a[@class="actionLinkLite smallText deleteLink"]'
    #     self._remove_window = self._driver.find_element(By.XPATH, AAA)
    #     self._remove_window.click()

