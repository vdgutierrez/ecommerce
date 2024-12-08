from flask import Flask
from flask_cors import CORS
from shared.database import db
from shared.config import CatalogConfig
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)
    app.config.from_object(CatalogConfig)  # Configuración de la base de datos y JWT
    db.init_app(app)
    JWTManager(app)  # Inicializa el gestor de JWT
    CORS(app, origins="http://127.0.0.1:8000")
    from .routes import catalog_bp
    app.register_blueprint(catalog_bp, url_prefix="/catalog")

    return app
