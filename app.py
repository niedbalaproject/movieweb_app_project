from flask import Flask
from datamanager.json_data_manager import JSONDataManager


# Create Flask application
app = Flask(__name__)

# Create DataManager instance
data_manager = JSONDataManager('movies.json')


@app.route('/')
def home():
    return "Welcome to MovieWeb App!"


@app.route('/users')
def list_users():
    users = data_manager.get_all_users()
    return str(users)


@app.route('/users/<user_id>')
def user_movies(user_id):
    movies = data_manager.get_user_movies(user_id)
    return f"Movies for user {user_id}: {movies}"


@app.route('/add_user')
def add_user():
    return "Add user page"


@app.route('/users/<user_id>/add_movie')
def add_movie(user_id):
    return f"Add movie for user {user_id}"


@app.route('/users/<user_id>/update_movie/<movie_id>')
def update_movie(user_id, movie_id):
    return f"Update movie {movie_id} for user {user_id}"


@app.route('/users/<user_id>/delete_movie/<movie_id>')
def delete_movie(user_id, movie_id):
    return f"Delete movie {movie_id} for user {user_id}"


if __name__ == '__main__':
    app.run(debug=True)
