from flask_login import UserMixin
from flask_dance.consumer.storage.sqla import OAuthConsumerMixin
from app.database.session import Base
from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String, types
from sqlalchemy.orm import relationship
from dateutil import tz
from werkzeug.security import generate_password_hash, check_password_hash
import app.globals.constants as CONST

######################################################################################
# 1. Units are maintained in the models using US/Imperial standards.
#    Measurements are then converted to other standards depending upon user prefs.
# 2. Date/time variables are kept in UTC and then converted to local time for display.
# 3. All 'name' fields of tables with multiple entries (rows) must be unique.
# 4. 'CHOICES' lists are formatted as [(id0,txt1), (id1,txt1), ...] for all values.
######################################################################################

# Time zone aware DateTime object (forces storage using UTC time zone)
class UTCDateTime(types.TypeDecorator):
    impl = types.DateTime
    def process_bind_param(self, value, dialect):
        if value is not None:
            return value.astimezone(tz.tzutc())
    def process_result_value(self, value, dialect):
        if value is not None:
            return value.replace(tzinfo=tz.tzutc())

# System users
class User(UserMixin, Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(64), index=True, unique=True)
    email = Column(String(256), index=True, unique=True)
    password_hash = Column(String(128))
    recovery_password_hash = Column(String(128))
    session_token = Column(String(CONST.SESSION_TOKEN_LEN+10), index=True)
    oauth_github = Column(String(128), nullable=True)

    def __repr__(self):
        return '<User.id {}>'.format(self.id)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def set_recovery_password(self, password):
        self.recovery_password_hash = generate_password_hash(password)

    def check_recovery_password(self, password):
        return check_password_hash(self.recovery_password_hash, password)
        
    def get_id(self):
        # Will be unique for each user session
        return str(self.session_token)

# OAuth users
# https://flask-dance.readthedocs.io/en/latest/_modules/flask_dance/consumer/storage/sqla.html#
class OAuth(OAuthConsumerMixin, Base):
    __tablename__ = 'oauth'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="cascade"), nullable=False)
    user = relationship(User)

    def __repr__(self):
        return '<OAuth.id {}>'.format(self.id)