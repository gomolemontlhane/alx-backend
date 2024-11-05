#!/usr/bin/env python3
"""
1-app.py: A Flask application with Babel for internationalization.
"""

from flask import Flask, render_template
from flask_babel import Babel

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

@app.route('/')
def index() -> str:
    """
    Renders the index page with a welcome message.

    Returns:
        str: The rendered HTML template.
    """
    return render_template('1-index.html')

if __name__ == '__main__':
    app.run(debug=True)
