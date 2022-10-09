from utils import *
from locators import *
from inputs import *


def test_registration_success(driver, random_name, random_email, random_password):
    driver.implicitly_wait(3)
    driver.get(link)
    driver.find_element(By.XPATH, account_button_xpath).click()
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be(link + 'login'))
    register = driver.find_element(By.XPATH, login_register_button)
    register.click()
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be(link + 'register'))
    name_field = driver.find_element(By.XPATH, name_xpath)
    name_field.send_keys(random_name)
    email_field = driver.find_element(By.XPATH, email_xpath)
    email_field.send_keys(random_email)
    password_field = driver.find_element(By.XPATH, password_xpath)
    password_field.send_keys(random_password)
    driver.find_element(By.XPATH, register_button_xpath).click()
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be(link + 'login'))
    assert driver.current_url == link + 'login'

def test_registration_with_bad_password(driver, random_name, random_email, random_password):
    driver.implicitly_wait(3)
    driver.get(link)
    driver.find_element(By.XPATH, account_button_xpath).click()
    register = driver.find_element(By.XPATH, login_register_button)
    register.click()
    name_field = driver.find_element(By.XPATH, name_xpath)
    name_field.send_keys(random_name)
    email_field = driver.find_element(By.XPATH, email_xpath)
    email_field.send_keys(random_email)
    password_field = driver.find_element(By.XPATH, password_xpath)
    password_field.send_keys(bad_password)
    driver.find_element(By.XPATH, register_button_xpath).click()
    #exists only after use bad password
    error = driver.find_element(By.XPATH, "//p[@class='input__error text_type_main-default']")
    assert error


