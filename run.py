from application.runapp import create_app
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


if __name__ =='__main__':
    app = create_app()
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.run(debug=True)