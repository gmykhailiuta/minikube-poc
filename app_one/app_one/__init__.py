"""Flask helloapp
"""
from flask_api import FlaskAPI

app_one = FlaskAPI(__name__)

from app_one import routes
