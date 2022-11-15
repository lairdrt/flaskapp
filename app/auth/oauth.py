from flask import redirect, url_for, request
from flask_login import current_user, login_user, confirm_login
from flask_dance.consumer import oauth_authorized
from flask_dance.contrib.github import github, make_github_blueprint
from flask_dance.consumer.storage.sqla import SQLAlchemyStorage
from app import db_session
from app.instance.config import Config
from app.database.models import User, OAuth
from app.log.logger import logger, err
from secrets import token_urlsafe
from sqlalchemy.orm.exc import NoResultFound
from urllib.parse import urlparse, urljoin
from werkzeug.urls import url_parse
import app.globals.constants as CONST

# Check for basic proper URL form
def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc

github_bp = make_github_blueprint(
    client_id=Config.GITHUB_ID,
    client_secret=Config.GITHUB_SECRET,
    scope = 'user',
    storage=SQLAlchemyStorage(
        OAuth,
        db_session,
        user=current_user,
        user_required=False
    )
)

@oauth_authorized.connect_via(github_bp)
def github_logged_in(blueprint, token):
    info = github.get("/user")
    if info.ok:
        # Extract username from provider response
        account_info = info.json()
        username = account_info["login"]
        # See if user already exists in the database
        user = db_session.query(User).filter_by(oauth_github=username).first()
        if user is None:
            # Add (github) user to database
            user = User()
            user.username = '(gh)' + username
            user.oauth_github = username
            db_session.add(user)
            db_session.commit()
        # Update user session token
        db_session.query(User).filter(User.id == user.id).update(
            {User.session_token: token_urlsafe(CONST.SESSION_TOKEN_LEN)},
            synchronize_session = False)
        db_session.commit()
        login_user(user)
        confirm_login()
        next_page = request.args.get('next')
        if not is_safe_url(next_page):
            return abort(400)
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home.index')
        return redirect(next_page)