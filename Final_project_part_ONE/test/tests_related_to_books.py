import time
import unittest

from infra.browser_wrapper import BrowserWrapper
from logic.friends_page import FriendsPage
from logic.home_page import HomePage
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

    def test_search_a_book_by_author(self):
        self.home_page.search_for_a_book("Stephen King")
        search_page = SearchPage(self.driver)
        search_page.search_for_author_name()
        time.sleep(5)

    def test_find_book_in_my_books_list_and_open_it(self):
        self.home_page.click_on_my_books_button()
        my_books_page = MyBooksPage(self.driver)
        my_books_page.choose_one_of_my_books_by_title("Return of the King")

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








if __name__ == '__main__':
    unittest.main()
