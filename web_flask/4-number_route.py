#!/usr/bin/python3
"""num  that starts a Flask web application"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Hiesraa():
    """This method is to display a welcome message from
    the page that is hosted"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HB():
    """This is a function to display the school name when
    sepcifying the route /hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def CC(text):
    """A method to display “C ” followed by the value of
    the text variable"""
    text = text.replace("_", " ")
    return 'C ' + text


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def COOL(text='is cool'):
    """A method to display “python” followed by the value
    of the text variable"""
    text = text.replace("_", " ")
    return 'Python ' + text


@app.route("/number/<int:n>", strict_slashes=False)
def NA(n):
    """This is script that starts a Flask web application with numbers"""
        return str(n) + ' is a number’

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
