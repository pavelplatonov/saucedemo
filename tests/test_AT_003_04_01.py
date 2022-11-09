import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

link = 'https://www.saucedemo.com/'

def test_login_to_item_card_irisamo():
    o = webdriver.ChromeOptions()
    o.headless = True
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )

    driver.get(link)

    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()
    time.sleep(2)

    assert driver.current_url == 'https://www.saucedemo.com/inventory.html'

    driver.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//div[@id="shopping_cart_container"]/a').click()
    time.sleep(2)

    assert driver.current_url == 'https://www.saucedemo.com/cart.html'

    itemNameBasketList = driver.find_element(By.XPATH, '//a[@id="item_0_title_link"]/div').text
    driver.find_element(By.XPATH, '//a[@id="item_0_title_link"]/div').click()
    time.sleep(2)
    itemNameItemCard = driver.find_element(
        By.XPATH, '//div[@id="inventory_item_container"]//div[@class="inventory_details_name large_size"]').text

    assert itemNameBasketList == itemNameItemCard

    driver.find_element(By.XPATH, '//div[@id="shopping_cart_container"]/a').click()
    time.sleep(2)

    assert driver.current_url == 'https://www.saucedemo.com/cart.html'

    driver.quit()