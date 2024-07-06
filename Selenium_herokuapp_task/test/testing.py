import time
import unittest

from logic.context_menu_page import ContextMenuPage
from logic.checkboxes_page import CheckboxesPage
from logic.challenging_dom_page import ChallengingDOMPage
from logic.broken_images_page import BrokenImagesPage
from logic.add_remove_elements_page import AddRemoveElementsPage
from logic.home_page import HomePage

from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider





def starting_new_test():
    browser = BrowserWrapper()
    return browser.get_driver(browser.config["base_url"])


class Testing(unittest.TestCase):

    def test_add_remove_element(self):
        driver = starting_new_test()
        home_page = HomePage(driver)
        print("\nTesting Add/Remove Elements -")
        home_page.add_remove_elements_link()
        add_remove_elements = AddRemoveElementsPage(driver)
        add_remove_elements.click_on_add_element_count(5)  # Change number of buttons added
        add_remove_elements.click_on_delete(3)  # Change index of deleted button

    def test_broken_images(self):
        driver = starting_new_test()
        home_page = HomePage(driver)
        print("\nTesting Broken Images -")
        home_page.broken_images_link()
        check_broken_images = BrokenImagesPage(driver)
        check_broken_images.check_if_image_is_broken()

    def test_challenging_dom(self):
        driver = starting_new_test()
        home_page = HomePage(driver)
        print("\nTesting Challenging DOM -")
        home_page.challenging_dom_link()
        challenging_dom = ChallengingDOMPage(driver)
        challenging_dom.click_on_edit_button(3)  # Change number of edited row
        challenging_dom.click_on_delete_button(5)  # Change number of deleted row

    def test_checkboxes(self):
        driver = starting_new_test()
        home_page = HomePage(driver)
        print("\nTesting Checkboxes -")
        home_page.checkboxes_link()
        checkboxes = CheckboxesPage(driver)
        checkboxes.check_if_first_checkbox_selected()
        checkboxes.check_if_second_checkbox_selected()
        checkboxes.click_on_first_checkbox()
        checkboxes.click_on_first_checkbox()
        checkboxes.click_on_second_checkbox()
        checkboxes.check_if_first_checkbox_selected()
        checkboxes.check_if_second_checkbox_selected()

    def test_context_menu(self):
        driver = starting_new_test()
        home_page = HomePage(driver)
        print("\nTesting Context Menu -")
        home_page.context_menu_link()
        context_menu = ContextMenuPage(driver)
        context_menu.right_click_on_box()





