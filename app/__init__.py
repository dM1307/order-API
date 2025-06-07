from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
from .config import Config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    Swagger(app)

    from .routes.job_routes import job_bp
    app.register_blueprint(job_bp)

    return app