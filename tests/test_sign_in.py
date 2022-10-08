from utils import *
from locators import *
from inputs import *


# Вход через 'Войти в аккаунт'
def test_sign_in_with_button(driver):
    driver.implicitly_wait(3)
    driver.get(link)
    driver.find_element(By.XPATH, enter_into_account).click()
    driver.find_element(By.XPATH, login_email_field_xpath).send_keys(email)
    driver.find_element(By.XPATH, login_password_field_xpath).send_keys(password)
    driver.find_element(By.XPATH, login_enter_button_xpath).click()
    WebDriverWait(driver, 10).until(expected_conditions.url_matches(link))
    assert driver.current_url == link
    
# Вход через личный кабинет
def test_sign_in_with_personal_account(driver):
    driver.implicitly_wait(3)
    driver.get(link)
    cu = driver.current_url
    driver.find_element(By.XPATH, personal_account_button).click()
    WebDriverWait(driver, 10).until(expected_conditions.url_changes(cu))
    driver.find_element(By.XPATH, login_email_field_xpath).send_keys(email)
    driver.find_element(By.XPATH, login_password_field_xpath).send_keys(password)
    cu = driver.current_url
    driver.find_element(By.XPATH, login_enter_button_xpath).click()
    WebDriverWait(driver, 10).until(expected_conditions.url_changes(cu))
    assert driver.current_url == link

# Вход через кнопку логина в разделе регистрации
def test_sign_in_with_registration_section(driver):
    driver.implicitly_wait(3)
    driver.get(link + 'register')
    driver.find_element(By.XPATH, sign_in_button).click()
    WebDriverWait(driver, 10).until(expected_conditions.url_matches(link + 'login'))
    driver.find_element(By.XPATH, login_email_field_xpath).send_keys(email)
    driver.find_element(By.XPATH, login_password_field_xpath).send_keys(password)
    cu = driver.current_url
    driver.find_element(By.XPATH, login_enter_button_xpath).click()
    WebDriverWait(driver, 10).until(expected_conditions.url_changes(cu))
    assert driver.current_url == link

# Вход через 'Забыл пароль'
def test_sign_in_with_forgot_password(driver):
    driver.implicitly_wait(3)
    driver.get(link + 'forgot-password')
    driver.find_element(By.XPATH, forgot_password_sign_in_button).click()
    WebDriverWait(driver, 10).until(expected_conditions.url_matches(link + 'login'))
    driver.find_element(By.XPATH, login_email_field_xpath).send_keys(email)
    driver.find_element(By.XPATH, login_password_field_xpath).send_keys(password)
    cu = driver.current_url
    driver.find_element(By.XPATH, login_enter_button_xpath).click()
    WebDriverWait(driver, 10).until(expected_conditions.url_changes(cu))
    assert driver.current_url == link

