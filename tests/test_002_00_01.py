import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
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


def test_find_product_cards():
    try:
        driver.find_elements_by_class_name("inventory_item_price")
    except NoSuchElementException:
        return False
    return True
    # len(driver.find_elements_class_name("inventory_item_price"))


def test_scrolling_keyboard():
    driver.find_element_css_selector("item_4_title_link").send_keys(Keys.END)
    time.sleep(2)
    driver.find_element_css_selector(".footer_copy").send_keys(Keys.HOME)
    time.sleep(2)
    driver.find_element_css_selector("item_4_title_link").send_keys(Keys.PAGE_DOWN)
    time.sleep(2)
    driver.find_element_css_selector(".footer_copy").send_keys(Keys.PAGE_UP)
