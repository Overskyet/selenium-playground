import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException


def sum(a, b):
  return a+b


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/selects2.html"

try: 
    browser.get(link)

    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "form")))

    a = browser.find_element(By.CSS_SELECTOR, "h2 span#num1")
    b = browser.find_element(By.CSS_SELECTOR, "h2 span#num2")
    result = sum(int(a.text), int(b.text))

    Select(browser.find_element(By.CSS_SELECTOR, "select#dropdown.custom-select")).select_by_value(str(result))

    browser.find_element(By.CSS_SELECTOR, "button[type=\"submit\"].btn.btn-default").click()

except NoSuchElementException as e:
    print("[X] NoSuchElement:\n --{}".format(e))

except TimeoutException as e:
    print("[X] Timeout:\n --Couldn't load resource link.\n --{}".format(e))

except WebDriverException as e:
    print("[X] WebDriverException:\n --Couldn't get link.\n --{}".format(e))

finally:
    time.sleep(5)
    browser.quit()

