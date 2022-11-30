from selenium.webdriver.common.by import By


"""Локаторы общие для всех страниц"""


class MainPageLocators:
    BASE_ICON = (By.CSS_SELECTOR, ".login_logo")

    # локаторы выпадающего меню и кнопка бутерброд
    MENU_BTN = (By.CSS_SELECTOR, "#react-burger-menu-btn")
    SIDEBAR_BTN_ALL = (By.CSS_SELECTOR, "#inventory_sidebar_link")
    SIDEBAR_BTN_ABOUT = (By.CSS_SELECTOR, "#about_sidebar_link")
    SIDEBAR_BTN_LOGOUT = (By.CSS_SELECTOR, "#logout_sidebar_link")
    SIDEBAR_BTN_RESET = (By.CSS_SELECTOR, "#reset_sidebar_link")
    SIDEBAR_BTN_CROSS = (By.CSS_SELECTOR, "#react-burger-cross-btn")

    # локатор иконки корзины
    CART_BTN = (By.XPATH, "//a[@class='shopping_cart_link']")
    CART_BTN_BAGE = (By.CSS_SELECTOR, ".shopping_cart_badge")

    # локаторы подвала
    FOOTER_TEXT = (By.CSS_SELECTOR, ".footer_copy")


"""Локаторы страницы авторизации"""


class LoginPageLocators:
    LOGIN_FORM = (By.XPATH, "(//form)[1]")
    LOGIN_USER = (By.CSS_SELECTOR, "#user-name")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#password")
    LOGIN_LIST = (By.CSS_SELECTOR, ".login_credentials_wrap-inner")
    LOGIN_BTN = (By.CSS_SELECTOR, "#login-button")
    ERROR_WARNING = (By.XPATH, "//h3[@data-test='error']")
    ERROR_WARNING_1 = (By.CSS_SELECTOR, "h3[data-test]")
    ERROR_ITEM_ON_NAME_FIELD = (By.CSS_SELECTOR, "#user-name + svg")
    ERROR_ITEM_ON_PASSWORD_FIELD = (By.CSS_SELECTOR, "#password + svg")
    ERROR_ELEMENT_BOTTOM_COLOR = (By.CSS_SELECTOR, ".input_error.error")


"""Локаторы страницы каталога"""


