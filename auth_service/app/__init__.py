from flask import Flask
from flask_jwt_extended import JWTManager
from shared.database import db
from shared.config import AuthConfig  # Importa la configuración
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object(AuthConfig)  # Usa la configuración compartida
    db.init_app(app)
    jwt = JWTManager(app)
    CORS(app, origins="http://127.0.0.1:8000")
    from .routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix="/auth")
    return app
