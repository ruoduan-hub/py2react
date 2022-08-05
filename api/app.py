#!/usr/bin/python3

# from flask import Flask, request, render_template, url_for, redirect
from flask import Flask, request, redirect, Response

from src.config import create_app

app = create_app()


# @app.route('/', methods=['GET'])
# def page():
#     return render_template('index.html')


@app.route('/hello', methods=['GET'])
def hello():
    return {'title': 'Hello Word ！',
            'info': ' This a Flask and  app ! <br> language： Api use Python; Front use Typescript  '}


@app.route('/mgtest.gif', methods=['GET'])
def gif_md():
    """
    GIF埋点
    返回GIF图片，获取埋点数据，
    :return: file -> image/gif
    """
    print('埋点数据：%s 时间戳：%s' % (request.args['data'], request.args['now']))
    with open('./assets/11.gif', 'rb') as f:
        img = f.read()
    return Response(img, mimetype='image/gif')


if __name__ == '__main__':
    app.run()
