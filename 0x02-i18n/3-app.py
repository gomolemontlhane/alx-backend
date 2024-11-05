#!/usr/bin/env python3
"""
3-app.py: A Flask application with Babel for internationalization using parameterized templates.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _

class Config:
    """Configuration class for Flask-Babel."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

# Initialize the Flask application
app = Flask(__name__)
app.config.from_object(Config)

# Initialize Babel
babel = Babel(app)

@babel.localeselector
def get_locale() -> str:
    """
    Determines the best match with the supported languages based on the request's accept languages.

    Returns:
        str: The best match locale.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index() -> str:
    """
    Renders the index page with a welcome message.

    Returns:
        str: The rendered HTML template.
    """
    return render_template('3-index.html')

if __name__ == '__main__':
    app.run(debug=True)
