from idlelib import browser
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


link = "https://www.saucedemo.com/"
valid_user = "standard_user"
locked_out_user = "locked_out_user"
problem_user = "problem_user"
performance_glitch_user = "performance_glitch_user"
valid_password = "secret_sauce"
link_2 = "https://www.saucedemo.com/inventory.html"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(link)

"""TC_002.00.01 | Выполнение предварительных условий"""


def test_login_form():
    user_name = driver.find_element(By.CSS_SELECTOR, "#user-name")
    user_name.send_keys(valid_user)

    password = driver.find_element(By.CSS_SELECTOR, "#password")
    password.send_keys(valid_password)

    button_login = driver.find_element(By.CSS_SELECTOR, "#login-button")
    button_login.click()

    assert driver.current_url == 'https://www.saucedemo.com/inventory.html', 'We reached another site!!!'


"""TC_002.00.01 | Страница каталога > Просмотр каталога товаров"""


def test_open_catalog_page(browser, page=None):
    page.should_be_current_page(link_2)

# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get(link)
#
# driver.find_element_by_tag_name('body').send_keys(Keys.END)
# # Use send_keys(Keys.HOME) to scroll up to the top of page
# """Обратите внимание, что send_keys(Keys.DOWN) / send_keys(Keys.UP) и
# send_keys(Keys.PAGE_DOWN) / send_keys(Keys.PAGE_UP) также могут использоваться для прокрутки"""
