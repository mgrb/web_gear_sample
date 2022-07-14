"""
Entry point for the web app.
"""
from flask import Flask
from logging import info


def create_app():
    """
    App builder
    """
    info('Building webApp...')
    app = Flask(__name__)

    @app.route('/')
    def landing_page():
        return 'Hello'

    return app
