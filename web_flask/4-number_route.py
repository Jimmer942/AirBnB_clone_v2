#!/usr/bin/python3

"""script that starts a Flask web application"""


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ Hello HBNB """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ HBNB """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def C(text):
    """ C ... """
    return "C " + text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def Python(text='is cool'):
    """ Python ... """
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>')
def number(n):
    """ n is a number"""
    if type(n) is int:
        return str(n) + " is a number"

if __name__ == '__main__':
    app.run()
