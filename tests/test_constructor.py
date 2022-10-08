from utils import *
from locators import *
from inputs import *

# Чек того что при заходе на страницу видны первые две булки
def test_look_at_buns(logged_in):
    driver = logged_in
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, buns_button)))
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, first_bun)))
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, second_bun)))
    assert True

# Переход к соусам
def test_go_to_sauses(logged_in):
    driver = logged_in
    driver.find_element(By.XPATH, sauses_button).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, first_sause)))
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, second_sause)))
    assert True

# Переход к начинкам
def test_go_to_fillings(logged_in):
    driver = logged_in
    driver.find_element(By.XPATH, fillings_button).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, first_filling)))
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, second_filling)))
    assert True

# Переход к соусам и обратно к булкам
def test_go_to_sauses_and_back_to_buns(logged_in):
    driver = logged_in
    driver.find_element(By.XPATH, sauses_button).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, first_sause)))
    driver.find_element(By.XPATH, buns_button).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, first_bun)))
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, second_bun)))
    assert True
