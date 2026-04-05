# test_api_posts.py
import allure
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

@allure.feature("API-тесты")
@allure.story("Работа с постами")
class TestPostsAPI:

    @allure.title("Создание нового поста")
    @allure.description("Отправляем POST-запрос → проверяем ответ")
    def test_create_post(self):
        payload = {
            "title": "Лабораторная работа СПО",
            "body": "Тестирование с Allure Report",
            "userId": 10
        }

        with allure.step("Отправить POST-запрос"):
            response = requests.post(f"{BASE_URL}/posts", json=payload)

        with allure.step("Проверить статус и данные"):
            assert response.status_code == 201, f"Статус: {response.status_code}"
            data = response.json()
            assert data["title"] == payload["title"]
            assert data["userId"] == 10

        allure.attach(
            str(payload), name="Request body", attachment_type=allure.attachment_type.TEXT
        )
        allure.attach(
            response.text, name="Response body", attachment_type=allure.attachment_type.JSON
        )

    @allure.title("Получение поста по ID=1")
    @allure.description("GET-запрос к /posts/1")
    def test_get_post(self):
        with allure.step("Отправить GET-запрос"):
            response = requests.get(f"{BASE_URL}/posts/1")

        with allure.step("Проверить ответ"):
            assert response.status_code == 200
            data = response.json()
            assert data["id"] == 1
            assert "sunt aut facere" in data["title"]