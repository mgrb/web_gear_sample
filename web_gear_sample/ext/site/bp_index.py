from flask import Blueprint, render_template


bp = Blueprint('web_gear', __name__)


@bp.route('/')
def landing_page():
    """
    Render template
    """
    return render_template('index.html')
