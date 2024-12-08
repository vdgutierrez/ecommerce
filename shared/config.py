class AuthConfig:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root@localhost/auth_service_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "your_secret_key"

class CatalogConfig:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root@localhost/catalog_service_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "your_secret_key"

