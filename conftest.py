import pytest

from tests.locators import *
from tests.inputs import link, email, password
from tests.utils import *

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import random
import string


def random_char(char_num):
       return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

@pytest.fixture
def random_name():
    return 'kirill_shilov_' + random_char(10)

@pytest.fixture
def random_email():
    return random_char(10) + '@ya.ru'

@pytest.fixture
def random_password():
    return random_char(6)

@pytest.fixture
def driver():
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.close()


@pytest.fixture
def logged_in(driver):
    driver.implicitly_wait(3)
    driver.get(link)
    driver.find_element(By.XPATH, enter_into_account).click()
    driver.find_element(By.XPATH, login_email_field_xpath).send_keys(email)
    driver.find_element(By.XPATH, login_password_field_xpath).send_keys(password)
    driver.find_element(By.XPATH, login_enter_button_xpath).click()
    WebDriverWait(driver, 5).until(expected_conditions.url_matches(link))
    return driver

