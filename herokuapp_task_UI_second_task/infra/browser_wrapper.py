from selenium import webdriver
from herokuapp_task_UI_second_task.infra.config_provider import ConfigProvider


class BrowserWrapper:

    def __init__(self):
        self._driver = None
        self.config = ConfigProvider.load_from_file('../config.json')
        print("\nTest Start")

    def get_driver(self, url):
        if self.config["browser"] == "Chrome":
            self._driver = webdriver.Chrome()
        elif self.config["browser"] == "FireFox":
            self._driver = webdriver.Firefox()
        elif self.config["browser"] == "Edge":
            self._driver = webdriver.Edge()

        self._driver.get(url)
        #self._driver.maximize_window()
        return self._driver
