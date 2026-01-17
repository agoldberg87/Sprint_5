from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
import random

driver = webdriver.Chrome()

class TestRegistration:

    def setup(self):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

    def teardown(self):
        driver.quit()

    def test_registration(self):

        self.setup()
        
        # Зарегистрироваться
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.login_and_register_button))
        ).click()
        
        driver.find_element(By.XPATH, Locators.no_account_button).click()

        # Сгенерировать креды
        email = f"test"+str(random.randint(1000, 9999))+"@test.ru"
        password = str(random.randint(10000000, 99999999))

        driver.find_element(By.XPATH, Locators.email_field).send_keys(email)
        driver.find_element(By.XPATH, Locators.password_field).send_keys(password)
        driver.find_element(By.XPATH, Locators.repeat_password_field).send_keys(password)
        
        driver.find_element(By.XPATH, Locators.register_button).click()

        # Проверки ОР
        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.user_name))
        ).text == 'User.'

        assert driver.find_element(By.XPATH, Locators.user_avatar).is_displayed()

        self.teardown()

    
    def test_registration_email_no_mask_returns_error(self):

        self.setup()
        
        # Зарегистрировать пользователя
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.login_and_register_button))
        ).click()
        
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.no_account_button))
        ).click()

        # Сгенерировать креды не по маске
        email = f"test"+str(random.randint(1000, 9999))
        password = str(random.randint(10000000, 99999999))

        driver.find_element(By.XPATH, Locators.email_field).send_keys(email)
        driver.find_element(By.XPATH, Locators.password_field).send_keys(password)
        driver.find_element(By.XPATH, Locators.repeat_password_field).send_keys(password)
        
        driver.find_element(By.XPATH, Locators.register_button).click()

        # Проверки ОР
        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.error_notice))
        ).text == 'Ошибка' 
        
        for i in driver.find_elements(By.XPATH, Locators.input_parent):
            assert i.value_of_css_property('border-top-color') == 'rgba(255, 105, 114, 1)'

        self.teardown()


    def test_registration_existing_user_returns_error(self):

        self.setup()
        
        # Создать пользователя
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.login_and_register_button))
        ).click()
        
        driver.find_element(By.XPATH, Locators.no_account_button).click()

        # Сгенерировать креды
        email = f"test"+str(random.randint(1000, 9999))+"@test.ru"
        password = str(random.randint(10000000, 99999999))

        driver.find_element(By.XPATH, Locators.email_field).send_keys(email)
        driver.find_element(By.XPATH, Locators.password_field).send_keys(password)
        driver.find_element(By.XPATH, Locators.repeat_password_field).send_keys(password)
        
        driver.find_element(By.XPATH, Locators.register_button).click()

        # Разлогиниться
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.logout_button))
        ).click()

        # Создать пользователя повторно с уже использованными кредами
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.login_and_register_button))
        ).click()
        
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.no_account_button))
        ).click()

        driver.find_element(By.XPATH, Locators.email_field).send_keys(email)
        driver.find_element(By.XPATH, Locators.password_field).send_keys(password)
        driver.find_element(By.XPATH, Locators.repeat_password_field).send_keys(password)
        
        driver.find_element(By.XPATH, Locators.register_button).click()

        # Проверки ОР
        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.error_notice))
        ).text == 'Ошибка'

        for i in driver.find_elements(By.XPATH, Locators.input_parent):
            assert i.value_of_css_property('border-top-color') == 'rgba(255, 105, 114, 1)'

        self.teardown()
    