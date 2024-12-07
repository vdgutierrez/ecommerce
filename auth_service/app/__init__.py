from flask import Flask
from flask_jwt_extended import JWTManager
from shared.database import db
from shared.config import Config  # Importa la configuración

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Usa la configuración compartida
    db.init_app(app)
    jwt = JWTManager(app)
    from .routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix="/auth")
    return app
