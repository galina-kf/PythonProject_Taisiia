import secrets

from flask import Flask
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

from Taisiia_project.app.views import shopping_bp, main_bp
from Taisiia_project.database import db


def create_app():
    app = Flask(__name__)

    app.jinja_env.add_extension("jinja2.ext-do")
    app.config.from_mapping(
        SECRET_KEY=secrets.token_hex(64),
        SQLALCHEMY_DATABASE_URI="sqlite:///library.db",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    app.register_blueprint(shopping_bp)
    #app.register_blueprint(products_bp)
    #app.register_blueprint(brands_bp)
    #app.register_blueprint(colors_bp)
    app.register_blueprint(main_bp)

    db.init_app(app)
    Migrate(app, db)
    CSRFProtect(app)

    return app
