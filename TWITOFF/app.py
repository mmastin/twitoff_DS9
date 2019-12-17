"""Code for app"""

from flask import Flask

# make our app factory

def create_app():
    app = Flask(__name__)

    # add config for database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'

    # have the database know about the app
    DB.init_app(app)

    @app.route('/')
    def root():
        return 'Welcome to Twitoff'
    return app

