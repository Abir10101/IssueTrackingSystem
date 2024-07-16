import jwt
import secrets
import datetime
import werkzeug.security as _ws
from app.services.queue import Queue
from app.config.base import BaseConfig
from flask import current_app
from .models.user import User
from app import db
from .exc import *


# functions
def health_check():
    from sqlalchemy import text

    query = text("SELECT 1;")
    with db.engine.connect() as connection:
        result = connection.execute( query )

    return


def encode_auth_token( email :int, secret :str ) -> str:
    expiry = datetime.datetime.utcnow() + datetime.timedelta( seconds=BaseConfig.AUTH_TOKEN_VALIDITY )
    payload = {
        'exp': expiry,
        'iat': datetime.datetime.utcnow(),
        'sub': email,
        'secret': secret,
        'expiry': expiry.strftime('%s')
    }
    return jwt.encode(
        payload,
        current_app.secret_key,
        algorithm='HS256'
    )


def decode_auth_token( token :str ) -> dict:
    try:
        payload = jwt.decode( token, current_app.secret_key, algorithms='HS256' )
        return {
            'email': payload['sub'],
            'secret': payload['secret'],
            'expiry': payload['expiry']
        }
    except jwt.ExpiredSignatureError:
        raise TokenError('Token expired')
    except jwt.InvalidTokenError:
        raise TokenError('Invalid token')


def register( email :str, password :str, name :str ) -> str:
    try:
        new_user = User()
        new_user.u_email = email
        new_user.hash_password( password )
        new_user.u_name = name
        new_user.save()
    except ValueError as err:
        err = f"{err}"
        if err == "InvalidEmail":
            raise ValidationError("Invalid Email")
        elif err == "InvalidPassword":
            raise ValidationError("Invalid Password")
        elif err == "InvalidName":
            raise ValidationError("Invalid Name")
        elif err == "UserExists":
            raise DuplicationError("User already exists")

    queue = Queue()
    queue.push_message("UserRegistered", new_user.to_json())

    return new_user


def login( email :str, password :str ) -> str:
    user = User.get_user_by_email( email )

    if user:
        if User.check_password( password, user.u_password ):
            token = encode_auth_token( user.u_email, user.u_secret )
            return token
        else:
            raise ValidationError("Invalid password")
    else:
        raise NotFoundError("Invalid user")


def logout( token :str ) -> bool:
    decoded_token = decode_auth_token( token )
    user = User.get_user_by_email( decoded_token["email"] )

    if not user:
        raise UnauthorizationError("Invalid user")

    if decoded_token["secret"] != user.u_secret:
        raise UnauthorizationError("User not logged in.")

    user.refresh_secret()
    return True


def refresh_login_token( token: str ) -> dict:
    decoded = decode_auth_token( token )
    email = decoded['email']
    token_secret = decoded['secret']
    token_exp = datetime.datetime.fromtimestamp( int(decoded['expiry']) )

    user = User.get_user_by_email( email )

    if not user:
        raise UnauthorizationError("Invalid user.")

    if token_secret != user.u_secret:
        raise UnauthorizationError("User not logged in.")

    if (token_exp - datetime.datetime.utcnow()) < datetime.timedelta( seconds=BaseConfig.AUTH_TOKEN_REFRESH_RATE ):
        new_secret = user.refresh_secret()
        new_token = encode_auth_token( email, new_secret )
        token = new_token

    return {
        "user_id": user.id,
        "user_token": token
    }

