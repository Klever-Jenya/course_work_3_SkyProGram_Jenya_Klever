from pathlib import Path

CURRENT_PATH = Path(__file__).resolve().parent  # ТЕКУЩИЙ _ ПУТЬ ... родитель

PATH_POSTS = Path.joinpath(CURRENT_PATH, 'data', 'posts.json')

PATH_COMMENTS = Path.joinpath(CURRENT_PATH, 'data', 'comments.json')

# PATH_POSTS = os.path.join('data', 'posts.json')
# PATH_COMMENTS = os.path.join('data', 'comments.json')
