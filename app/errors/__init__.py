from flask import Blueprint

bp = Blueprint('errors', __name__, url_prefix='')

from app.errors import handlers