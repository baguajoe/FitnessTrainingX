from flask import request, jsonify, Blueprint
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from api.models import db, User

# Create a Flask Blueprint
api = Blueprint('api', __name__)

# ----------------------------------------
# SIGNUP ROUTE
# ----------------------------------------
@api.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()

    email = data.get('email')
    username = data.get('username')
    password = data.get('password')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    role = data.get('role')

    # ✅ Validate required fields
    if not email or not username or not password:
        return jsonify({"error": "Email, username, and password are required"}), 400

    # 🔍 Check for duplicate email or username
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already in use"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already in use"}), 400

    # 🔐 Hash the password
    hashed_password = generate_password_hash(password)

    # 🧱 Create new user instance
    new_user = User(
        email=email,
        username=username,
        password=hashed_password,
        first_name=first_name,
        last_name=last_name,
        role=role
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created successfully"}), 201

# ----------------------------------------
# LOGIN ROUTE
# ----------------------------------------
@api.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    # ✅ Basic validation
    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    # 🔍 Lookup user
    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        return jsonify({"error": "Invalid email or password"}), 401

    # 🔐 Create JWT token
    access_token = create_access_token(identity=user.id)

    # ✅ Return token and user info
    return jsonify({
        "message": "Login successful",
        "token": access_token,
        "user": {
            "id": user.id,
            "email": user.email,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "role": user.role
        }
    }), 200
