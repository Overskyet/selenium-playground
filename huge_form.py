import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
link = "http://suninjuly.github.io/huge_form.html"

try:
    driver.get(link)

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".first_block")))

    elements = driver.find_elements(By.CSS_SELECTOR, ".first_block input")

    for element in elements:
        element.send_keys("test")

    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-default").click()

finally:
    time.sleep(10)
    driver.quit()

