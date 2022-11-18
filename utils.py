import json

from paths import PATH_POSTS, PATH_COMMENTS


class Post:

    def __init__(self):
        self.query = None
        self.username = None
        self.pk = None

    def get_posts_all(self):  # + возвращает посты
        with open(PATH_POSTS, "r", encoding="utf-8") as file:
            return json.load(file)

    def get_posts_by_user(self, username):  # + возвращает посты определенного пользователя.
        self.username = username
        posts_username = []
        posts = self.get_posts_all()
        for post in posts:
            if post["poster_name"] == username:
                posts_username.append(post)
        if len(posts_username) == 0:
            raise ValueError("У пользователя нет постов")
        return posts_username

    def get_post_by_pk(self, pk):  # + возвращает один пост по его идентификатору.
        self.pk = pk
        if type(pk) != int: raise TypeError("Должно быть целое число от 1 до 8")
        if pk < 1 or pk > 8: raise ValueError("Должно быть от 1 до 8")
        posts = self.get_posts_all()
        for post in posts:
            if post["pk"] == pk:
                return post

    def search_for_posts(self, query):  # + возвращает список постов по ключевому слову
        self.query = query
        query_posts = []
        posts = self.get_posts_all()
        for post in posts:
            if query in post["content"]:
                query_posts.append(post)
        return query_posts


class Comment:

    def __init__(self):
        self.post_id = None

    def get_all_comments(self):  # + возвращает все комментарии
        with open(PATH_COMMENTS, "r", encoding="utf-8") as file:
            return json.load(file)

    def get_comments_by_post_id(self, post_id):  # + возвращает комментарии определенного поста.
        self.post_id = post_id
        comments_by_id = []
        comments = self.get_all_comments()
        for comment in comments:
            if comment["post_id"] == post_id:
                comments_by_id.append(comment)
        if len(comments) == 0:
            raise ValueError("Нет комментариев к посту")
        return comments_by_id


class Tag(Post):

    def pull_tag_from_content(self, content):  # + в контенте находит все #хештеги, выводит список хештегов
        tags = []
        text = content.replace(", ", " ")
        text = content.replace(": ", " ")
        text = content.replace(". ", " ")
        text = content.replace("! ", " ")
        words = text.split(" ")
        for word in words:
            if word.lower().startswith("#"):
                tags.append(word[1:])
        return tags

    def find_tag(self, tag):  # находит посты по тегу
        posts = self.get_posts_all()
        posts_tag = []
        for post in posts:
            tags = self.pull_tag_from_content(post["content"])
            if tag in tags:
                posts_tag.append(post)
                return posts_tag
