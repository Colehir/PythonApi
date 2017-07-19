import os
from flask import request
from flask import Flask
import json

app = Flask(__name__)

class Snake:
    def __init__(self):
        self.list = []
        self.food = {}

snake = Snake()

@app.route('/', methods=['GET'])
def get():
    result = ''
    for obj in snake.list:
        result += str(obj["x"])
    return result, 200

@app.route('/snake', methods=['GET'])
def getSnake():
    return json.dumps(snake.list)

@app.route('/food', methods=['GET'])
def getFood():
    return json.dumps(snake.food)

@app.route('/snake', methods=['POST'])
def updateSnake():
    newList = request.json['list']
    snake.list = newList
    return '', 200

@app.route('/food', methods=['POST'])
def updateFood():
    newFood = request.json['food']
    snake.food = newFood
    return '', 200

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    print("starting")
    app.run()
    #app.run(host = '0.0.0.0', port = int(port))
