from flask import request, jsonify
from app import app, db
from models import User
from flask_jwt_extended import create_access_token

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    new_user = User(username=data['username'], password=data['password'], role=data['role'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user and user.password == data['password']:
        access_token = create_access_token(identity={'username': user.username, 'role': user.role})
        return jsonify({"token": access_token})
    return jsonify({"message": "Invalid credentials"}), 401
