from flask import Blueprint, jsonify

health_bp = Blueprint("health", __name__)


@health_bp.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "OK"})


@health_bp.route("/", methods=["GET"])
def basic_check():
    return jsonify({"message": "App is working"})
