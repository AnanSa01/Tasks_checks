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

    def tearDown(self):
        self.driver.quit()

    def test_rating_a_book(self):
        print("Test rating a book -")
        name_of_the_book = "Return of the King"
        rating_of_the_book = 5
        self.home_page.search_for_a_book(name_of_the_book)
        search_page = SearchPage(self.driver)
        search_page.first_result_in_search()
        search_page.rating_the_book(rating_of_the_book)
        self.assertEqual(search_page.check_current_rating_of_the_book_open(), rating_of_the_book)
        time.sleep(5)
        search_page.rating_the_book(rating_of_the_book)


if __name__ == '__main__':
    unittest.main()
