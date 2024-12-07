from flask import Blueprint, request, jsonify
from .models import Product, db

catalog_bp = Blueprint('catalog', __name__)

@catalog_bp.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{"id": p.id, "name": p.name, "price": p.price, "stock": p.stock} for p in products])

@catalog_bp.route('/products', methods=['POST'])
def add_product():
    data = request.json
    product = Product(name=data['name'], price=data['price'], stock=data['stock'])
    db.session.add(product)
    db.session.commit()
    return jsonify({"message": "Product added successfully"}), 201
