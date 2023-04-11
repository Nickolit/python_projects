import pytest
import requests
import allure


with open('_internal_links.txt', 'r') as f:
    internal_urls = f.read().splitlines()


@allure.feature('Check url')
@allure.story('Запрашиваем статус-код ссылки')
@pytest.mark.parametrize("internal_url", internal_urls)
def test_getting_posts(internal_url):
    response = requests.get(internal_url)

    with allure.step("Запрос отправлен. Сверяем ответ url на статус-код 200"):
        assert response.status_code == 200, "Полученное количество элементов не соответствует ожидаемому"
