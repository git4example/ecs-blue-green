#!/usr/bin/env python

import os

from flask import Flask, request
from flask_json import as_json

application = Flask(__name__)

VER = os.getenv('APP_VER', 'default')

@application.route('/')
@as_json
def hello():
    name = request.args.get("name", "World")
    VER = os.getenv('APP_VER', 'beta')
    return 'Hello, {}! APP_VERr={}'.format(name, VER)

if __name__ == '__main__':
    PORT = os.getenv('APP_PORT', 80)
    application.run(host='0.0.0.0', port=PORT)
