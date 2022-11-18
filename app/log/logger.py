from app.instance.config import Config
from logging.handlers import SMTPHandler, RotatingFileHandler
import app.globals.constants as CONST
import logging
import os

# Need config for mail options
config = Config()

# Global logger
logger = logging.getLogger('sdr')

# Formatter
if config.DEBUG:
    fmt = '['+config.SERIAL_NUMBER+']' + ' [%(asctime)23s] %(levelname)s: %(message)s [%(pathname)s:%(lineno)d]'
else:
    fmt = '['+config.SERIAL_NUMBER+']' + ' [%(asctime)23s] %(levelname)s: %(message)s'
formatter = logging.Formatter(fmt)

# To the console
# DEBUG and higher to console
ch = logging.StreamHandler()
ch.setFormatter(formatter)
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)

# To a log file
# INFO and higher to log file
if not os.path.exists(CONST.LOG_FILE_DIR):
    os.mkdir(CONST.LOG_FILE_DIR)
fh = RotatingFileHandler(CONST.LOG_FILE_NAME, maxBytes=10240, backupCount=10)
fh.setFormatter(formatter)
fh.setLevel(logging.INFO)
logger.addHandler(fh)

# Via email
# ERROR and higher to email
if config.MAIL_SERVER:
    auth = None
    if config.MAIL_USERNAME or config.MAIL_PASSWORD:
        auth = (config.MAIL_USERNAME, config.MAIL_PASSWORD)
    secure = None
    if config.MAIL_USE_TLS:
        secure = ()
    mh = SMTPHandler(
        mailhost=(config.MAIL_SERVER, config.MAIL_PORT),
        fromaddr='no-reply@' + config.MAIL_SERVER,
        toaddrs=config.ADMINS,
        subject='Waterworks Notification',
        credentials=auth,
        secure=secure)
    mh.setFormatter(formatter)
    mh.setLevel(logging.ERROR)
    logger.addHandler(mh)

# Default to DEBUG
logger.setLevel(logging.DEBUG)

def err(n):
    return '{:d} '.format(n)