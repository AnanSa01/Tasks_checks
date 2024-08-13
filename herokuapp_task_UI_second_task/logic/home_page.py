from herokuapp_task_UI_second_task.infra.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from herokuapp_task_UI_second_task.infra.browser_wrapper import BrowserWrapper


class HomePage(BasePage):
    ADD_REMOVE_ELEMENTS_LINK = '//a[contains(text(),"Add/Remove Elements")]'
    BROKEN_IMAGES_LINK = '//a[contains(text(),"Broken Images")]'
    CHALLENGING_DOM_LINK = '//a[contains(text(),"Challenging DOM")]'
    CHECKBOXES_LINK = '//a[contains(text(),"Checkboxes")]'
    CONTEXT_MENU_LINK = '//a[contains(text(),"Context Menu")]'

    def __init__(self, driver):
        super().__init__(driver)
        self._add_remove_elements_link = self._driver.find_element(By.XPATH, self.ADD_REMOVE_ELEMENTS_LINK)
        self._broken_images_link = self._driver.find_element(By.XPATH, self.BROKEN_IMAGES_LINK)
        self._challenging_dom_link = self._driver.find_element(By.XPATH, self.CHALLENGING_DOM_LINK)
        self._checkboxes_link = self._driver.find_element(By.XPATH, self.CHECKBOXES_LINK)
        self._context_menu_link = self._driver.find_element(By.XPATH, self.CONTEXT_MENU_LINK)

    def add_remove_elements_link(self):
        self._add_remove_elements_link.click()

    def broken_images_link(self):
        self._broken_images_link.click()

    def challenging_dom_link(self):
        self._challenging_dom_link.click()

    def checkboxes_link(self):
        self._checkboxes_link.click()

    def context_menu_link(self):
        self._context_menu_link.click()


