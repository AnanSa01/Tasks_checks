import time
import unittest

from herokuapp_task_UI_second_task.logic.context_menu_page import ContextMenuPage
from herokuapp_task_UI_second_task.logic.checkboxes_page import CheckboxesPage
from herokuapp_task_UI_second_task.logic.challenging_dom_page import ChallengingDOMPage
from herokuapp_task_UI_second_task.logic.broken_images_page import BrokenImagesPage
from herokuapp_task_UI_second_task.logic.add_remove_elements_page import AddRemoveElementsPage
from herokuapp_task_UI_second_task.logic.home_page import HomePage

from herokuapp_task_UI_second_task.infra.browser_wrapper import BrowserWrapper
from herokuapp_task_UI_second_task.infra.config_provider import ConfigProvider


class Testing(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver(self.browser.config["base_url"])

    def test_add_remove_element(self):
        home_page = HomePage(self.driver)
        print("\nTesting Add/Remove Elements -")
        home_page.add_remove_elements_link()
        add_remove_elements = AddRemoveElementsPage(self.driver)
        add_remove_elements.click_on_add_element_count(5)  # Change number of buttons added
        add_remove_elements.click_on_delete(3)  # Change index of deleted button

    def test_broken_images(self):
        home_page = HomePage(self.driver)
        print("\nTesting Broken Images -")
        home_page.broken_images_link()
        check_broken_images = BrokenImagesPage(self.driver)
        check_broken_images.check_if_image_is_broken()

    def test_challenging_dom(self):
        home_page = HomePage(self.driver)
        print("\nTesting Challenging DOM -")
        home_page.challenging_dom_link()
        challenging_dom = ChallengingDOMPage(self.driver)
        challenging_dom.click_on_edit_button(3)  # Change number of edited row
        challenging_dom.click_on_delete_button(5)  # Change number of deleted row

    def test_checkboxes(self):
        home_page = HomePage(self.driver)
        print("\nTesting Checkboxes -")
        home_page.checkboxes_link()
        checkboxes = CheckboxesPage(self.driver)
        checkboxes.check_if_first_checkbox_selected()
        checkboxes.check_if_second_checkbox_selected()
        checkboxes.click_on_first_checkbox()
        checkboxes.click_on_first_checkbox()
        checkboxes.click_on_second_checkbox()
        checkboxes.check_if_first_checkbox_selected()
        checkboxes.check_if_second_checkbox_selected()

    def test_context_menu(self):
        home_page = HomePage(self.driver)
        print("\nTesting Context Menu -")
        home_page.context_menu_link()
        context_menu = ContextMenuPage(self.driver)
        context_menu.right_click_on_box()


if __name__ == '__main__':
    unittest.main()
