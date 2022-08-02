"""hello.py
"""
#! /usr/bin/evn python

from flask import Flask

app = Flask(__name__)

message = "Hello world"

@app.route("/")
def hello():
    return message

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8888, debug=True)
