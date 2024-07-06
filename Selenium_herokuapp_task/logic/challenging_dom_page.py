from selenium.webdriver.common.by import By

from infra.base_page import BasePage


class ChallengingDOMPage(BasePage):
    ROWS_IN_TABLE = '//tr'
    EDIT_ROW_IN_TABLE_BUTTON = '//a [contains(text(),"edit")]'
    DELETE_ROW_IN_TABLE_BUTTON = '//a [contains(text(),"delete")]'

    def __init__(self, driver):
        super().__init__(driver)
        self._edit_row_in_table_button = self._driver.find_elements(By.XPATH, self.EDIT_ROW_IN_TABLE_BUTTON)
        self._delete_row_in_table_button = self._driver.find_elements(By.XPATH, self.DELETE_ROW_IN_TABLE_BUTTON)

    def click_on_edit_button(self, index):
        print(f"Editing row number {index + 1}")
        self._edit_row_in_table_button[index].click()

    def click_on_delete_button(self, index):
        print(f"Deleting row number {index + 1}")
        self._delete_row_in_table_button[index].click()