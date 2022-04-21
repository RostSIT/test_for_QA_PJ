import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en-gb', help='Choose language')


@pytest.fixture(scope='function')
def browser(request):
    language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    cookies = browser.get_cookies()
    print(f'main: cookies = {cookies}')
    browser.delete_all_cookies()
    browser.implicitly_wait(5)
    yield browser
    print('\nquit browser')
    browser.quit()

