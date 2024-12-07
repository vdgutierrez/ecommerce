class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root@localhost/auth_service_db"  # O para catalog_service_db según el servicio
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "your_secret_key"
