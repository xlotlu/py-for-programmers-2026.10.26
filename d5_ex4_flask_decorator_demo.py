from flask import Flask # micro-framework web

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/user/<name>")
def user(name):
    return f"<p>Salutare, {name}!</p>"

