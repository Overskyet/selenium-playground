import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException
from test_alert_window_parse_answer_value_and_copy_to_clipboard import parse_and_copy


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


def get_answer():
    alert = browser.switch_to.alert
    parse_and_copy(alert.text)
    alert.accept()



browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"

try: 
    browser.get(link)

    button = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type=\"submit\"].btn.btn-primary")))
    button.click()

    WebDriverWait(browser, 10).until(EC.alert_is_present())
    confirm = browser.switch_to.alert
    confirm.accept()

    value = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span#input_value")))
    result = calc(value.text)

    browser.find_element(By.CSS_SELECTOR, "input#answer").send_keys(result)
    browser.find_element(By.CSS_SELECTOR, "button[type=\"submit\"].btn.btn-primary").click()

    WebDriverWait(browser, 10).until(EC.alert_is_present())
    get_answer()


except NoSuchElementException as e:
    print("[X] NoSuchElement:\n --{}".format(e))

except TimeoutException as e:
    print("[X] Timeout:\n --Couldn't load resource link.\n --{}".format(e))

except WebDriverException as e:
    print("[X] WebDriverException:\n --Couldn't get link.\n --{}".format(e))

finally:
    time.sleep(5)
    browser.quit()

