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

# https://flask-dance.readthedocs.io/en/latest/providers.html#module-flask_dance.contrib.github
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

# https://flask-dance.readthedocs.io/en/latest/multi-user.html
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


        
# https://flask-dance.readthedocs.io/en/latest/multi-user.html

"""
# create/login local user on successful OAuth login
@oauth_authorized.connect_via(github_bp)
def github_logged_in(blueprint, token):
    if not token:
        flash("Failed to log in with GitHub.", category="error")
        return False

    resp = blueprint.session.get("/user")
    if not resp.ok:
        msg = "Failed to fetch user info from GitHub."
        flash(msg, category="error")
        return False

    github_info = resp.json()
    github_user_id = str(github_info["id"])

    # Find this OAuth token in the database, or create it
    query = OAuth.query.filter_by(
        provider=blueprint.name,
        provider_user_id=github_user_id,
    )
    try:
        oauth = query.one()
    except NoResultFound:
        oauth = OAuth(
            provider=blueprint.name,
            provider_user_id=github_user_id,
            token=token,
        )

    if oauth.user:
        # If this OAuth token already has an associated local account,
        # log in that local user account.
        # Note that if we just created this OAuth token, then it can't
        # have an associated local account yet.
        login_user(oauth.user)
        flash("Successfully signed in with GitHub.")

    else:
        # If this OAuth token doesn't have an associated local account,
        # create a new local user account for this user. We can log
        # in that account as well, while we're at it.
        user = User(
            # Remember that `email` can be None, if the user declines
            # to publish their email address on GitHub!
            email=github_info["email"],
            name=github_info["name"],
        )
        # Associate the new local user account with the OAuth token
        oauth.user = user
        # Save and commit our database models
        db.session.add_all([user, oauth])
        db.session.commit()
        # Log in the new local user account
        login_user(user)
        flash("Successfully signed in with GitHub.")

    # Since we're manually creating the OAuth model in the database,
    # we should return False so that Flask-Dance knows that
    # it doesn't have to do it. If we don't return False, the OAuth token
    # could be saved twice, or Flask-Dance could throw an error when
    # trying to incorrectly save it for us.
    return False        

"""