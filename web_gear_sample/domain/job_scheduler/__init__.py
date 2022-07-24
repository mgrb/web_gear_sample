"""
Job Scheduler Blueprint register
"""
from flask import Flask
from .job_scheduler import job_scheduler_bp


def init_app(app: Flask):
    """
    Blueprint register
    """
    app.register_blueprint(job_scheduler_bp, url_prefix='/scheduler')
