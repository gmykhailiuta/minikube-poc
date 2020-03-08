# -*- coding: utf-8 -*-
"""Routes for app
"""

import os
import requests
import json
from app_two import app_two
from flask import abort


@app_two.route('/', methods=['GET'])
def hello_world():
    """
    Hello world response!
    """
    app_one_url = os.getenv("APP_ONE_URL")
    req = requests.get(app_one_url)
    try:
        message = json.loads(req.text)['message']
    except json.ValueErorr as e:
        abort(400, e.message)
    reversed_message = ''.join(reversed(message))
    return {"id": "2", "message": reversed_message}


@app_two.route('/healthcheck', methods=['GET'])
def healthcheck():
    return {}


@app_two.route('/<path:path>')
def catch_all(path):
    return 'Try /'
