# -*- coding: utf-8 -*-  

from flask import Flask
from flask import Flask
from flask_jsonrpc import JSONRPC

app = Flask(__name__)
jsonrpc = JSONRPC(app, '/api')

@app.route('/')
def hello_world():
    return 'Hello World!'

@jsonrpc.method('hx.asset.summary')
def assetSummary():
    return [{'name': 'HX', 'amount': 100, 'status': 'normal'}, {'name': 'HC', 'amount': 1000, 'status': 'normal'}, {'name': 'BTC', 'amount': 10000, 'status': 'normal'}]

if __name__ == '__main__':
    app.run(debug=True)