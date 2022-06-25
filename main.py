from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

# CHROME_DRIVER_PATH = "C:\ChromeDriver\chromedriver.exe"

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("http://orteil.dashnet.org/cookieclicker/")
browser.set_window_size(1920, 1080)
browser.maximize_window()

browser.find_element(By.CSS_SELECTOR, "#langSelect-EN").click()  # choose English language

cookie = browser.find_element(By.CSS_SELECTOR, "#bigCookie")

while True:
    for _ in range(10):
        cookie.click()
        sleep(0.004)

    upgrades = browser.find_elements(By.CSS_SELECTOR, "#upgrades div.crate.upgrade.enabled")
    for option in reversed(upgrades):
        option.click()

    shop = browser.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")
    for option in reversed(shop):
        option.click()
