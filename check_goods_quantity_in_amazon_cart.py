import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException

timeDelay = 1
driver = webdriver.Chrome()
expectedResult = 2
link1 = "https://www.amazon.com/Logitech-LIGHTSYNC-Wired-Gaming-Mouse/dp/B07YN82X3B/ref=pd_di_sccai_4/134-3776108-3013620?_encoding=UTF8&pd_rd_i=B07YN82X3B&pd_rd_r=71402062-44c4-44bb-a490-971693d5112c&pd_rd_w=gaUow&pd_rd_wg=BUYBr&pf_rd_p=c9443270-b914-4430-a90b-72e3e7e784e0&pf_rd_r=KCEHA6DG9CW17Z32MYAS&psc=1&refRID=KCEHA6DG9CW17Z32MYAS"
link2 = "https://www.amazon.com/Razer-DeathAdder-Elite-Mechanical-Ergonomic/dp/B01LXC1QL0/ref=pd_sbs_147_5/138-5612860-0710923?_encoding=UTF8&pd_rd_i=B01LXC1QL0&pd_rd_r=436fab22-a64c-4779-9430-9dcdee2e2611&pd_rd_w=LpVEi&pd_rd_wg=DsGuI&pf_rd_p=c52600a3-624a-4791-b4c4-3b112e19fbbc&pf_rd_r=G755TRRQ2JPA4P6STRG1&psc=1&refRID=G755TRRQ2JPA4P6STRG1"
cartLink = "https://www.amazon.com/gp/cart/view.html?ref_=nav_cart"

try:
    driver.get(link1)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#add-to-cart-button"))).click()

    driver.get(link2)
    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#add-to-cart-button"))).click()

    time.sleep(timeDelay)

    driver.get(cartLink)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-name=\"Active Items\"]")))
    goods = driver.find_elements(By.CSS_SELECTOR, "div[data-name=\"Active Items\"] div[data-itemtype=\"active\"]")

    assert len(goods) == expectedResult

    print("[V] Assertion passed:\n --Actual number of goods in a cart: [%s]\n --Expected result: [%s]" % (len(goods), expectedResult))

except NoSuchElementException:
    print("[X] Couldn't find given element")

except TimeoutException:
    print("[X] Couldn't load given resource link")

except WebDriverException:
    print("[X] Couldn't get link, check get() function")

except AssertionError:
    print("[X] Assertion failed:[X]\n --Actual number of goods in a cart: [%s]\n --Expected result: [%s]" % (len(goods), expectedResult))

finally:
    driver.quit()
