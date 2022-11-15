from flask_login import current_user, login_user
from flask_dance.consumer import oauth_authorized
from flask_dance.contrib.github import github, make_github_blueprint
from flask_dance.consumer.storage.sqla import SQLAlchemyStorage
from app import db_session
from app.instance.config import Config
from app.database.models import User, OAuth
from app.log.logger import logger, err
from sqlalchemy.orm.exc import NoResultFound

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
    logger.debug("github_logged_in: SP1")
    if info.ok:
        logger.debug("github_logged_in: SP2")
        account_info = info.json()
        username = account_info["login"]
        try:
            logger.debug("github_logged_in: SP3")
            user = db_session.query(User).filter_by(oauth_github=username).one()
            logger.debug("github_logged_in: user.username:" + str(user.username))
            logger.debug("github_logged_in: user.oauth_github:" + str(user.oauth_github))
            login_user(user)
        except NoResultFound:
            logger.debug("github_logged_in: SP4")
            # Save to db
            user = User()
            user.username = '(gh)' + username
            user.oauth_github = username
            # Save current user
            db_session.add(user)
            db_session.commit()
            login_user(user)