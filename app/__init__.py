from flask import Flask,current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_cors import CORS,cross_origin

db = SQLAlchemy()
migrate = Migrate()
cors = CORS()

def create_app(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    cors.init_app(app)
    db.init_app(app)
    migrate.init_app(app,db)

    from app.api.teste import bp as teste_app
    app.register_blueprint(teste_app,url_prefix='/teste')

    return app

import app.models
