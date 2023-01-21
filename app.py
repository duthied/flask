# app.py

from flask import Flask, jsonify, request

app = Flask(__name__)

movies = [
    {
        "name": "The Shawshank Redemption",
        "cast": ["Tim Robbins", "Morgan Freeman", "Bob Gunton"],
        "genres": ["Drama"]
    },
    {
        "name": "The Godfather",
        "cast": ["Marlon Brando", "Al Pacino", "James Caan"],
        "genres": ["Crime", "Drama"]
    },
    {
        "name": "The Dark Knight",
        "cast": ["Christian Bale", "Heath Ledger", "Aaron Eckhart"],
        "genres": ["Action", "Crime", "Drama"]
    },
    {
        "name": "Pulp Fiction",
        "cast": ["John Travolta", "Samuel L. Jackson", "Uma Thurman"],
        "genres": ["Crime", "Drama"]
    },
    {
        "name": "The Lord of the Rings: The Return of the King",
        "cast": ["Elijah Wood", "Viggo Mortensen", "Ian McKellen"],
        "genres": ["Adventure", "Drama", "Fantasy"]
    }
]

@app.route('/movies', methods=['GET'])
def hello():
    return jsonify(movies)

@app.route('/movies', methods=['POST'])
def add_movie():
    movie = request.get_json()
    movies.append(movie)
    return {'id': len(movies)}, 200

@app.route('/movies/<int:index>', methods=['PUT'])
def update_movies(index):
    movie = request.get_json()
    movies[index] = movie
    return jsonify(movies[index]), 200

@app.route('/movies/<int:index>', methods=['DELETE'])
def delete_movie(index):
    movies.pop(index)
    return 'None', 200

app.run(host="localhost", port=8080, debug=True)