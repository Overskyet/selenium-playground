import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
link = "http://suninjuly.github.io/find_link_text"

try:
    driver.get(link)

    time.sleep(3)

    result = str(math.ceil(math.pow(math.pi, math.e)*10000))
    link = driver.find_element(By.LINK_TEXT, result)

    link.click()

    time.sleep(1)

    submitButton = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-default")

    firstNameField = driver.find_element(By.CSS_SELECTOR, "input[name=\"first_name\"]")
    lastNameField = driver.find_element(By.CSS_SELECTOR, "input[name=\"last_name\"]")
    cityField = driver.find_element(By.CSS_SELECTOR, "input.form-control.city")
    countryField = driver.find_element(By.CSS_SELECTOR, "input#country.form-control")

    firstNameField.send_keys("Baka")
    lastNameField.send_keys("Matte")
    cityField.send_keys("Moscow")
    countryField.send_keys("Russia")

    submitButton.click()

    time.sleep(5)

finally:
    driver.quit()
