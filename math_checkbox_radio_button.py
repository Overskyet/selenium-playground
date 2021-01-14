import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/math.html"

try: 
    browser.get(link)

    element = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span#input_value")))

    result = calc(element.text)

    browser.find_element(By.CSS_SELECTOR, "input#answer").send_keys(result)
    browser.find_element(By.CSS_SELECTOR, "input[type=\"checkbox\"]#robotCheckbox").click()
    browser.find_element(By.CSS_SELECTOR, "input[type=\"radio\"]#robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, "button[type=\"submit\"].btn.btn-default").click()

except NoSuchElementException as e:
    print("[X] NoSuchElement:\n --{}".format(e))

except TimeoutException as e:
    print("[X] Timeout:\n --Couldn't load resource link.\n --{}".format(e))

except WebDriverException as e:
    print("[X] WebDriverException:\n --Couldn't get link.\n --{}".format(e))

finally:
    time.sleep(3)
    browser.quit()

