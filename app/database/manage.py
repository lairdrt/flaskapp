from app.database.session import engine, ManagedSession
from app.database.models import *
import click

# Commands are of the form 'flask database command', e.g., flask database create
def init_app(app):
    @app.cli.group()
    def database():
        pass

    @database.command()
    def create():
        print('Dropping all tables...')
        Base.metadata.drop_all(bind=engine)
        print('Creating all tables...')
        Base.metadata.create_all(bind=engine)
        print('Adding default user(s)...')
        with ManagedSession() as db_session:
            u = User(username='rtlaird', email='robin.laird@cox.net')
            u.set_password('Thx1138!')
            u.set_recovery_password('B54_up@9!Z*{;x6-')
            db_session.add(u)
            db_session.commit()
        print("Done")
        return

    @database.command()
    def change():
        return

    @database.command()
    def reset():
        return