"""Code for app"""

from flask import Flask, render_template, request
from decouple import config
from .models import DB, User

# make our app factory

def create_app():
    app = Flask(__name__)

    # add config for database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    # stop tracking modifications on sqlalchemy config
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # have the database know about the app
    DB.init_app(app)

    @app.route('/')
    def root():
        users = User.query.all()
        return render_template('base.html', title='Home', users=users)
    return app

