from selenium.webdriver.common.by import By

from infra.base_page import BasePage


class CheckboxesPage(BasePage):
    CHECKBOX_FIRST = '//form[@id="checkboxes"]//input[1]'
    CHECKBOX_SECOND = '//form[@id="checkboxes"]//input[2]'

    def __init__(self, driver):
        super().__init__(driver)
        self._checkbox_first = self._driver.find_element(By.XPATH, self.CHECKBOX_FIRST)
        self._checkbox_second = self._driver.find_element(By.XPATH, self.CHECKBOX_SECOND)

    def click_on_first_checkbox(self):
        self._checkbox_first.click()
        print("Clicked on first box")

    def click_on_second_checkbox(self):
        self._checkbox_second.click()
        print("Clicked on second box")

    def check_if_first_checkbox_selected(self):
        if self._checkbox_first.is_selected():
            print("The first checkbox IS SELECTED!")
        else:
            print("The first checkbox is NOT selected!")

    def check_if_second_checkbox_selected(self):
        if self._checkbox_second.is_selected():
            print("The second checkbox IS SELECTED!")
        else:
            print("The second checkbox is NOT selected!")

    def clear_checkbox(self):
        self._checkbox_second.clear()
        print("box is cleared")