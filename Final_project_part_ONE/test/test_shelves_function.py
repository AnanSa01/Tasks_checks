import time
import unittest

from infra.browser_wrapper import BrowserWrapper
from logic.home_page import HomePage
from logic.individual_book_page import IndividualBookPage
from logic.login_page import LoginPage
from logic.my_books_page import MyBooksPage
from logic.search_page import SearchPage


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver(self.browser.config["base_url"])
        self.login_page = LoginPage(self.driver)
        self.login_page.valid_login_flow()
        self.home_page = HomePage(self.driver)

    def test_add_a_new_shelf(self):
        self.home_page.click_on_my_books_button()
        my_books_page = MyBooksPage(self.driver)
        my_books_page.add_new_shelf_functionality("This list for test")
        time.sleep(5)

    def test_rating_a_book(self):
        self.home_page.search_for_a_book("Return of the King")
        search_page = SearchPage(self.driver)
        search_page.first_result_in_search()
        search_page.rating_the_book(5)  # change rating here
        time.sleep(3)

    def test_changing_rating_of_a_book(self):
        self.home_page.search_for_a_book("The Alchemist")
        search_page = SearchPage(self.driver)
        search_page.first_result_in_search()
        search_page.change_rating_of_the_book()
        time.sleep(3)

    def test_add_book_to_read_list(self):
        self.home_page.search_for_a_book("The Republic")
        search_page = SearchPage(self.driver)
        search_page.first_result_in_search()
        search_page.open_more_option_to_book_lists()
        search_page.add_book_to_read_list()
        search_page.click_done_button_after_adding_to_list()

    def test_something(self):
        time.sleep(3)
        self.home_page.refresh_page()
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()
