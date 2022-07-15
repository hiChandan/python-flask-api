import jwt
from flask import Blueprint, jsonify, request
from werkzeug.security import check_password_hash
import time
from routes.auth import allowed_users, secret_token

token_bp = Blueprint("token", __name__)


@token_bp.route("/token", methods=["POST"])
def login():
    d = request.json
    if "username" not in d or "password" not in d:
        raise Exception("Unable to authenticate")

    if not check_password_hash(allowed_users[d["username"]], d["password"]):
        raise Exception("Invalid password")
    encoded_jwt = jwt.encode({"username": str(
        d["username"]), "date": time.time()}, secret_token, algorithm="HS512")
    return jsonify({"token": encoded_jwt.decode('utf-8')})
