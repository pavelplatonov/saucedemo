from pages.catalog_page import CatalogPage
from pages.locators import CatalogPageLocators

link = "https://www.saucedemo.com/"


def test_check_sorting_za_standard_user(browser):
    page = CatalogPage(browser, link)
    page.open_login_page()
    page.login_standard_user()
    page.enter_valid_password()
    page.click_login_btn()

    assert browser.current_url == "https://www.saucedemo.com/inventory.html"

    page.click_element(*CatalogPageLocators.SORT_WINDOW)
    page.click_element(*CatalogPageLocators.SORT_NAME_ZA)
    items_names = page.find_all_items_names_in_inventory()
    new_items_list = [x.text for x in items_names]

    assert new_items_list == sorted(
        new_items_list, reverse=True
    ), "Incorrect Z-A sorting"


def test_check_sorting_az_standard_user(browser):
    page = CatalogPage(browser, link)
    page.open_login_page()
    page.login_standard_user()
    page.enter_valid_password()
    page.click_login_btn()

    assert browser.current_url == "https://www.saucedemo.com/inventory.html"

    page.click_element(*CatalogPageLocators.SORT_WINDOW)
    page.click_element(*CatalogPageLocators.SORT_NAME_ZA)
    page.click_element(*CatalogPageLocators.SORT_NAME_AZ)
    items_names = page.find_all_items_names_in_inventory()
    new_items_list = [x.text for x in items_names]

    assert new_items_list == sorted(new_items_list), "Incorrect A-Z sorting"


def test_check_sorting_za_problem_user(browser):
    page = CatalogPage(browser, link)
    page.open_login_page()
    page.login_problem_user()
    page.enter_valid_password()
    page.click_login_btn()

    assert browser.current_url == "https://www.saucedemo.com/inventory.html"

    page.click_element(*CatalogPageLocators.SORT_WINDOW)
    page.click_element(*CatalogPageLocators.SORT_NAME_ZA)
    items_names = page.find_all_items_names_in_inventory()
    new_items_list = [x.text for x in items_names]

    assert new_items_list == sorted(
        new_items_list, reverse=True
    ), "Incorrect Z-A sorting"


def test_check_sorting_az_problem_user(browser):
    page = CatalogPage(browser, link)
    page.open_login_page()
    page.login_problem_user()
    page.enter_valid_password()
    page.click_login_btn()

    assert browser.current_url == "https://www.saucedemo.com/inventory.html"

    page.click_element(*CatalogPageLocators.SORT_WINDOW)
    page.click_element(*CatalogPageLocators.SORT_NAME_ZA)
    page.click_element(*CatalogPageLocators.SORT_NAME_AZ)
    items_names = page.find_all_items_names_in_inventory()
    new_items_list = [x.text for x in items_names]

    assert new_items_list == sorted(new_items_list), "Incorrect A-Z sorting"


def test_check_sorting_high_low_standard_user(browser):
    page = CatalogPage(browser, link)
    page.open_login_page()
    page.login_standard_user()
    page.enter_valid_password()
    page.click_login_btn()

    assert browser.current_url == "https://www.saucedemo.com/inventory.html"

    page.click_element(*CatalogPageLocators.SORT_WINDOW)
    page.click_element(*CatalogPageLocators.SORT_PRICE_HIGH_LOW)

    items_cost = page.find_all_items_cost_in_inventory()
    new_items_cost = [float(x.text.replace("$", "")) for x in items_cost]

    assert new_items_cost == sorted(
        new_items_cost, reverse=True
    ), "Incorrect High-Low sorting"


def test_check_sorting_high_low_problem_user(browser):
    page = CatalogPage(browser, link)
    page.open_login_page()
    page.login_problem_user()
    page.enter_valid_password()
    page.click_login_btn()

    assert browser.current_url == "https://www.saucedemo.com/inventory.html"

    page.click_element(*CatalogPageLocators.SORT_WINDOW)
    page.click_element(*CatalogPageLocators.SORT_PRICE_HIGH_LOW)

    items_cost = page.find_all_items_cost_in_inventory()
    new_items_cost = [float(x.text.replace("$", "")) for x in items_cost]

    assert new_items_cost == sorted(
        new_items_cost, reverse=True
    ), "Incorrect High-Low sorting"


def test_check_sorting_low_high_standard_user(browser):
    page = CatalogPage(browser, link)
    page.open_login_page()
    page.login_standard_user()
    page.enter_valid_password()
    page.click_login_btn()

    assert browser.current_url == "https://www.saucedemo.com/inventory.html"

    page.click_element(*CatalogPageLocators.SORT_WINDOW)
    page.click_element(*CatalogPageLocators.SORT_PRICE_LOW_HIGH)

    items_cost = page.find_all_items_cost_in_inventory()
    new_items_cost = [float(x.text.replace("$", "")) for x in items_cost]

    assert new_items_cost == sorted(new_items_cost), "Incorrect Low-High sorting"


def test_check_sorting_low_high_problem_user(browser):
    page = CatalogPage(browser, link)
    page.open_login_page()
    page.login_problem_user()
    page.enter_valid_password()
    page.click_login_btn()

    assert browser.current_url == "https://www.saucedemo.com/inventory.html"

    page.click_element(*CatalogPageLocators.SORT_WINDOW)
    page.click_element(*CatalogPageLocators.SORT_PRICE_LOW_HIGH)

    items_cost = page.find_all_items_cost_in_inventory()
    new_items_cost = [float(x.text.replace("$", "")) for x in items_cost]

    assert new_items_cost == sorted(new_items_cost), "Incorrect Low-High sorting"
