from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/registration2.html"
expectedResult = "Congratulations! You have successfully registered!"

try: 
    browser.get(link)

    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[required]")))

    browser.find_element(By.XPATH, "//label[contains(text(), \"First name*\")]/following-sibling::input").send_keys("Name")
    browser.find_element(By.XPATH, "//label[contains(text(), \"Last name*\")]/following-sibling::input").send_keys("Lastname")
    browser.find_element(By.XPATH, "//label[contains(text(), \"Email*\")]/following-sibling::input").send_keys("mail@mail.com")

    browser.find_element_by_css_selector("button.btn").click()

    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1")))

    welcome_text_elt = browser.find_element_by_tag_name("h1")

    assert expectedResult == welcome_text_elt.text
    print("[V] Assertion passed:\n --Actual result: {}\n --Expected result: {}".format(welcome_text_elt.text, expectedResult))

except AssertionError:
    print("[X] Assertion failed:\n --Actual result: {}\n --Expected result: {}".format(welcome_text_elt.text, expectedResult))

except NoSuchElementException as e:
    print("[X] NoSuchElement:\n --{}".format(e))

except TimeoutException as e:
    print("[X] Timeout:\n --Couldn't load resource link.\n --{}".format(e))

except WebDriverException as e:
    print("[X] WebDriverException:\n --Couldn't get link.\n --{}".format(e))

finally:
    browser.quit()

