from pages.login_page import LoginPage
from pages.locators import CheckoutPageLocators


first_name = "Вилле"
last_name = "Хаапасало"
zip_code = "2566"

class CheckoutPage(LoginPage):

     # Ввод валидных данных в поле First_Name / Last_name / Zip/Postal_code

    def input_valid_first_name(self):
        self.keyboard_input(*CheckoutPageLocators.FIELD_FIRST_NAME, first_name)

    def input_valid_last_name(self):
        self.keyboard_input(*CheckoutPageLocators.FIELD_LAST_NAME, last_name)

    def input_valid_zip_code(self):
        self.keyboard_input(*CheckoutPageLocators.FIELD_ZIP_CODE, zip_code)


