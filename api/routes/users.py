from routes.auth import basic_auth, token_auth

from flask import Blueprint, jsonify, request, Response

users_bp = Blueprint("users", __name__, url_prefix="/users")


@users_bp.route("", methods=["GET"])
@token_auth.login_required
def get_all_users():
    all_users = [{"id": 1, "name": "joe"}, {"id": 2, "name": "bob"}]
    return jsonify(all_users)


# @users_bp.route("", methods=["POST"])
# @basic_auth.login_required
# def create_user():
#     sample = {"sample": "OK POST BASIC AUTH"}
#     return jsonify(sample)
#     # return Response(status=204)


@users_bp.route("/app", methods=["GET"])
@token_auth.login_required
def create_user2():
    d = request.json
    sample = d
    return jsonify(sample)
