# -*- coding: utf-8 -*-
"""Routes for app
"""

from app_one import app_one


@app_one.route('/', methods=['GET'])
def hello_world():
    """
    Hello world response!
    """
    return {"id": "1", "message": "Hello world"}


@app_one.route('/healthcheck', methods=['GET'])
def healthcheck():
    return {}


@app_one.route('/<path:path>')
def catch_all(path):
    return 'Try /'
