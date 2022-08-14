from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    #app.config.from_object('application.config.Config')
    db.init_app(app)
    with app.app_context():

        api = Api(app)
        app.config['api'] = api

        from application import routes

        return app