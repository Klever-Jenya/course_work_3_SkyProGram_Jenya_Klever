import pytest

from utils import Post, Comment, Tag

post_class = Post()
comment_class = Comment()
tag_class = Tag()

# возвращает один пост по его идентификатору.
pk_parameters = [(1, 1)]


@pytest.mark.parametrize("pk_int, pk_int_", pk_parameters)
def test_get_post_by_pk(open_mock, pk_int, pk_int_):
    assert post_class.get_post_by_pk(pk_int)["pk"] == pk_int_


# error_parameters = [(0, ValueError, open_mock), (2, ValueError, open_mock), ("6", TypeError, open_mock), (6.0, TypeError, open_mock)]
#
#
# @pytest.mark.parametrize("pk, error, mock", error_parameters)
# def test_get_post_by_pk_type_error(pk, error, mock):
#     with pytest.raises(error):
#         get_post_by_pk(pk)

def test_get_post_by_pk_value_error_0(open_mock):
    with pytest.raises(ValueError):
        post_class.get_post_by_pk(0)
    with pytest.raises(ValueError):
        post_class.get_post_by_pk(9)
    with pytest.raises(TypeError):
        post_class.get_post_by_pk("6")
    with pytest.raises(TypeError):
        post_class.get_post_by_pk(6.0)


# def test_pull_tag_from_content(content):  # + в контенте находит все #хештеги, выводит список хештегов
#     assert pull_tag_from_content(content) ==

#
# def test_find_tag(tag): # находит посты по тегу
#     assert find_tag(tag) ==


# отрефакторить

class TestPost:

    def test_get_posts_all(self, open_mock):  # + возвращает посты
        assert type(post_class.get_posts_all()) == list, "возвращается не список"
        assert post_class.get_posts_all()[0]["poster_name"] == "leo", "Неверное имя пользователя"

    def test_get_posts_by_user(self, open_mock):  # + возвращает посты определенного пользователя.
        assert type(post_class.get_posts_by_user("leo")) == list, "возвращается не список"
        with pytest.raises(ValueError):
            post_class.get_posts_by_user("jane"), "Неверное имя пользователя"

    def test_search_for_posts(self, open_mock):  # + (список словарей) возвращает список постов по ключевому слову
        assert type(post_class.search_for_posts("вышел")) == list, "возвращается не список"

    def test_get_post_by_pk_value_error_0(self, open_mock):
        with pytest.raises(ValueError):
            post_class.get_post_by_pk(0)
        with pytest.raises(ValueError):
            post_class.get_post_by_pk(9)
        with pytest.raises(TypeError):
            post_class.get_post_by_pk("6")
        with pytest.raises(TypeError):
            post_class.get_post_by_pk(6.0)

    # возвращает один пост по его идентификатору.
    pk_parameters = [(1, 1)]

    @pytest.mark.parametrize("pk_int, pk_int_", pk_parameters)
    def test_get_post_by_pk(self, open_mock, pk_int, pk_int_):
        assert post_class.get_post_by_pk(pk_int)["pk"] == pk_int_


class TestComment:
    def test_get_all_comments(self, open_mock):  # + возвращает все комментарии
        assert comment_class.get_all_comments()[0]["poster_name"] == "leo", "Неверное имя пользователя"
        assert type(comment_class.get_all_comments()) == list, "Возвращается не список"

    def test_get_comments_by_post_id(self,open_mock_2):
        # + (список словарей) возвращает комментарии определенного поста.
        assert type(comment_class.get_comments_by_post_id(5)) == list, "возвращается не список"
        assert comment_class.get_comments_by_post_id(5)[0]["post_id"] == 5, "Неверный id поста пользователя"
