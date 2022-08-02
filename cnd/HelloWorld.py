"""HelloWord.py
"""
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        data = {"message":"Hello world"}
        return data

api.add_resource(HelloWorld,"/")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8888, debug=True)
