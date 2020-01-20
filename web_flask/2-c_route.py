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
def hello_c(text):
    """ C ... """
    return "C " + text

if __name__ == '__main__':
    app.run()
