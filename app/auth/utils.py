import jwt
import secrets
import datetime
import werkzeug.security as _ws
from flask import current_app
from .config import Config
from .models.user import User


# functions
def health_check():
    from sqlalchemy import text

    query = text("SELECT 1;")
    with db.engine.connect() as connection:
        result = connection.execute( query )

    return


def encode_auth_token( username :int, secret :str ) -> str:
    expiry = datetime.datetime.utcnow() + datetime.timedelta( seconds=Config.TOKEN_VALIDITY )
    payload = {
        'exp': expiry,
        'iat': datetime.datetime.utcnow(),
        'sub': username,
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
            'username': payload['sub'],
            'secret': payload['secret'],
            'expiry': payload['expiry']
        }
    except jwt.ExpiredSignatureError:
        raise ValueError('Token expired.')
    except jwt.InvalidTokenError:
        raise ValueError('Invalid token.')


def register( username :str, password :str, name :str ) -> str:
    new_user = User()
    new_user.u_username = username
    new_user.u_password = password
    new_user.u_name = name
    user = new_user.save()

    token = encode_auth_token( user.u_username, user.u_secret )
    return token


def login( username :str, password :str ) -> str:
    user = User.get_user_by_username( username )

    if user:
        if User.check_password( password, user.u_password ):
            token = encode_auth_token( user.u_username, user.u_secret )
            return token
        else:
            raise ValueError("Invalid Password")
    else:
        raise ValueError("User does not exists")


def logout( token :str ) -> bool:
    username = decode_auth_token( token )['username']
    user = User.get_user_by_username( username )
    status = user.refresh_secret()
    return status


def refresh_login_token( token: str ) -> dict:
    decoded = decode_auth_token( token )
    username = decoded['username']
    token_secret = decoded['secret']
    token_exp = datetime.datetime.fromtimestamp( int(decoded['expiry']) )

    user = User.get_user_by_username( username )
    user_secret = user.u_secret

    if token_secret != user_secret:
        raise ValueError("User not logged in.")

    if (token_exp - datetime.datetime.utcnow()) < datetime.timedelta( seconds=Config.TOKEN_REFRESH_RATE ):
        new_token = encode_auth_token( user_id, token_secret )
        token = new_token

    return {
        "user_id": user.id,
        "user_token": token
    }

