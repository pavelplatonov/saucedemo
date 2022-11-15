import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.saucedemo.com/")

def test_title():
    title_from_site = driver.title
    assert title_from_site == "Swag Labs"

def test_login_form():

    driver.find_element(By.CSS_SELECTOR, 'input#user-name').send_keys('standard_user')
    driver.find_element(By.XPATH, "//input[contains(@placeholder, 'Password')]").send_keys('secret_sauce')
    driver.find_element(By.CSS_SELECTOR, 'input#login-button').click()

    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "We are on another page!!!"
    time.sleep(2)

def click_on_icon():
    driver.find_element(By.XPATH, "//a[@id='item_4_title_link']").click()
    time.sleep(2)

    # icon_button = driver.find_element((By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']"))
    # icon_button.click()

    driver.quit()


