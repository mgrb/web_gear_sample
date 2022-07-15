"""
Modulo initializer
"""
from logging import info

from flask import Flask, render_template
from web_gear_sample.ext import site

__version__ = '0.1.0'


def create_app():
    """
    App builder
    """
    info('Building webApp...')
    app = Flask(__name__)
    site.init_app(app)
    return app


if __name__ == "__main__":
    local_app = create_app()
    local_app.run(host='0.0.0.0', debug=True)
