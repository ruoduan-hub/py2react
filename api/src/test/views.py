#!/usr/bin/python3
from . import test_blue


@test_blue.route('/get_info')
def get_info():
    return {
        'data': 'my name is flask '
    }


@test_blue.route('/get_info_two')
def get_info_two():
    return {
        'data': 'get_info_two2222 '
    }
