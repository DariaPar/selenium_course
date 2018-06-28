import pytest
from selenium import webdriver


@pytest.fixture()
def driver(request):
    web_driver = webdriver.Chrome()
    request.addfinalizer(web_driver.quit)
    return web_driver


def test_login(driver):
    driver.get('http://localhost/litecart/admin/')
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_name('login').click()
    assert driver.find_element_by_css_selector('.fa-sign-out').is_displayed()
