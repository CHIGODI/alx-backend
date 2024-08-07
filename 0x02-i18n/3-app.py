#!/usr/bin/env python3
"""Task 2: Get locale from request"""

from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """Config class"""
    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


def get_locale() -> str:
    """Retrieves the locale for a web page"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app, locale_selector=get_locale)


@app.route('/')
def index() -> str:
    """default route"""
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run(debug=1)
