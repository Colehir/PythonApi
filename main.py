from flask import request
import json

@app.route('/', methods=['GET'])
def getSnake():
    return "Hello"
