import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# infra    # logic
driver.get("https://www.google.com/")

# logic
search_input = driver.find_element(By.XPATH, "//*[@id='APjFqb']")
search_input.send_keys("Python programming")
search_input.send_keys(Keys.RETURN)


first_result = driver.find_element(By.CSS_SELECTOR, "h3")
print(f"The result is: \n{first_result.text}")


# infrastructure
driver.quit()