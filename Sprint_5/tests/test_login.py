from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
import random

driver = webdriver.Chrome()

class TestLogin:

    def setup(self):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

    def teardown(self):
        driver.quit()

    def test_login(self):
        self.setup()

        # Залогиниться созданным пользователем
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.login_and_register_button))
        ).click()

        driver.find_element(By.XPATH, Locators.email_field).send_keys(Locators.login_email)
        driver.find_element(By.XPATH, Locators.password_field).send_keys(Locators.login_password)
        
        driver.find_element(By.XPATH, Locators.login_button).click()

        # Проверки ОР
        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.user_name))
        ).text == 'User.'

        assert driver.find_element(By.XPATH, Locators.user_avatar).is_displayed()

        self.teardown()