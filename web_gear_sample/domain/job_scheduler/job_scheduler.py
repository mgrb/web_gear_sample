"""
Job Scheduler
"""
from flask import Blueprint, render_template


job_scheduler_bp = Blueprint('job_scheduler', __name__, template_folder='templates')

@job_scheduler_bp.route('/')
def main_page():
    """
    Main page of module
    """
    return render_template('job_manager.html.j2')
