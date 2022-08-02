#!/usr/bin/env python3
"""hello.py
"""

import requests
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    message = requests.get("http://127.0.0.1:8888").json()["message"]
    return "<h1 style=background-color:powderblue;>" + message + "</h1>"
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
