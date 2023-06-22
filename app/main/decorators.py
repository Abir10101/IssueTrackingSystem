from functools import wraps
from flask import request
from app.auth.utils import refresh_login_token
from flask import current_app


def token_required(f):
    @wraps(f)
    def decorated( *args, **kwargs ):
        try:
            token = request.headers['Authorization'].split(" ")[1]
            details = refresh_login_token( token )

            return f( details["user_id"], details["user_token"] )

        except KeyError as err:
            response = {
                "isOk": False,
                "status": 400,
                "message": "Auth Token Required!"
            }
        
        except ValueError as err:
            response = {
                "isOk": False,
                "status": 400,
                "message": f"{err}"
            }

        return response, response['status']

    return decorated
