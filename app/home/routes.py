from flask import render_template, redirect, url_for, request, jsonify
from flask_login import login_required
from app import db_session
from app.database.session import ManagedSession
from app.home import bp
from app.log.logger import logger, err
import app.globals.constants as CONST
import json

ERB = CONST.MSG_HOME_BASE # error message base

# APP route: use shared session
@bp.route('/', methods=['GET'])
@bp.route('/index', methods=['GET'])
@login_required
def index():
    if request.method == 'GET':
        try:
            pass
        except Exception as ex:
            raise
    return render_template('home/index.html', title='Dashboard')

# ASYNCH route: need separate session
@bp.route('/index/getstatus', methods=['GET'])
@login_required
def getstatus():
    with ManagedSession() as session:
        try:
            pass
        except Exception as ex:
            raise
        return jsonify(rstatus='ERROR', reason='Exception getting status')