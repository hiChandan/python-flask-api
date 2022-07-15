from flask import Flask

from routes.health import health_bp
from routes.token import token_bp
from routes.errors import error_bp
from routes.users import users_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(token_bp)
    app.register_blueprint(health_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(error_bp)

    return app
