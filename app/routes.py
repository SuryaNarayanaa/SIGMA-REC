from logging import Logger
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt, unset_jwt_cookies
from flask_wtf.csrf import CSRFError
from datetime import timedelta
from .utils import validate_password, get_user_by_email, get_all_users, find_by_id, update_record, delete_user_by_id
from .models import User
from .blocklist import BLOCKLIST
from .Schemas import UserRegistrationModel, UserLoginModel, UserUpdateModel
from pydantic import ValidationError
user = Blueprint("user", __name__, url_prefix="/user")


# Helper Functions
def serialize_user(user):
    if user:
        user["_id"] = str(user["_id"])  # Convert _id to string
    return user


def check_if_admin():
    claims = get_jwt()
    current_user = get_jwt_identity()
    isadmin = claims.get("isadmin")
    if not current_user or not isadmin:
        return False
    return True



# Common routes
@user.route("/users/<user_id>", methods=["GET"])
@jwt_required()
def get_user_by_id(user_id):
    user = find_by_id(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify(serialize_user(user)), 200


@user.route("/logout", methods=["POST"])
@jwt_required()
def logout_user():
    jti = get_jwt()["jti"]
    BLOCKLIST.add(jti)

    response = jsonify({"message": "Logout successful"})
    unset_jwt_cookies(response)
    return response, 200



# User-specific routes
@user.route("/register", methods=["POST"])
def register_user():
    try:
        data = request.get_json()
        user_data = UserRegistrationModel(**data)  
    except ValidationError as err:
        return jsonify({"error": err.errors()}), 400

    existing_user = get_user_by_email(user_data.email)
    if existing_user:
        return jsonify({"error": "User already exists"}), 400

    new_user = User(
        user_data.username, user_data.email, user_data.password, user_data.isadmin
    )
    new_user.save()
    return jsonify({"message": "User registered successfully"}), 201


@user.route("/login", methods=["POST"])
def login_user():
    try:
        data = request.form or {}
        user_data = UserLoginModel(**data)  
    except ValidationError as err:
        return jsonify({"error": err.errors()}), 400

    user = get_user_by_email(user_data.email)
    if not user or not validate_password(user["password"], user_data.password):
        return jsonify({"error": "Invalid email or password"}), 401

    access_token = create_access_token(
        identity=str(user["_id"]),
        additional_claims={"email": user["email"], "isadmin": user["isadmin"]},
        expires_delta=timedelta(hours=1),
    )
    return jsonify({
        "message": f"Login successful for {user['username']}",
        "access_token": access_token,
    }), 200



# Admin-specific routes
@user.route("/users", methods=["GET"])
@jwt_required()
def fetch_all_users():
    if not check_if_admin():
        return jsonify({"error": "Unauthorized access"}), 401

    users = get_all_users()
    return jsonify([serialize_user(user) for user in users]), 200


@user.route("/users/<user_id>", methods=["PUT"])
@jwt_required()
def update_user(user_id):
    if not check_if_admin():
        return jsonify({"error": "Unauthorized access"}), 401

    try:
        data = request.get_json()
        user_data = UserUpdateModel(**data) 
    except ValidationError as err:
        return jsonify({"error": err.errors()}), 400

    user = find_by_id(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    updated_data = {
        "username": user_data.username or user["username"],
        "email": user_data.email or user["email"],
        "password": user_data.password or user["password"],
        "isadmin": user_data.isadmin if user_data.isadmin is not None else user["isadmin"],
    }
    update_record(user_id, **updated_data)
    return jsonify({"message": "User updated successfully"}), 200


@user.route("/users/<user_id>", methods=["DELETE"])
@jwt_required()
def delete_user(user_id):
    if not check_if_admin():
        return jsonify({"error": "Unauthorized access"}), 401

    count = delete_user_by_id(user_id)
    if count == 0:
        return jsonify({"error": "User not found"}), 404

    return jsonify({"message": f"User deleted successfully. Count: {count}"}), 200


@user.errorhandler(CSRFError)
def handle_csrf_error(e):
    return jsonify({"error": "CSRF token missing or incorrect."}), 400    