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
        # Creates all database tables in model
        print('Dropping all tables...')
        Base.metadata.drop_all(bind=engine)
        print('Creating all tables...')
        Base.metadata.create_all(bind=engine)
        print("Done")

    @database.command()
    def change():
        return

    @database.command()
    def reset():
        return