from utils import *
from locators import *
from inputs import *


# Переход в личный кабинет
def test_go_to_personal_account_and_logout(logged_in):
    driver = logged_in
    driver.find_element(By.XPATH, personal_account_button).click()
    WebDriverWait(driver, 10).until(expected_conditions.url_changes(link))
    WebDriverWait(driver, 10).until(expected_conditions.url_matches(link + 'account/profile'))
    driver.find_element(By.XPATH, exit_button).click()
    WebDriverWait(driver, 10).until(expected_conditions.url_changes(link + 'account/profile'))
    assert driver.current_url == link + 'login'
    
