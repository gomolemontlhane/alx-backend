#!/usr/bin/env python3
"""
4-app.py: A Flask application with Babel for internationalization with URL parameter support.
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
    Also checks for a locale parameter in the URL.

    Returns:
        str: The best match locale.
    """
    # Get the locale from URL parameters
    locale_param = request.args.get('locale')
    if locale_param in app.config['LANGUAGES']:
        return locale_param
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index() -> str:
    """
    Renders the index page with a welcome message.

    Returns:
        str: The rendered HTML template.
    """
    return render_template('4-index.html')

if __name__ == '__main__':
    app.run(debug=True)
