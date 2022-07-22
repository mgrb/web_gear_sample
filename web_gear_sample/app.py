"""
App main module
"""
from logging import info

from flask import Flask
from web_gear_sample.ext import configuration


def minimal_app(**config):
    """
    App minimal bulder
    """
    info('Building webApp...')
    app = Flask(__name__,static_url_path='/static')
    configuration.init_app(app, **config)
    # site.init_app(app)
    return app


def create_app(**config):
    """
    App builder
    """
    app = minimal_app(**config)
    # site.init_app(app)
    configuration.load_extensions(app)
    return app


if __name__ == "__main__":
    local_app = create_app()
    local_app.run(host='0.0.0.0', debug=True)
