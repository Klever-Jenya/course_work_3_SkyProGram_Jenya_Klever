import logging
from json import JSONDecodeError

from flask import Flask, request, render_template, jsonify
from werkzeug.exceptions import NotFound

from utils import Post, Comment, Tag

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
# app.json.ensure_ascii
app.config["JSON_AS_ASCII"] = False

post_class = Post()
comment_class = Comment()
tag_class = Tag()


@app.route("/")
def index():
    try:
        posts = post_class.get_posts_all()  # + возвращает посты
    except (FileNotFoundError, JSONDecodeError):
        return "Сервис не доступен", 503
    logging.info("Главная страница всех постов запрошена")
    return render_template("index.html", posts=posts)


@app.route("/posts/<int:post_id>")
def get_post(post_id):
    post = post_class.get_post_by_pk(post_id)  # + (словарь) возвращает пост по pk.
    comments = comment_class.get_comments_by_post_id(post_id)
    # + (список словарей) возвращает комментарии определенного поста.
    count = len(comments)
    logging.info("Страница одного поста запрошена")
    return render_template("post.html",
                           post=post,
                           comments=comments,
                           count=count
                           )


@app.route("/search/")
def search_post():
    word = request.args.get("s").lower()
    # pull_tag_from_content(content): # в контенте находит все #хештеги, выводит список хештегов
    posts_by_query = post_class.search_for_posts(word)
    # (query-запрос) + возвращает (список словарей) постов по ключевому слову
    logging.info("Страница запроса запрошена")
    return render_template("search.html",
                           word=word,
                           posts_by_query=posts_by_query,
                           )


@app.route("/users/<username>")
def username_post(username):
    posts_by_username = post_class.get_posts_by_user(username)  # + возвращает посты определенного пользователя.
    count = len(posts_by_username)
    logging.info("Страница одного пользователя запрошена")
    return render_template("user-feed.html",
                           posts_by_username=posts_by_username,
                           count=count
                           )


@app.route("/api/posts")
def api_index():
    logging.info("Страница JSON всех постов запрошена")
    return jsonify(post_class.get_posts_all())


@app.route("/api/posts/<int:pk>")
def api_get_post(pk):
    logging.info("Страница JSON одного поста запрошена")
    return jsonify(post_class.get_post_by_pk(pk))


# @app.route("/tag/<tag>")
# def tag_page(tag):
#     """ - Страница тегов"""
#     posts = post_class.get_posts_all()  # + возвращает посты
#     posts_tag = tag_class.find_tag(tag)  # (словарь) находит пост по тегу
#     return render_template("tag.html", posts=posts, posts_tag=posts_tag, tag=tag)

@app.errorhandler(NotFound)
def error_404(e):
    return "Такой страницы нет", 404


app.run()
