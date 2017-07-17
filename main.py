from flask import request
from flask import Flask
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def getSnake():
    return json.dumps({ "x": 1 })

if __name__ == "__main__":
    app.run()
