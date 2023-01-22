# app.py

from flask import Flask, jsonify, request

app = Flask(__name__)

import connexion

app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml")

@app.route('/', methods=['GET'])
def hello():
    return jsonify("'hello': 'yo'")

# @app.route('/movies', methods=['POST'])
# def add_movie():
#     movie = request.get_json()
#     movies.append(movie)
#     return {'id': len(movies)}, 200

# @app.route('/movies/<int:index>', methods=['PUT'])
# def update_movies(index):
#     movie = request.get_json()
#     movies[index] = movie
#     return jsonify(movies[index]), 200

# @app.route('/movies/<int:index>', methods=['DELETE'])
# def delete_movie(index):
#     movies.pop(index)
#     return 'None', 200

app.run(host="localhost", port=8080, debug=True)