from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
import random

driver = webdriver.Chrome()

class TestPlaceAd:

    def setup(self):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

    def teardown(self):
        driver.quit()

    def test_place_ad_no_registration_returns_error(self):
        self.setup()

        # Разместить объявление
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.place_ad_button))
        ).click()

        # Проверка ОР
        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.authorization_notice))
        ).text == 'Чтобы разместить объявление, авторизуйтесь'

        self.teardown()

    
    def test_place_ad_registration_completed(self):
        self.setup()

        # Залогиниться созданным пользователем
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.login_and_register_button))
        ).click()

        driver.find_element(By.XPATH, Locators.email_field).send_keys(Locators.login_email)
        driver.find_element(By.XPATH, Locators.password_field).send_keys(Locators.login_password)
        
        driver.find_element(By.XPATH, Locators.login_button).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.user_avatar))
        )

        # Разместить объявление
        WebDriverWait(driver, 15).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Locators.place_ad_button))
        ).click()

        dummy_price = random.randint(1000, 9999)
        dummy_text = f"Тестовое объявление " + str(dummy_price)

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.ad_name_field))
        ).send_keys(dummy_text) # Название

        driver.find_element(By.XPATH, Locators.ad_description_field).send_keys(dummy_text) # Описание (совпадает с названием)

        driver.find_element(By.XPATH, Locators.ad_price_field).send_keys(dummy_price) # Цена

        # Рандомно выбрать город
        driver.find_element(By.XPATH, Locators.city_dropdown_button).click()
        city_options = driver.find_elements(By.XPATH, Locators.city_options)
        if city_options:
            random_index = random.randint(0, len(city_options) - 1)
            city_options[random_index].click()

        # Рандомно выбрать категорию
        driver.find_element(By.XPATH, Locators.category_dropdown_button).click()
        category_options = driver.find_elements(By.XPATH, Locators.category_options)
        if category_options:
            random_index = random.randint(0, len(category_options) - 1)
            category_options[random_index].click()

        driver.find_elements(By.XPATH, Locators.condition_radio_buttons)[random.randint(0, len(driver.find_elements(By.XPATH, Locators.condition_radio_buttons)) - 1)].click() # Рандомно выбрать состояние

        driver.find_element(By.XPATH, Locators.submit_ad_button).click()

        driver.get('https://qa-desk.stand.praktikum-services.ru/profile')

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.profile_header))
        )

        # Листаем по страницам объявлений до последней
        max_attempts = 999  # Максимальное количество пролистываний
        found = False
        
        for attempt in range(max_attempts):
            # Дожидаемся загрузки последнего сообщения __на странице__
            ad_card_element = WebDriverWait(driver, 3).until(
                expected_conditions.visibility_of_element_located((By.XPATH, Locators.ad_card))
            )
            
            # Если текст совпадает, то успех
            if ad_card_element.text == dummy_text:
                found = True
                break
                
            # Если текст не совпадает, и это не последняя попытка, то переходим на следующую страницу
            if attempt < max_attempts - 1:
                try:
                    right_button = WebDriverWait(driver, 3).until(
                        expected_conditions.element_to_be_clickable((By.XPATH, Locators.right_button))
                    )
                    right_button.click()
                    # Дожидаемся загрузки блока
                    WebDriverWait(driver, 3).until(
                        expected_conditions.staleness_of(ad_card_element)
                    )
                except:
                    # В случае, если кнопки не существует, или она некликабельна (напр., на последней странице)
                    break
        
        assert found, f"Объявления '{dummy_text}' не найдено после проверки {max_attempts} страниц"

        self.teardown()









