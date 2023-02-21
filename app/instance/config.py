from dotenv import load_dotenv
import os

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'), verbose=True)

# Configuration for all development phases
class Config(object):
    # Note that values coming from the environment are basically strings, not numbers nor booleans
    DEBUG = os.environ.get('FLASK_DEBUG') or False
    TESTING = os.environ.get('TESTING') or False
    SERIAL_NUMBER = os.environ.get('SERIAL_NUMBER') or os.urandom(13)
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(24)
    RECOVERY_PASSWORD = os.environ.get('RECOVERY_PASSWORD') or os.urandom(16)
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') == 'True'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_DEBUG = os.environ.get('MAIL_DEBUG') == 'True'
    ADMINS = ['support@samedayrules.com']
    SQLALCHEMY_DATABASE = os.environ.get('SQLALCHEMY_DATABASE') or 'sqlite'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False
    SESSION_COOKIE_NAME = 'sdrsession' # set the session cookie for our app to a unique name
    SESSION_COOKIE_SAMESITE = 'Lax' # prevents sending cookies with CSRF-prone requests from external sites ('Lax')
    SESSION_COOKIE_HTTPONLY = True # protects the contents of cookies from being read with JavaScript
    SESSION_COOKIE_SECURE = False # set the session cookie to be secure (must use HTTPS)
    REMEMBER_COOKIE_NAME = 'sdrremember' # set the session cookie for our app to a unique name
    REMEMBER_COOKIE_SAMESITE = 'Lax' # prevents sending cookies with CSRF-prone requests from external sites ('Lax')
    REMEMBER_COOKIE_HTTPONLY = True # protects the contents of cookies from being read with JavaScript
    REMEMBER_COOKIE_SECURE = False # set the session cookie to be secure (must use HTTPS)
    WTF_CSRF_SSL_STRICT = False # enforce same origin policy by checking that referrer matches host (HTTPS)
    WTF_CSRF_TIME_LIMIT = 3600 # set CSRF token time limit (None = valid for duration of the session - assumes you’re using WTF-CSRF protection)
    ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets') # DOM assets management
    GITHUB_ID = os.getenv('GITHUB_ID')
    GITHUB_SECRET = os.getenv('GITHUB_SECRET')
    SOCIAL_AUTH_GITHUB = GITHUB_ID and GITHUB_SECRET # enable/disable Github OAuth login
    OAUTHLIB_INSECURE_TRANSPORT = 0
