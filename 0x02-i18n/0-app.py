#!/usr/bin/env python3
"""Basic flask app"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """Renders simple html page"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
