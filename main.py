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

@app.route('/food', methods=['POST'])
def updateFood():
    newFood = request.json['food']
    snake.food = newFood

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    print("starting")
    app.run(host='0.0.0.0', port=int(port))
