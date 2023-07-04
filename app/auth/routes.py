from flask import jsonify, request, current_app
from . import auth_blueprint
from .utils import health_check, register, login, logout
from .exc import *


@auth_blueprint.route( '/health', methods=['GET'] )
def _health():
    current_app.logger.info("auth Running")
    health_check()
    return jsonify({"status": 200, "data": "auth Running..."})


@auth_blueprint.route( '/register', methods=['POST'] )
def _resgister():
    if request.method == 'POST':
        request_data = request.get_json()

        if not request_data.get('username') or \
            not request_data.get('password') or \
            not request_data.get('name'):
            response = {
                "isOk": False,
                "status": 400,
                "message": "Invalid parameters passed"
            }

        else:
            username = request_data.get('username')
            password = request_data.get('password')
            name = request_data.get('name')

            try:
                token = register( username, password, name )
            except (ValidationError, DuplicationError) as err:
                response = {
                    "isOk": False,
                    "status": 400,
                    "message":  f"{err}",
                }
            else:
                response = {
                    "isOk": True,
                    "status": 200,
                    "message": "User added successfully",
                    "data": {
                        "token": token,
                    }
                }

    return jsonify(response), response["status"]


@auth_blueprint.route( '/login', methods=['POST'] )
def _login():
    if request.method == 'POST':
        request_data = request.get_json()
        if 'username' not in request_data or \
           'password' not in request_data:
            response = {
                "isOk": False,
                "status": 400,
                "message": "Invalid parameters passed"
            }
        elif len(request_data['username'].strip()) < 1:
            response = {
                "isOk": False,
                "status": 400,
                "message": "Username is required"
            }
        elif len(request_data['password'].strip()) < 1:
            response = {
                "isOk": False,
                "status": 400,
                "message": "Password is required"
            }
        else:
            username = request_data['username'].strip()
            password = request_data['password'].strip()

            try:
                token = login( username, password )
            except (ValidationError, NotFoundError) as err:
                response = {
                    "isOk": False,
                    "status": 400,
                    "message": f"{err}",
                }
            else:
                response = {
                    "isOk": True,
                    "status": 200,
                    "message": "User login successfully",
                    "data": {
                        "token": token
                    }
                }

    return jsonify(response), response["status"]


@auth_blueprint.route( '/logout', methods=['POST'] )
def _logout():
    if request.method == 'POST':
        request_data = request.get_json()

        if 'token' not in request_data:
            response = {
                "isOk": False,
                "status": 400,
                "message": "Invalid parameters passed"
            }
        elif len(request_data['token'].strip()) < 1:
            response = {
                "isOk": False,
                "status": 400,
                "message": "Token cannot be empty"
            }
        else:
            token = request_data['token']
            try:
                logout( token )
            except NotFoundError as err:
                response = {
                    "isOk": False,
                    "status": 400,
                    "message": f"{err}",
                }
            else:
                response = {
                    "isOk": True,
                    "status": 200,
                    "message": "User logout successfully"
                }

    return jsonify(response), response['status']
