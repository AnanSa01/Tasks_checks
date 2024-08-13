from selenium import webdriver
from youtube_selenium_task.infra.config_provider import ConfigProvider
from selenium.common.exceptions import *


class BrowserWrapper:

    def __init__(self):
        self._driver = None
        self.config = ConfigProvider.load_from_file('../config.json')
        print("\nTest Start")

    def get_driver(self, url):
        try:
            if self.config["browser"] == "Chrome":
                self._driver = webdriver.Chrome()
            elif self.config["browser"] == "FireFox":
                self._driver = webdriver.Firefox()
            elif self.config["browser"] == "Edge":
                self._driver = webdriver.Edge()

            self._driver.get(url)
            self._driver.maximize_window()
            return self._driver
        except WebDriverException:
            print("There is an error while opening the browser")
