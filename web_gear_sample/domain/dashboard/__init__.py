"""
Blueprint to base web app interface
"""
from flask import Flask
from .dashboard import dashboard_bp


def init_app(app: Flask):
    """
    Blueprints register
    """
    app.register_blueprint(dashboard_bp)
