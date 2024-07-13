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

    def test_add_multiple_books_at_once(self):
        print("Test adding multiple books at once -")
        self.home_page.search_for_a_book("Harry Potter")
        search_page = SearchPage(self.driver)
        how_many_books_to_add = 5
        search_page.add_multiple_books_at_once(how_many_books_to_add)
        search_page.click_on_my_books_button()
        my_books_page = MyBooksPage(self.driver)
        my_books_page.click_on_want_to_read_list()
        self.assertEqual(my_books_page.return_how_many_books_in_my_to_read_list(), how_many_books_to_add, "Error!")


if __name__ == '__main__':
    unittest.main()


    #def test_add_a_new_shelf(self):
    #     self.home_page.click_on_my_books_button()
    #     my_books_page = MyBooksPage(self.driver)
    #     name_of_the_list = "This list for test"
    #     my_books_page.add_new_shelf_functionality(name_of_the_list)
    #     time.sleep(5)
    #     my_books_page.click_on_edit_book_shelves_button()
    #     time.sleep(5)
    #     my_books_page.click_on_edit_book_shelves_button()
    #     time.sleep(5)
    #     my_books_page.click_on_edit_book_shelves_button()
    #     # self.assertEqual(my_books_page.catch_all_lists_in_shelves(),name_of_the_list)
    #     # time.sleep(5)

    # def test_add_book_to_read_list(self):
    #     self.home_page.search_for_a_book("The Republic")
    #     search_page = SearchPage(self.driver)
    #     search_page.first_result_in_search()
    #     search_page.open_more_option_to_book_lists()
    #     search_page.add_book_to_read_list()
    #     search_page.click_done_button_after_adding_to_list()