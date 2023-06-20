import flask
from flask import request, jsonify
import json

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "This works great"

@app.route('/student', methods=['GET'])
def student():
    student={
        "name":"Raj",
        "age":20,
        "college":"NIT",
        "address":"Test",
        "marks":[90,80,70,60]
    }
    return jsonify(student)


app.run('127.0.0.1',4005,debug=True)