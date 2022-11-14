from flask import render_template, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, confirm_login
from flask_dance.contrib.github import github
from app import db_session, csrf
from app.auth import bp
from app.auth.forms import LoginForm
from app.database.models import User
from app.log.logger import logger, err
from urllib.parse import urlparse, urljoin
from werkzeug.urls import url_parse
import app.globals.constants as CONST

ERB = CONST.MSG_AUTH_BASE+500 # error message base

# Check for basic proper URL form
def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc

# APP route: use shared session
@bp.route("/github")
def login_github():
    if not github.authorized:
        return redirect(url_for("github.login"))
    res = github.get("/user")
    return redirect(url_for('home.index'))

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        logger.debug(err(ERB+1)+'S3')
        user = db_session.query(User).filter_by(username=form.username.data).first()
        if user is None:
            logger.debug(err(ERB+1)+'Invalid username')
            return render_template('auth/login.html', msg='Invalid username', form=form)
        elif (not user.check_password(form.password.data)) and (not user.check_recovery_password(form.password.data)):
            logger.debug(err(ERB+1)+'Invalid username')
            return render_template('auth/login.html', msg='Invalid password', form=form)
        login_user(user)
        confirm_login()
        next_page = request.args.get('next')
        if not is_safe_url(next_page):
            return abort(400)
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home.index')
        return redirect(next_page)
    logger.debug(err(ERB+1)+'username:'+str(form.username.data))
    logger.debug(err(ERB+1)+'password:'+str(form.password.data))
    logger.debug(err(ERB+1)+'csrf_token:'+str(form.csrf_token.data))
    return render_template('auth/login.html', title='Sign in', form=form)

# APP route: use shared session
@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))