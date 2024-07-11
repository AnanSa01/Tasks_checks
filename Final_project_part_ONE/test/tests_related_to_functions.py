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

    def test_add_a_new_shelf(self):
        self.home_page.click_on_my_books_button()
        my_books_page = MyBooksPage(self.driver)
        my_books_page.add_new_shelf_functionality("This list for test")
        time.sleep(5)

    def test_add_book_to_read_list(self):
        self.home_page.search_for_a_book("The Republic")
        search_page = SearchPage(self.driver)
        search_page.first_result_in_search()
        search_page.open_more_option_to_book_lists()
        search_page.add_book_to_read_list()
        search_page.click_done_button_after_adding_to_list()

    def test_changing_order_in_my_books(self):
        self.home_page.click_on_my_books_button()
        my_books_page = MyBooksPage(self.driver)
        my_books_page.change_order_in_my_books()
        time.sleep(5)

    def test_add_a_friend(self):
        self.home_page.click_on_friends_button()
        time.sleep(3)
        friends_page = FriendsPage(self.driver)
        friends_page.search_for_a_person_flow("tzahi")
        time.sleep(3)
        friends_page.add_as_a_friend_first_person()
        time.sleep(5)

    def test_add_multiple_books_at_once(self):
        self.home_page.search_for_a_book("Harry Potter")
        search_page = SearchPage(self.driver)
        time.sleep(3)
        search_page.add_multiple_books_at_once(3)
        time.sleep(3)
        search_page.click_on_my_books_button()
        time.sleep(3)
        my_books_page = MyBooksPage(self.driver)
        my_books_page.click_on_want_to_read_list()
        # my_books_page.click_on_remove_button_in_my_books_chosen(2)
        # my_books_page.click_window()


if __name__ == '__main__':
    unittest.main()
