import datetime
from selenium.common.exceptions import NoSuchElementException
import os


class BasePage:
    def __init__(self, browser, link):
        self.browser = browser
        self.link = link

    """Открывает ссылку"""

    def open_page(self):
        self.browser.get(self.link)

    """Нажатие на выбранный элемент из локаторов"""

    def click_element(self, method, locator):
        self.browser.find_element(method, locator).click()

    """Передает текст или нажание кнопок на клавиатуре"""

    def keyboard_input(self, method, locator, keys_text):
        self.browser.find_element(method, locator).send_keys(keys_text)

    """Подтверждение наличия элемента на странице"""

    def element_is_present(self, method, locator):
        try:
            self.browser.find_element(method, locator)
        except NoSuchElementException:
            return False
        return True

    """Подтверждение текущего адреса страницы"""

    def should_be_current_page(self, link):
        assert link in self.browser.current_url, "wrong url"

    """скриншот результата"""

    def take_screenshot(self, test_name):
        screen_path = os.path.abspath("screenshots")
        now_date = datetime.datetime.now().strftime("_%H-%M-%S.%d.%m.%y.")
        name_screenshot = test_name + now_date + "png"
        self.browser.save_screenshot(screen_path + "/" + name_screenshot)
