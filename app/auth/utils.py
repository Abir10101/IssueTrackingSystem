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
        payload = jwt.decode( token, app.secret_key, algorithms='HS256' )
    except jwt.ExpiredSignatureError:
        raise Exception('Token expired.')
    except jwt.InvalidTokenError:
        raise Exception('Invalid token.')
    return {
        'username': payload['sub'],
        'secret': payload['secret'],
        'expiry': payload['expiry']
    }

def register( username :str, password :str, name :str ) -> str:
    try:
        new_user = User()
        new_user.u_username = username
        new_user.u_password = password
        new_user.u_name = name
        user = new_user.save()

        token = encode_auth_token( user.u_username, user.u_secret )

    except ValueError as err:
        raise ValueError( f"{err}" )

    except Exception as err:
        current_app.logger.info(f"Error user register: {str(err)}")
        raise Exception("Something went wrong! Contact support.")

    return token

def login( username :str, password :str ) -> str:
    try:
        user = User.get_user_by_username( username )

    except Exception as err:
        current_app.logger.info(f"Error user login: {str(err)}")
        raise Exception("Something went wrong! Contact support.")

    if user:
        if User.check_password( password, user.u_password ):
            token = encode_auth_token( user.u_username, user.u_secret )
        else:
            raise ValueError("Invalid Password")
    else:
        raise ValueError("User does not exists")

    return token
