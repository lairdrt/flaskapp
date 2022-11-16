from flask import render_template, request
from flask_wtf.csrf import CSRFError
from app import db_session
from app.errors import bp

@bp.app_errorhandler(400)
def bad_request_error(error):
    return render_template('errors/400.html'), 403

@bp.app_errorhandler(403)
def forbidden_error(error):
    return render_template('errors/403.html'), 403

@bp.app_errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@bp.app_errorhandler(500)
def internal_error(error):
    db_session.rollback()
    return render_template('errors/500.html'), 500

@bp.app_errorhandler(CSRFError)
def csrf_error(e):
    print(request.form)
    return render_template('errors/csrf.html', reason=e.description), 400