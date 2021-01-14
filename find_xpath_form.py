import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
link = "http://suninjuly.github.io/find_xpath_form"

try:
    driver.get(link)

    time.sleep(2)

    button = driver.find_element(By.XPATH, "//button[contains(text(), \"Submit\")]")

    # firstNameField = driver.find_element(
    #     By.CSS_SELECTOR, ".container form div:nth-child(1) input")
    firstNameField = driver.find_element(
        By.CSS_SELECTOR, "input[name=\"first_name\"]")
    # lastNameField = driver.find_element(
    #     By.CSS_SELECTOR, ".container form div:nth-child(2) input")
    lastNameField = driver.find_element(
        By.CSS_SELECTOR, "input[name=\"last_name\"]")
    # cityField = driver.find_element(
    #     By.CSS_SELECTOR, ".container form div:nth-child(3) input")
    cityField = driver.find_element(
        By.CSS_SELECTOR, ".form-control.city")
    # countrytNameField = driver.find_element(
    #     By.CSS_SELECTOR, ".container form div:nth-child(4) input")
    countrytNameField = driver.find_element(
        By.CSS_SELECTOR, "#country.form-control")

    firstNameField.send_keys("Baka")
    lastNameField.send_keys("Matte")
    cityField.send_keys("Moscow")
    countrytNameField.send_keys("Russia")

    button.click()

    time.sleep(5)

finally:
    driver.quit()

