#!/usr/bin/python3

from flask import Flask
from flask_cors import CORS

__author__ = 'Ruoduan'


def create_app():
    app = Flask(__name__)
    register_blueprint(app)
    CORS(app)
    return app


def register_blueprint(app):
    from ..test.views import test_blue
    app.register_blueprint(test_blue)
