import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
file_path = os.path.join(os.getcwd(), "test-text.txt")

try: 
    browser.get(link)

    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.form-group")))

    browser.find_element(By.CSS_SELECTOR, "div.form-group input[type=\"text\"][name=\"firstname\"]").send_keys("Name")
    browser.find_element(By.CSS_SELECTOR, "div.form-group input[type=\"text\"][name=\"lastname\"]").send_keys("Lastname")
    browser.find_element(By.CSS_SELECTOR, "div.form-group input[type=\"text\"][name=\"email\"]").send_keys("mail@mail.com")

    browser.find_element(By.CSS_SELECTOR, "input[type=\"file\"][accept=\".txt\"]#file").send_keys(file_path)

    browser.find_element(By.CSS_SELECTOR, "button[type=\"submit\"].btn.btn-primary").click()


except NoSuchElementException as e:
    print("[X] NoSuchElement:\n --{}".format(e))

except TimeoutException as e:
    print("[X] Timeout:\n --Couldn't load resource link.\n --{}".format(e))

except WebDriverException as e:
    print("[X] WebDriverException:\n --Couldn't get link.\n --{}".format(e))

finally:
    time.sleep(5)
    browser.quit()

