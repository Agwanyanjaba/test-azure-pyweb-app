from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Wycliffe Hello World!"

@app.route('/msg')
def hello():
    return "Wycliffe Hello World!"