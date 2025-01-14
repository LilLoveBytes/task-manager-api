from flask import Blueprint

user_bp = Blueprint("users", __name__)

@user_bp.route("", methods=["GET"])
def get_users():
    return "all users"

@user_bp.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    return f"user {user_id}"

