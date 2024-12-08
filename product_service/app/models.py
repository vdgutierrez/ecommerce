from shared.database import db

class Product(db.Model):
    __tablename__ = 'products'  # Nombre exacto de la tabla

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)