import json
import allure
import pytest
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage

fake = Faker()


def load_test_data():
    with open("test_data.json", "r", encoding="utf-8") as f:
        return json.load(f)


@allure.feature("Авторизация")
class TestParametrized:

    @allure.story("Параметризованный тест из JSON")
    @pytest.mark.parametrize("data", load_test_data())
    def test_login_with_json_data(self, driver, data):

        login_page = LoginPage(driver)
        login_page.open_page()
        login_page.login(data["username"], data["password"])

        if data["expected"] == "success":
            assert "inventory.html" in driver.current_url, \
                f"Не удалось войти с {data['username']}"
        else:
            assert "inventory.html" not in driver.current_url, \
                f"Заблокированный пользователь {data['username']} смог войти"

            error_element = login_page.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
            )
            assert "locked out" in error_element.text.lower()

    @allure.story("Генерация случайных данных через Faker")
    def test_login_with_faker(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page()

        random_username = fake.user_name()
        random_password = fake.password()

        login_page.login(random_username, random_password)

        error_element = login_page.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
        )

        assert "Username and password do not match" in error_element.text