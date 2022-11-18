from flask import render_template, request
from flask_wtf.csrf import CSRFError
from app import db_session
from app.errors import bp

@bp.app_errorhandler(400)
def bad_request_error(error):
    return render_template('errors/400.html', reason=error.description), 403

@bp.app_errorhandler(403)
def forbidden_error(error):
    return render_template('errors/403.html', reason=error.description), 403

@bp.app_errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html', reason=error.description), 404

@bp.app_errorhandler(500)
def internal_error(error):
    db_session.rollback()
    return render_template('errors/500.html', reason=error.description), 500

@bp.app_errorhandler(CSRFError)
def csrf_error(error):
    print(request.form)
    return render_template('errors/csrf.html', reason=error.description), 400