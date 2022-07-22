"""
Routes for Dashboard
"""
from flask import Blueprint, render_template


dashboard_bp = Blueprint('dashboard', __name__, template_folder='templates')


@dashboard_bp.route('/')
def main_page():
    """
    Render template
    """
    return render_template('dashboard.html')
