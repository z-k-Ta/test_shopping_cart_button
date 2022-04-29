import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store',default='ru',
                     help="input type language")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    yield browser
    time.sleep(3)
    print("\nquit browser..")
    browser.quit()
