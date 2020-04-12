#coding=utf-8

import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello World!'

@app.route('/')
def index():
    return render_template('test.html')


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)