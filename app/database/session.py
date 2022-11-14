from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from app.instance.config import Config
import contextlib

# Thread-local sessions
# https://docs.sqlalchemy.org/en/14/orm/contextual.html
# https://copdips.com/2019/05/using-python-sqlalchemy-session-in-multithreading.html
# https://gist.github.com/nitred/4323d86bb22b7ec788a8dcfcac03b27a
# https://flask.palletsprojects.com/en/1.1.x/patterns/sqlalchemy/

config = Config()
if config.SQLALCHEMY_DATABASE == 'postgres':
    engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
elif config.SQLALCHEMY_DATABASE == 'mysql':
    engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
elif config.SQLALCHEMY_DATABASE == 'sqlite3':
    engine = create_engine(config.SQLALCHEMY_DATABASE_URI, connect_args={'check_same_thread':False})
else:
    raise RuntimeError('Missing database engine specification')
Session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base(bind=engine)

@contextlib.contextmanager
def ManagedSession():
    global Session
    if Session is None:
        raise ValueError("Session has not been created yet")
    session = Session()
    try:
        yield session
        session.commit()
        session.flush()
    except Exception:
        session.rollback()
        raise
    finally:
        Session.remove()