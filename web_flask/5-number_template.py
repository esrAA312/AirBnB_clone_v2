#!/usr/bin/python3
"""This is a script that starts a Flask web application"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Hiesraa():
    """Display Hello HBNB!"""
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def HB():
    """Display HBNB"""
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def CC(text):
    """Display C followed by the value of the text variable"""
    t = text.replace('_', ' ')
    return 'C ' + t


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def COOL(text='is cool'):
    """display Python followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')


@app.route("/number/<int:n>", strict_slashes=False)
def NA(n):
    """display n is a number"""
    return f'{n} is a number'


@app.route("/number_template/<int:n>", strict_slashes=False)
def nue(n):
    """This is a function to deploy the jinja template"""
    return render_template("5-number.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
