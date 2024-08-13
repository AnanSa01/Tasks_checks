from selenium.webdriver.common.by import By
from Selenium_herokuapp_task.infra.base_page import BasePage


class AddRemoveElementsPage(BasePage):
    ADD_ELEMENT_BUTTON = '//button[text() = "Add Element"]'
    DELETE_BUTTON = '//button[text() = "Delete"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._add_element_button = self._driver.find_element(By.XPATH, self.ADD_ELEMENT_BUTTON)


    def click_on_add_element_count(self, count):
        print(f"Clicking 'Add Element' button {count} times.")
        for i in range(count):
            self._add_element_button.click()

    def click_on_delete(self, index):
        print(f"Deleting button number {index}.")
        self._delete_button = self._driver.find_elements(By.XPATH, self.DELETE_BUTTON)
        self._delete_button[index].click()
