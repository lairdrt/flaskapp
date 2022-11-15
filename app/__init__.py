
from flask import Flask, render_template
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from app.database.session import Session
from app.database import manage as dbmgnt
from app.instance.config import Config
from app.log.logger import logger, err
import app.globals.constants as CONST

ERB = CONST.MSG_INIT_BASE # error message base

# Global session for database access
# See Implicit Method Access under:
# https://docs.sqlalchemy.org/en/14/orm/contextual.html
db_session = Session()

# Global access to login information
loginmgnt = LoginManager()
loginmgnt.session_protection = 'strong'
loginmgnt.login_view = 'auth.login'
loginmgnt.login_message = 'Please sign in to access this page.'
loginmgnt.login_message_category = CONST.FLASH_WARNING
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # This extension adds support for break and continue in loops
    app.jinja_env.add_extension('jinja2.ext.loopcontrols')
    # Remove all the wasted space in rendered templates
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True

    # Tell all modules about app
    loginmgnt.init_app(app)
    csrf.init_app(app)
    dbmgnt.init_app(app)

    # Setup blueprints
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    from app.auth.oauth import github_bp
    app.register_blueprint(github_bp, url_prefix="/login") 
    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)
    from app.home import bp as home_bp
    app.register_blueprint(home_bp)
    return app

# Main application created here
app = create_app()

# Make sure models are loaded before any page accesses them
from app.database import models

# Removes session after request handling
# See Declarative under:
# https://flask.palletsprojects.com/en/1.1.x/patterns/sqlalchemy/
@app.teardown_appcontext
def shutdown_session(exception=None):
    Session.remove()

# Called each time database accessed
@loginmgnt.user_loader
def load_user(session_token):
    try:
        return db_session.query(models.User).filter_by(session_token = session_token).first()
    except Exception as ex:
        logger.error(err(ERB+1)+'Error loading user session token: ' + str(ex))
        return None

@loginmgnt.unauthorized_handler
def unauthorized_error():
    return render_template('errors/403.html'), 403