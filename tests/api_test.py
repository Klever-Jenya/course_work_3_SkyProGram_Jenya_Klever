# Протестируйте эндпоинт `GET /api/posts` , проверьте, что
# - возвращается список
# - у элементов есть нужные ключи
def test_api_get_posts_all(test_client):
    response = test_client.get('/api/posts', follow_redirects=True)

    assert response.status_code == 200
    assert type(response.json) == list
    assert {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}.issubset(set(response.json[0].keys()))


# Протестируйте эндпоинт `GET /api/posts/<post_id>` , проверьте, что
# - возвращается словарь
# - у элемента есть нужные ключи
def test_get_posts_all(test_client):
    response = test_client.get('/api/posts/1', follow_redirects=True)

    assert response.status_code == 200
    assert type(response.json) == dict
    assert {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}.issubset(set(response.json.keys()))

