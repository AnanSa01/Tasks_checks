import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from youtube_task_UI_third_task.logic.base_app_page import BaseAppPage


class HistoryPage(BaseAppPage):
    CLEAR_HISTORY_BUTTON = '//button[@aria-label="Clear all watch history"]'
    POP_CLEAR_HISTORY_BUTTON = '//button[@aria-label="Clear watch history"]'
    MESSAGE_CLEAR_HISTORY = '//yt-formatted-string[@id="message"]'

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_clear_history_button(self):
        WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.CLEAR_HISTORY_BUTTON)))
        self._clear_history_button = self._driver.find_element(By.XPATH, self.CLEAR_HISTORY_BUTTON)
        self._clear_history_button.click()

    def click_on_pop_clear_history_button(self):
        WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.POP_CLEAR_HISTORY_BUTTON)))
        self._pop_clear_history_button = self._driver.find_element(By.XPATH, self.POP_CLEAR_HISTORY_BUTTON)
        self._pop_clear_history_button.click()

    def return_text_message_clear_history(self):
        time.sleep(2)
        self._message_history_button = self._driver.find_element(By.XPATH, self.MESSAGE_CLEAR_HISTORY)
        return self._message_history_button.text
