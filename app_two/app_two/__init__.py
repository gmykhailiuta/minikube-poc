"""Flask helloapp
"""
from flask_api import FlaskAPI

app_two = FlaskAPI(__name__)

from app_two import routes
