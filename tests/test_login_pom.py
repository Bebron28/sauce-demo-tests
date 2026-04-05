import allure
from pages.login_page import LoginPage

@allure.feature("Авторизация")
class TestLogin:

    @allure.story("Успешный вход")
    def test_successful_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page()
        login_page.login("standard_user", "secret_sauce")

        assert "inventory.html" in driver.current_url