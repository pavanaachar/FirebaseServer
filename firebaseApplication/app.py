from firebaseApplication import app
from firebaseApplication import serverApp
from flask import request
import json


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/send', methods=['POST'])
def publish():
    if not request.json:
        return "No data"
    data = request.json
    msg = data['data']
    result = serverApp.publish_andr(data=msg)
    return result
