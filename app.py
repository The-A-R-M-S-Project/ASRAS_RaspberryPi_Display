from flask import Flask, render_template, jsonify
from flask_cors import CORS
from Project.scheduler import main
import time

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/home')
def hello():
    return render_template('hello.html')


@app.route('/')
@app.route('/amortize', methods=['POST', 'GET'])
def algorithm():
    output = main()
    masaka = output.split('&')
    return render_template('hello.html', results=masaka)


def display():
    return render_template('display.html')


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


if __name__ == '__main__':
    app.run()
