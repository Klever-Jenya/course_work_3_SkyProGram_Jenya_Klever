import json

from paths import PATH_POSTS, PATH_COMMENTS


# + возвращает посты
def get_posts_all():
    with open(PATH_POSTS, "r", encoding="utf-8") as file:
        return json.load(file)


# + возвращает посты определенного пользователя.
def get_posts_by_user(username):
    posts_username = []
    posts = get_posts_all()
    for post in posts:
        if post["poster_name"] == username:
            posts_username.append(post)
    if len(posts_username) == 0:
        raise ValueError("У пользователя нет постов")
    return posts_username


# + возвращает все комментарии
def get_all_comments():
    with open(PATH_COMMENTS, "r", encoding="utf-8") as file:
        return json.load(file)


# + возвращает один пост по его идентификатору.
def get_post_by_pk(pk):
    if type(pk) != int: raise TypeError("Должно быть целое число от 1 до 8")
    if pk < 1 or pk > 8: raise ValueError("Должно быть от 1 до 8")
    posts = get_posts_all()
    for post in posts:
        if post["pk"] == pk:
            return post


# + возвращает комментарии определенного поста.
def get_comments_by_post_id(post_id):
    comments_by_id = []
    comments = get_all_comments()
    for comment in comments:
        if comment["post_id"] == post_id:
            comments_by_id.append(comment)
    if len(comments) == 0:
        raise ValueError("Нет комментариев к посту")
    return comments_by_id


# + возвращает список постов по ключевому слову
def search_for_posts(query):  # query-запрос
    query_posts = []
    posts = get_posts_all()
    for post in posts:
        if query in post["content"]:
            query_posts.append(post)
    return query_posts

# # + в контенте находит все #хештеги, выводит список хештегов
# def pull_tag_from_content(content):
#     tags = []
#     text = content.replace(", ", " ")
#     text = content.replace(": ", " ")
#     text = content.replace(". ", " ")
#     text = content.replace("! ", " ")
#     words = text.split(" ")
#     for word in words:
#         if word.lower().startswith("#"):
#             tags.append(word[1:])
#     return tags
#
#
# # находит посты по тегу
# def find_tag(tag):
#     posts = get_posts_all()
#     posts_tag = []
#     for post in posts:
#         tags = pull_tag_from_content(post["content"])
#         if tag in tags:
#             posts_tag.append(post)
#             return posts_tag
