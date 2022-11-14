# Добавьте обработчик запросов к несуществующим страницам,
# например `/meow` и верните в этом случае статус-код 404.
#
# Добавьте обработчик ошибок, возникших на стороне сервера
# (ошибка 500, Internal Server Error )
# и верните в этом случае статус-код 500.

class TestPost:
    def test_index(self, test_client):
        response = test_client.get('/posts/1', follow_redirects=True)
        assert response.status_code == 200, 'Не верный статус код от страницы c постом'

    def test_username_post(self, test_client):
        response = test_client.get('/users/larry', follow_redirects=True)
        assert response.status_code == 200, 'Не верный статус код от страницы пользователя'


