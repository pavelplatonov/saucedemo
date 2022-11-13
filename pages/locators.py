from selenium.webdriver.common.by import By


class BasePageLocators():
    BASE_ICON = (By.CSS_SELECTOR, ".login_logo")


class LoginPageLocators():
    LOGIN_FORM = (By.XPATH, "(//form)[1]")
    LOGIN_USER = (By.XPATH, "//input[@id = 'user-name']")
    LOGIN_PASSWORD = (By.XPATH, "//input[@id = 'password']")
    LOGIN_LIST = (By.CSS_SELECTOR, ".login_credentials_wrap-inner")
    LOGIN_BTN = (By.XPATH, "//input[@id = 'login-button']")
    ERROR_WARNING = (By.XPATH, "//h3[@data-test='error']")
    ERROR_WARNING_1 = (By.CSS_SELECTOR, "h3[data-test]")


class CatalogPageLocators():
    MENU_BTN = (By.CSS_SELECTOR, "#react-burger-menu-btn")
    SIDEBAR_BTN_ALL = (By.CSS_SELECTOR, "#inventory_sidebar_link")
    SIDEBAR_BTN_ABOUT = (By.CSS_SELECTOR, "#about_sidebar_link")
    SIDEBAR_BTN_LOGOUT = (By.CSS_SELECTOR, "#logout_sidebar_link")
    SIDEBAR_BTN_RESET = (By.CSS_SELECTOR, "#reset_sidebar_link")
    SIDEBAR_BTN_CROSS = (By.CSS_SELECTOR, "#react-burger-cross-btn")

    CART_BTN = (By.XPATH, "//a[@class='shopping_cart_link']")
    SORT_WINDOW = (By.XPATH, "//select[@class='product_sort_container']")

    CATALOGUE_LIST = (By.XPATH, '//div[@class="inventory_item"]')
    ITEM_NAME_BACKPACK = (By.CSS_SELECTOR, "#item_4_title_link")
    ITEM_IMG_BACKPACK = (By.CSS_SELECTOR, "#item_4_img_link")
    ITEM_DESC_BACKPACK = (By.XPATH, "//div[contains(text(),'carry.allTheThings() with the sleek, streamlined S')]']")
    PRICE_BACKPACK = (By.XPATH, "//div[normalize-space()='$29.99']")
    BTN_ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    BTN_REMOVE_BACKPACK = (By.ID, "remove-sauce-labs-backpack")

    ITEM_NAME_BOLT_T_SHIRT = (By.CSS_SELECTOR, "#item_1_title_link")
    ITEM_IMG_BOLT_T_SHIRT = (By.CSS_SELECTOR, "#item_1_img_link")
    ITEM_DESC_BOLT_T_SHIRT = (By.XPATH, "//div[contains(text(),'Get your testing superhero on with the Sauce Labs ')]")
    PRICE_BOLT_T_SHIRT = (By.XPATH, "//body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/div[2]/"
                                    "div[1]']")
    BTN_ADD_BOLT_T_SHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    BTN_REMOVE_BOLT_T_SHIRT = (By.ID, "remove-sauce-labs-bolt-t-shirt")

    ITEM_NAME_ONESIE = (By.CSS_SELECTOR, "#item_2_title_link")
    ITEM_IMG_ONESIE = (By.CSS_SELECTOR, "#item_2_img_link")
    ITEM_DESC_ONESIE = (By.XPATH, "//div[contains(text(),'Rib snap infant onesie for the junior automation e')]")
    PRICE_ONESIE = (By.XPATH, "//*[@id='inventory_container']/div/div[5]/div[2]/div[2]/div")
    BTN_ADD_ONESIE = (By.ID, "add-to-cart-sauce-labs-onesie")
    BTN_REMOVE_ONESIE = (By.ID, "remove-sauce-labs-onesie")

    ITEM_NAME_BIKE_LIGHT = (By.CSS_SELECTOR, "#item_0_title_link")
    ITEM_IMG_BIKE_LIGHT = (By.CSS_SELECTOR, "#item_0_img_link")
    ITEM_DESC_BIKE_LIGHT = (By.XPATH, "//div[contains(text(),'A red ')]")
    PRICE_BIKE_LIGHT = (By.XPATH, "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div")
    BTN_ADD_BIKE_LIGHT = (By.ID, "add-to-cart-sauce-labs-bike-light")
    BTN_REMOVE_BIKE_LIGHT = (By.ID, "remove-sauce-labs-bike-light")

    ITEM_NAME_FLEECE_JACKET = (By.CSS_SELECTOR, "#item_5_title_link")
    ITEM_IMG_FLEECE_JACKET = (By.CSS_SELECTOR, "##item_5_img_link")
    ITEM_DESC_FLEECE_JACKET = (By.XPATH, "//*[@id='inventory_container']/div/div[4]/div[2]/div[1]/div")
    PRICE_FLEECE_JACKET = (By.XPATH, "//*[@id='inventory_container']/div/div[4]/div[2]/div[2]/div")
    BTN_ADD_FLEECE_JACKET = (By.ID, "add-to-cart-sauce-labs-fleece-jacket")
    BTN_REMOVE_FLEECE_JACKET = (By.ID, "remove-sauce-labs-fleece-jacket")

    ITEM_NAME_T_SHIRT = (By.CSS_SELECTOR, "#item_3_title_link")
    ITEM_IMG_T_SHIRT = (By.CSS_SELECTOR, "#item_3_img_link")
    ITEM_DESC_T_SHIRT = (By.XPATH, "//div[normalize-space()='This classic Sauce Labs t-shirt is perfect to wear "
                                   "when cozying up to your keyboard to automate a few tests. Super-soft and comfy "
                                   "ringspun combed cotton.']")
    PRICE_T_SHIRT = (By.XPATH, "//div[@class='inventory_list']//div[1]//div[2]//div[2]//div[1]")
    BTN_ADD_T_SHIRT = (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
    BTN_REMOVE_T_SHIRT = (By.ID, "remove-test.allthethings()-t-shirt-(red)")

    FOOTER_TEXT = (By.CSS_SELECTOR, ".footer_copy")

    """Большие катрочки товара."""
    BTN_BACK_TO_PRODUCTS = (By.CSS_SELECTOR, "#back-to-products")

    BIG_ITEM_NAME_BACKPACK = (By.XPATH, "//div[@class='inventory_details_name large_size']")
    BIG_ITEM_IMG_BACKPACK = (By.CSS_SELECTOR, "#item_4_img_link")
    BIG_ITEM_DESC_BACKPACK = (By.XPATH, "//div[contains(text(),'carry.allTheThings() with the sleek, streamlined S')]']")
    BIG_PRICE_BACKPACK = (By.XPATH, "//div[normalize-space()='$29.99']")
    BIG_BTN_ADD_BACKPACK = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
    BIG_BTN_REMOVE_BACKPACK = (By.CSS_SELECTOR, "#remove-sauce-labs-backpack")
