from flask import request, jsonify
from app import app, db

@app.route('/products', methods=['GET'])
def get_products():
    products = list(db.products.find({}, {'_id': 0}))
    return jsonify(products)

@app.route('/products', methods=['POST'])
def add_product():
    data = request.json
    db.products.insert_one(data)
    return jsonify({"message": "Product added successfully"}), 201
