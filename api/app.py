#!/usr/bin/python3

# from flask import Flask, request, render_template, url_for, redirect
from flask import Flask, request, redirect
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# @app.route('/', methods=['GET'])
# def page():
#     return render_template('index.html')

@app.route('/hello', methods=['GET'])
def hello():
    return { 'title': 'Hello Word ！', 'info': ' This a Flask and  app ! <br> language： Api use Python; Front use Typescript  ' }

@app.route('/mgtest.gif', methods=['GET'])
def mdFunc():
  print(request.args['name'])
  return redirect('https://sm.ms/image/W4yvPm5CFA3hMcX')

if __name__ == '__main__':
    app.run(debug=True)
