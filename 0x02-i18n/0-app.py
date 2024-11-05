#!/usr/bin/env python3
"""
0-app.py: A simple Flask application that renders an HTML page.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index() -> str:
    """
    Renders the index page with a welcome message.

    Returns:
        str: The rendered HTML template.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
