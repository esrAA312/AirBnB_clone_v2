#!/usr/bin/python3
"""
Start Flask application
"""

from flask import Flask

app = Flask(__name__)


def Hiesraa:
    """Returns Hello HBNB!"""
    return 'Hello HBNB!'


def HB():
    """Returns HBNB"""
    return 'HBNB'


def CC(text):
    """Display “C ” followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')

# Routes


app.add_url_rule('/', 'index', Hiesraa)
app.add_url_rule('/hbnb', 'hbnb', HB)
app.add_url_rule('/c/<text>', 'c', CC)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
