from selenium.webdriver.common.by import By
from herokuapp_task_UI_second_task.infra.base_page import BasePage


class BrokenImagesPage(BasePage):
    CHECK_IMAGES = '//div[@id="content"]//img'

    def __init__(self, driver):
        super().__init__(driver)
        self._check_all_images = self._driver.find_elements(By.XPATH, self.CHECK_IMAGES)

    def check_if_image_is_broken(self, requests=None, img=None):
        list_images = self._check_all_images
        print(f"In this test you have {len(list_images)} Images")
        i = 0
        for image in list_images:
            i += 1
            print(f"Result of image {i}: ", end="")
            if image.is_displayed():
                print("Is Diaplayed")
            else:
                print("Not!")

