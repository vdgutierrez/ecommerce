from flask import Blueprint, request, jsonify
from .models import Product, db
from flask_jwt_extended import jwt_required

catalog_bp = Blueprint('catalog', __name__)

@catalog_bp.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{"id": p.id, "name": p.name, "price": p.price, "stock": p.stock} for p in products])

@catalog_bp.route('/products', methods=['POST'])
@jwt_required()  # Proteger este endpoint con JWT
def add_product():
    data = request.json
    if not data or 'name' not in data or 'price' not in data or 'stock' not in data:
        return jsonify({"message": "Invalid input"}), 400

    product = Product(name=data['name'], price=data['price'], stock=data['stock'])
    db.session.add(product)
    db.session.commit()
    return jsonify({"message": "Product added successfully"}), 201