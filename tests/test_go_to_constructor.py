from utils import *
from locators import *
from inputs import *


# Переход из личного кабинета в конструктор через кнопку "конструктор"
def test_go_to_constructor_with_constructor(logged_in):
    driver = logged_in
    driver.find_element(By.XPATH, personal_account_button).click()
    driver.find_element(By.XPATH, constructor_button).click()
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be(link))
    assert driver.current_url == link
    
# Переход из личного кабинета в конструктор через лого
def test_go_to_constructor_with_logo(logged_in):
    driver = logged_in
    driver.find_element(By.XPATH, personal_account_button).click()
    driver.find_element(By.XPATH, logo).click()
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be(link))
    assert driver.current_url == link
