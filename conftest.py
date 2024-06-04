import pytest
from selenium import webdriver


@pytest.fixture
def browser(request):
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    request.cls.browser = browser
    yield browser
    browser.quit()
