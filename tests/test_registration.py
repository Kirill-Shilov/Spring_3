from utils import *

name = "Kirill"
email = "kirill_shilov5433@ya.ru"
password = "asdfgh"
bad_password = "12345"
link = "https://stellarburgers.nomoreparties.site"
name_xpath = "//label[text()='Имя']/following-sibling::input"
email_xpath = "//label[text()='Email']/following-sibling::input"
password_xpath = "//label[text()='Пароль']/following-sibling::input"
register_button_xpath = '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]'


def test_registration_success(driver):
    driver.get(link)
    driver.find_element(By.XPATH, "//a[@class='AppHeader_header__link__3D_hX'][@href='/account']").click()
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be(link+'/login'))
    driver.find_element(By.XPATH, "//a[@href='/register']").click()
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be(link + '/register'))
    name_field = driver.find_element(By.XPATH, name_xpath)
    name_field.send_keys(name)
    email_field = driver.find_element(By.XPATH, email_xpath)
    email_field.send_keys(email)
    password_field = driver.find_element(By.XPATH, password_xpath)
    password_field.send_keys(password)
    driver.find_element(By.XPATH, register_button_xpath).click()
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be(link + '/login'))

    assert driver.current_url == link + '/login'

def test_registration_with_bad_password(driver):
#    service = Service(executable_path=ChromeDriverManager().install())
#    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(3)
    driver.get(link)
    driver.find_element(By.XPATH, "//a[@class='AppHeader_header__link__3D_hX'][@href='/account']").click()
    driver.find_element(By.XPATH, "//a[@href='/register']").click()
    name_field = driver.find_element(By.XPATH, name_xpath)
    name_field.send_keys(name)
    email_field = driver.find_element(By.XPATH, email_xpath)
    email_field.send_keys(email)
    password_field = driver.find_element(By.XPATH, password_xpath)
    password_field.send_keys(bad_password)
    driver.find_element(By.XPATH, register_button_xpath).click()
    error = driver.find_element(By.XPATH, "//p[@class='input__error text_type_main-default']")
    
    assert error


