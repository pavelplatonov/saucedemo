from selenium.webdriver.common.by import By


class LoginLocators:
    login_field = (By.ID, "user-name")
    password_field = (By.ID, "password")
    login_btn = (By.ID, "login-button")
    error_warning = (By.XPATH, '//h3[@data-test="error"]')
