import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="session")
def browser():
    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )
    browser.maximize_window()
    yield browser
    browser.quit()
