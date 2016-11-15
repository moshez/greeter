import functools

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Live from ClusterHQ, It's Tuesday Night Live!"

run = functools.partial(app.run, port=80, host='0.0.0.0')
