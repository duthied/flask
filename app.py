# app.py

from flask import Flask, jsonify, request

app = Flask(__name__)

import connexion

app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml")

@app.route('/', methods=['GET'])
def hello():
    return jsonify("'hello': 'yo'")

app.run(host="localhost", port=8080, debug=True)