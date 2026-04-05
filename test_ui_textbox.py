# test_ui_textbox.py

import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("UI-тесты")
@allure.story("Авторизация на Sauce Demo")
class TestSauceDemo:

    @allure.title("Успешная авторизация")
    @allure.description("Вводим корректные данные → нажимаем Login → проверяем результат")
    def test_successful_login(self, driver):
        with allure.step("Открыть страницу авторизации"):
            driver.get("https://www.saucedemo.com")

        with allure.step("Заполнить поля логина и пароля"):
            driver.find_element(By.ID, "user-name").send_keys("standard_user")
            driver.find_element(By.ID, "password").send_keys("secret_sauce")

        with allure.step("Нажать кнопку Login"):
            driver.find_element(By.ID, "login-button").click()

        with allure.step("Проверить результат авторизации"):
            wait = WebDriverWait(driver, 10)
            # Проверяем, что появился заголовок страницы товаров
            products_title = wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "title"))
            ).text
            assert "Products" in products_title, f"Заголовок не совпадает: {products_title}"

        # Прикрепляем скриншот к отчёту
        allure.attach(
            driver.get_screenshot_as_png(),
            name="successful_login",
            attachment_type=allure.attachment_type.PNG
        )

    @allure.title("Проверка валидации для заблокированного пользователя")
    @allure.description("Вводим данные заблокированного пользователя → форма не должна пропустить")
    def test_locked_out_user(self, driver):
        with allure.step("Открыть страницу авторизации"):
            driver.get("https://www.saucedemo.com")

        with allure.step("Ввести данные заблокированного пользователя"):
            driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
            driver.find_element(By.ID, "password").send_keys("secret_sauce")

        with allure.step("Нажать кнопку Login"):
            driver.find_element(By.ID, "login-button").click()

        with allure.step("Убедиться, что авторизация НЕ прошла (появилась ошибка)"):
            wait = WebDriverWait(driver, 10)
            error_element = wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
            )
            error_text = error_element.text
            assert "locked out" in error_text.lower(), f"Неожиданное сообщение: {error_text}"

        # Прикрепляем скриншот с ошибкой
        allure.attach(
            driver.get_screenshot_as_png(),
            name="locked_out_error",
            attachment_type=allure.attachment_type.PNG
        )