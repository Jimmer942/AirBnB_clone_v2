#!/usr/bin/python3

"""script that starts a Flask web application"""


from flask import Flask
from flask import render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ n is a number"""
    if type(n) is int:
        return str(n) + " is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ template """
    if type(n) is int:
        return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_type(n):
    """ Even or odd """
    t = ''
    if type(n) is int:
        if n % 2 == 0:
            t = 'even'
        else:
            t = 'odd'
        return render_template('6-number_odd_or_even.html', number=n, numbertype=t)

if __name__ == '__main__':
    app.run()
