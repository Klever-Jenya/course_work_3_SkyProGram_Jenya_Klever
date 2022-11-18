class TestPost:
    def test_index(self, test_client):
        response = test_client.get('/posts/1', follow_redirects=True)
        assert response.status_code == 200, 'Не верный статус код от страницы c постом'

    def test_username_post(self, test_client):
        response = test_client.get('/users/larry', follow_redirects=True)
        assert response.status_code == 200, 'Не верный статус код от страницы пользователя'
