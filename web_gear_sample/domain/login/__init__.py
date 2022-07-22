"""
Blueprint to login
"""
from flask import Flask
from .login import login_bp


def init_app(app: Flask):
    """
    Blueprints register
    """
    app.register_blueprint(login_bp, url_prefix='/login')
