"""
Blueprint to base web app interface
"""
import flask

from .bp_index import bp


def init_app(app: flask):
    """
    Blueprints register
    """
    app.register_blueprint(bp)
