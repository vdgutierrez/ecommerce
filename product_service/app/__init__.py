from flask import Flask
from shared.database import db
from shared.config import Config  # Importa la configuración

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Usa la configuración compartida
    db.init_app(app)
    from .routes import catalog_bp
    app.register_blueprint(catalog_bp, url_prefix="/catalog")
    return app
