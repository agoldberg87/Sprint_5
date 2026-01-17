import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Initialize the WebDriver
    driver = webdriver.Chrome()
    driver.get("https://qa-desk.stand.praktikum-services.ru/")
    yield driver
    # Teardown - quit the driver after tests
    driver.quit()