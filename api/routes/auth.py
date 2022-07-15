
import jwt
import os

from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from werkzeug.security import generate_password_hash, check_password_hash

import os
from dotenv import load_dotenv

load_dotenv()
secret_token = os.getenv("mysecret")
username = os.getenv("api-username")
password = os.getenv("api-password")

allowed_users = {
    username: generate_password_hash(password)
}

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth(scheme="Bearer")


@basic_auth.verify_password
def verify_basic_password(username, password):
    return None
    if username not in allowed_users:
        return None

    if check_password_hash(allowed_users[username], password):
        return username


@token_auth.verify_token
def verify_token(token):
    try:
        decoded_jwt = jwt.decode(token, secret_token, algorithms=["HS512"])
    except Exception as e:
        return None
    if decoded_jwt["username"] in allowed_users:
        return True
    return None
