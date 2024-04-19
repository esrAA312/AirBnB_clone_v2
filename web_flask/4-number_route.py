#!/usr/bin/python3
"""num
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def Hiesraa():
    """Return string when route queried
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def HB():
    """Return string when route queried
    """
    return 'HBNB'


@app.route('/c/<text>')
def CC(text):
    """Return reformatted text
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>')
def COOL(text='is cool'):
    """Reformat text based on optional variable
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>')
def Na(n):
    return str(n) + ' is a number’


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
