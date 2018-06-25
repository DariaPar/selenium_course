import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture()
def driver(request):
    web_driver = webdriver.Chrome()
    request.addfinalizer(web_driver.quit)
    return web_driver

def test_first_selenium(driver):
    driver.get('http://selenium-python.readthedocs.io/')
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#selenium-with-python h1'),
                                    'Selenium with Python'))
