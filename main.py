from flask import request
import json

@app.route('/', methods=['GET'])
def getSnake():
    return json.dump({ x: 1 })

@app.route('/help', methods=['GET'])
def getHelp():
    return json.dump({ x: 1 })
