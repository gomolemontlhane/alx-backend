#!/usr/bin/env python3
"""
5-app.py: A Flask application with Babel for internationalization and mock user login.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _

# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

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

def get_user():
    """
    Retrieves a user from the mock database based on the login_as parameter.

    Returns:
        dict or None: The user dictionary or None if the user is not found.
    """
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit():
        user_id = int(user_id)
        return users.get(user_id)
    return None

@app.before_request
def before_request():
    """Executed before all other functions; sets the user in the global context."""
    g.user = get_user()

@babel.localeselector
def get_locale():
    """
    Determines the best match with the supported languages based on user settings,
    request headers, and URL parameters.

    Returns:
        str: The best match locale.
    """
    # Locale from URL parameters
    locale_param = request.args.get('locale')
    if locale_param in app.config['LANGUAGES']:
        return locale_param

    # Locale from user settings
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')

    # Locale from request headers
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """
    Renders the index page with user login information.

    Returns:
        str: The rendered HTML template.
    """
    return render_template('5-index.html')

if __name__ == '__main__':
    app.run(debug=True)
