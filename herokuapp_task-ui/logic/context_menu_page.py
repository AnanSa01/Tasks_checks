from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

from Selenium_herokuapp_task.infra.base_page import BasePage


class ContextMenuPage(BasePage):
    BOX_CLICK = '//div[@id="hot-spot"]'
    ALERT_MESSAGE = '//div[@id="content"]//script'

    def __init__(self, driver):
        super().__init__(driver)
        self._box_click = self._driver.find_element(By.XPATH, self.BOX_CLICK)

    def right_click_on_box(self):
        print("Right click on box to display alert.")
        action = ActionChains(self._driver)
        action.context_click(self._box_click).perform()
