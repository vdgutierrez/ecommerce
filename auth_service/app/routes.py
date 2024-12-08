from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from .models import User, db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"message": "Invalid input"}), 400

    hashed_password = generate_password_hash(data['password'])
    user = User(username=data['username'], password=hashed_password)

    # Verifica si el usuario ya existe
    if User.query.filter_by(username=data['username']).first():
        return jsonify({"message": "Username already exists"}), 409

    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()

    if user and check_password_hash(user.password, data['password']):
        token = create_access_token(identity={"username": user.username})
        return jsonify({"token": token}), 200

    return jsonify({"message": "Invalid credentials"}), 401
