"""
Blueprint to base web app interface
"""
from flask import Flask
from .bp_index import bp


def init_app(app: Flask):
    """
    Blueprints register
    """
    app.register_blueprint(bp)
