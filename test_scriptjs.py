import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
link = "https://suninjuly.github.io/execute_script.html"

try: 
    browser.get(link)

    element = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "label span#input_value")))

    result = calc(element.text)

    browser.find_element(By.CSS_SELECTOR, "input[type=\"text\"]#answer").send_keys(result)
    browser.find_element(By.CSS_SELECTOR, "div.form-check input[type=\"checkbox\"]#robotCheckbox").click()

    browser.execute_script("document.querySelector('footer').style.height=0;")
    
    browser.find_element(By.CSS_SELECTOR, "div.form-check input[type=\"radio\"]#robotsRule").click()
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

