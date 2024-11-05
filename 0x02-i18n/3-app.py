#!/usr/bin/env python3
"""basic flask application"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """ Application configuration class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Instantiate the application object
app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ets locale from request object"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Renders a basic html template"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
