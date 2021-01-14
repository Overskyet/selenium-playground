import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

time.sleep(3)

driver.get("http://suninjuly.github.io/simple_form_find_task.html")
time.sleep(3)

# textArea = driver.find_element_by_css_selector("")

# textArea.send_keys("selenium")
# time.sleep(5)

button = driver.find_element_by_id("submit_button")

button.click()
time.sleep(5)

driver.quit()
