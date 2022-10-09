from utils import *
from locators import *
from inputs import *


# Переход в личный кабинет
def test_go_to_personal_account(logged_in):
    driver = logged_in
    driver.find_element(By.XPATH, personal_account_button).click()
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be(link + 'account/profile'))
    assert driver.current_url == link + 'account/profile'
