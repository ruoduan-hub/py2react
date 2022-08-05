#!/usr/bin/python3

from flask import Blueprint

test_blue = Blueprint('test_blue', __name__, url_prefix='/test')

