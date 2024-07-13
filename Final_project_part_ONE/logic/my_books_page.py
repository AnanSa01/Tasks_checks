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
            print("Error in finding element in MyBooksPage")

    def change_order_in_my_books(self):
        self._avg_rating_button.click()

    def return_first_book_of_the_list(self):
        self._my_books_titles_dynamic = self._driver.find_elements(By.XPATH, self.MY_BOOKS_TITLES)
        return self._my_books_titles_dynamic[0].text

    def choose_one_of_my_books_by_title(self, title_input):
        for title in self._my_books_titles:
            if title_input.lower() in title.text.lower():
                return title.text
        print("Error! book not found in my books")

    def click_on_want_to_read_list(self):
        self._want_to_read_button.click()

    def return_how_many_books_in_my_to_read_list(self):
        self.list_of_books_in_want_to_read = self._driver.find_elements(By.XPATH, self.LIST_OF_BOOKS_IN_WANT_TO_READ)
        return len(self.list_of_books_in_want_to_read)

    def add_new_shelf_functionality(self, user_input):
        self._add_shelf_input = self._driver.find_element(By.XPATH, self.ADD_SHELF_INPUT)
        self._add_button_final = self._driver.find_element(By.XPATH, self.ADD_BUTTON_FINAL)
        self._add_shelf_button.click()
        time.sleep(3)
        self._add_shelf_input.click()
        self._add_shelf_input.send_keys(user_input)
        self._add_button_final.click()





    # def click_on_edit_book_shelves_button(self):
    #     self._edit_book_shelves_button.click()

    # def catch_all_lists_in_shelves(self):
    #     self._list_of_shelves = self._driver.find_elements(By.XPATH, self.LIST_OF_SHELVES)
    #     return self._list_of_shelves[3].text

    # def click_on_remove_button_in_my_books_chosen(self, remove_input):
    #     self._remove_buttons_from_my_books = self._driver.find_elements(By.XPATH, self.REMOVE_BUTTONS_FROM_MY_BOOKS)
    #     self._remove_buttons_from_my_books[remove_input - 1].click()

    # def click_window(self):
    #     AAA ='//a[@class="actionLinkLite smallText deleteLink"]'
    #     self._remove_window = self._driver.find_element(By.XPATH, AAA)
    #     self._remove_window.click()

