"""
Routes for Login
"""
from flask import Blueprint, render_template


login_bp = Blueprint('login', __name__, template_folder='templates')


@login_bp.route('/')
def main_page():
    """
    Render template
    """
    return render_template('login.html')
