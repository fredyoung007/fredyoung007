#!/usr/bin/env python3
"""HelloService.py
"""

from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)
payload ="Hello world"

class HelloService(Resource):
    def get(self):
        return {"message":payload}

api.add_resource(HelloService,"/")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8888, debug=True)
