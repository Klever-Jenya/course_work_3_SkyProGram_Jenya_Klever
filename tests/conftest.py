import json
from unittest.mock import patch, mock_open

import pytest

from main import app


@pytest.fixture()
def test_client():
    app.config["JSON_AS_ASCII"] = False
    return app.test_client()


@pytest.fixture()
def open_mock():  # исправить, встроенная команда, , заплатка
    with patch("builtins.open",
               new_callable=mock_open,
               read_data=json.dumps([{
                   "poster_name": "leo",
                   "poster_avatar": "https://randus.org/avatars/w/c1819dbdffffff18.png",
                   "pic": "https://images.unsplash.com/photo-152535132",
                   "content": "Ага, опять еда! ",
                   "views_count": 376,
                   "likes_count": 154,
                   "pk": 1}, ])) as mock:
        yield mock


@pytest.fixture()
def open_mock_2():  # исправить, встроенная команда, , заплатка
    with patch("builtins.open",
               new_callable=mock_open,
               read_data=json.dumps([{
                   "post_id": 5,
                   "commenter_name": "johnny",
                   "comment": "Давно тебя тут не было, с возвращением!",
                   "pk": 17}, ])) as mock:
        yield mock
