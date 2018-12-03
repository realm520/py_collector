# -*- coding: utf-8 -*-  

from flask import Flask
from flask import Flask
from flask_jsonrpc import JSONRPC

app = Flask(__name__)
jsonrpc = JSONRPC(app, '/api')

@app.route('/')
def hello_world():
    return 'Hello World!'

@jsonrpc.method('App.index')
def index():
    return u'Welcome to Flask JSON-RPC'

if __name__ == '__main__':
    app.run()