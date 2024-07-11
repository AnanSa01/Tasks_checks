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

    def test_changing_order_in_my_books(self): # this may should br in the shelevs function
        self.home_page.click_on_my_books_button()
        my_books_page = MyBooksPage(self.driver)
        my_books_page.change_order_in_my_books()
        time.sleep(5)

    def test_add_a_friend(self): # this may need to be in other test group
        self.home_page.click_on_friends_button()
        time.sleep(3)
        friends_page = FriendsPage(self.driver)
        friends_page.search_for_a_person_flow("tzahi")
        time.sleep(3)
        friends_page.add_as_a_friend_first_person()
        time.sleep(5)

    def test_edit_book_in_my_books(self):
        self.home_page.click_on_my_books_button()
        my_books_page = MyBooksPage(self.driver)
        my_books_page.choose_one_of_my_books_by_title("Return of the King")
        #  ...... to be continued




if __name__ == '__main__':
    unittest.main()
