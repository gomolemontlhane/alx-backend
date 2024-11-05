#!/usr/bin/env python3
"""
7-app.py: A Flask application with Babel for internationalization and timezone selection.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import pytz
from pytz.exceptions import UnknownTimeZoneError

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
    """Retrieve a user based on the login_as parameter."""
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit():
        user_id = int(user_id)
        return users.get(user_id)
    return None

@app.before_request
def before_request():
    """Set the user in the global context."""
    g.user = get_user()

@babel.localeselector
def get_locale():
    """
    Determine the best match with the supported languages based on user settings,
    request headers, and URL parameters.

    Returns:
        str: The best match locale.
    """
    locale_param = request.args.get('locale')
    if locale_param in app.config['LANGUAGES']:
        return locale_param

    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')

    return request.accept_languages.best_match(app.config['LANGUAGES'])

@babel.timezoneselector
def get_timezone():
    """
    Determine the best match for timezone based on user settings, URL parameters,
    and default to UTC if necessary.

    Returns:
        str: The best match timezone.
    """
    # Check for timezone in URL parameters
    timezone_param = request.args.get('timezone')
    if timezone_param:
        try:
            return pytz.timezone(timezone_param).zone
        except UnknownTimeZoneError:
            pass

    # Check for timezone in user settings
    if g.user and g.user.get('timezone'):
        try:
            return pytz.timezone(g.user['timezone']).zone
        except UnknownTimeZoneError:
            pass

    # Default to UTC
    return app.config['BABEL_DEFAULT_TIMEZONE']

@app.route('/')
def index():
    """Render the index page with user login information and timezone support."""
    return render_template('7-index.html')

if __name__ == '__main__':
    app.run(debug=True)
