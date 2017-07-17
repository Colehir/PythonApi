from flask import request
from flask import Flask
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def getSnake():
    return json.dumps({ "x": 1 })

@app.route('/help', methods=['GET'])
def getHelp():
    return json.dumps({ "x": 1 })

if __name__ == "__main__":
    print("starting")
    app.run()
