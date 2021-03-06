#!flask/bin/python
# -*- encoding: utf-8 -*-
from flask import Flask, jsonify, request
from DatabaseUtils import getlastweeklecture
from DatabaseUtils import searchlecture

app = Flask(__name__)

@app.route('/lecture/lastweek', methods=['GET'])
def get_lastweek_lecture():
    return jsonify(getlastweeklecture())

@app.route('/lecture/search', methods=['GET'])
def search_lecture():
    return  jsonify(searchlecture(request.args.get('keyword')))

@app.route('/')
def index():
    return "hello world"


if __name__ == '__main__':
    app.run(debug=True)
