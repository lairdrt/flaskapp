from flask import Blueprint

bp = Blueprint('home', __name__, url_prefix='')

from app.home import routes