class CatalogPageLocators:
    # локаторы кнопки сортировка каталога и карточек товара
    SORT_WINDOW = (By.XPATH, "//select[@class='product_sort_container']")
    CATALOGUE_LIST = (By.XPATH, "(//div[@class='inventory_item'])")

    # локаторы карточки рюкзака
    ITEM_NAME_BACKPACK = (By.CSS_SELECTOR, "#item_4_title_link > div")
    ITEM_IMG_BACKPACK = (By.CSS_SELECTOR, "#item_4_img_link > img")
    ITEM_DESC_BACKPACK = (
        By.XPATH,
        "(//div[@class = 'inventory_item_desc'])[1]",
    )
    PRICE_BACKPACK = (By.XPATH, "(//div[@class = 'inventory_item_price'])[1]")
    BTN_ADD_BACKPACK = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
    BTN_REMOVE_BACKPACK = (By.CSS_SELECTOR, "#remove-sauce-labs-backpack")

    # локаторы серой футболки
    ITEM_NAME_BOLT_T_SHIRT = (By.CSS_SELECTOR, "#item_1_title_link")
    ITEM_IMG_BOLT_T_SHIRT = (By.CSS_SELECTOR, "#item_1_img_link > img")
    ITEM_DESC_BOLT_T_SHIRT = (
        By.XPATH,
        "(//div[@class = 'inventory_item_desc'])[3]",
    )
    PRICE_BOLT_T_SHIRT = (
        By.XPATH,
        "(//div[@class = 'inventory_item_price'])[3]",
    )
    BTN_ADD_BOLT_T_SHIRT = (
        By.CSS_SELECTOR,
        "#add-to-cart-sauce-labs-bolt-t-shirt",
    )
    BTN_REMOVE_BOLT_T_SHIRT = (
        By.CSS_SELECTOR,
        "#remove-sauce-labs-bolt-t-shirt",
    )

    # локаторы красной кофты
    ITEM_NAME_ONESIE = (By.CSS_SELECTOR, "#item_2_title_link")
    ITEM_IMG_ONESIE = (By.CSS_SELECTOR, "#item_2_img_link")
    ITEM_DESC_ONESIE = (By.XPATH, "(//div[@class = 'inventory_item_desc'])[5]")
    PRICE_ONESIE = (By.XPATH, "(//div[@class = 'inventory_item_price'])[5]")
    BTN_ADD_ONESIE = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
    BTN_REMOVE_ONESIE = (By.CSS_SELECTOR, "#remove-sauce-labs-onesie")

    # локаторы карточки велосвета
    ITEM_NAME_BIKE_LIGHT = (By.CSS_SELECTOR, "#item_0_title_link")
    ITEM_IMG_BIKE_LIGHT = (By.CSS_SELECTOR, "#item_0_img_link")
    ITEM_DESC_BIKE_LIGHT = (
        By.XPATH,
        "(//div[@class = 'inventory_item_desc'])[2]",
    )
    PRICE_BIKE_LIGHT = (
        By.XPATH,
        "(//div[@class = 'inventory_item_price'])[2]",
    )
    BTN_ADD_BIKE_LIGHT = (
        By.CSS_SELECTOR,
        "#add-to-cart-sauce-labs-bike-light",
    )
    BTN_REMOVE_BIKE_LIGHT = (By.CSS_SELECTOR, "#remove-sauce-labs-bike-light")

    # локаторы серой кофты
    ITEM_NAME_FLEECE_JACKET = (By.CSS_SELECTOR, "#item_5_title_link")
    ITEM_IMG_FLEECE_JACKET = (By.CSS_SELECTOR, "##item_5_img_link")
    ITEM_DESC_FLEECE_JACKET = (
        By.XPATH,
        "(//div[@class = 'inventory_item_desc'])[4]",
    )
    PRICE_FLEECE_JACKET = (
        By.XPATH,
        "(//div[@class = 'inventory_item_price'])[4]",
    )
    BTN_ADD_FLEECE_JACKET = (
        By.CSS_SELECTOR,
        "#add-to-cart-sauce-labs-fleece-jacket",
    )
    BTN_REMOVE_FLEECE_JACKET = (
        By.CSS_SELECTOR,
        "#remove-sauce-labs-fleece-jacket",
    )

    # локаторы красной футболки
    ITEM_NAME_T_SHIRT = (By.CSS_SELECTOR, "#item_3_title_link")
    ITEM_IMG_T_SHIRT = (By.CSS_SELECTOR, "#item_3_img_link")
    ITEM_DESC_T_SHIRT = (
        By.XPATH,
        "(//div[@class = 'inventory_item_desc'])[6]",
    )
    PRICE_T_SHIRT = (By.XPATH, "(//div[@class = 'inventory_item_price'])[6]")
    BTN_ADD_T_SHIRT = (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
    BTN_REMOVE_T_SHIRT = (By.ID, "remove-test.allthethings()-t-shirt-(red)")


class ItemPageLocators:
    """Большие карточки товара."""

    BTN_BACK_TO_PRODUCTS = (By.CSS_SELECTOR, "#back-to-products")

    BIG_ITEM_NAME_BACKPACK = (By.CSS_SELECTOR, ".inventory_details_name")
    BIG_ITEM_IMG_BACKPACK = (By.CSS_SELECTOR, ".inventory_details_img")
    BIG_ITEM_DESC_BACKPACK = (By.CSS_SELECTOR, ".inventory_details_desc")
    BIG_PRICE_BACKPACK = (By.CSS_SELECTOR, ".inventory_details_price")
    BIG_BTN_ADD_BACKPACK = (
        By.CSS_SELECTOR,
        "#add-to-cart-sauce-labs-backpack",
    )
    BIG_BTN_REMOVE_BACKPACK = (By.CSS_SELECTOR, "#remove-sauce-labs-backpack")

    IN_BASKET = (By.XPATH, '//*[@class="inventory_item_name"]')


"""Локаторы страницы корзины"""


class CartPageLocators:
    BTN_CHECKOUT = (By.CSS_SELECTOR, "#checkout")
    BTN_CONTINUE = (By.XPATH, "//input[@id='continue']")

"""Локаторы страницы карточки товара"""


"""Локаторы страницы оформления заказа"""


class CheckoutPageLocators:
    FIELD_FIRST_NAME = (By.CSS_SELECTOR, "#first-name")
    FIELD_LAST_NAME = (By.CSS_SELECTOR, "#last-name")
    FIELD_ZIP_CODE = (By.CSS_SELECTOR, "#postal-code")
    EMPTY = "empty_first_name"

class FinishPageLocators:
    BTN_FINISH = (By.CSS_SELECTOR, "#finish")
    BTN_CANCEL = (By.XPATH, "//button[@id='cancel']")
    BTN_BACK_HOME = (By.CSS_SELECTOR, "#back-to-products")

class CompletePageLocators:
    IMG_PONY_EXPRESS = (By.XPATH, "//img[@alt='Pony Express']")



"""Надо дописывать локаторы на большие карточки товара и другие TC!!!"""
