from flask import jsonify, request, current_app
from . import main_blueprint

from .utils import health_check, add_ticket, add_branch, get_all_tickets, get_single_ticket, update_ticket, delete_ticket, get_all_branches, update_branch, delete_branch
from .decorators import token_required
from .exc import *


@main_blueprint.route("/health", methods=["GET"])
def health():
    current_app.logger.info("Main Logs Running")
    health_check()
    return jsonify({"status": 200, "data": "App Running..."})


@main_blueprint.route("/tickets", methods=["GET", "POST", "PATCH", "DELETE"])
@token_required
def tickets(user_id, token):
    if request.method == "POST":
        request_data = request.get_json()

        if "code" not in request_data or \
            "description" not in request_data or \
            "status" not in request_data:
            response = {
                "isOk": False,
                "status": 400,
                "message": "Invalid Parameters passed"
            }

        else:
            code = request_data["code"]
            description = request_data["description"]
            status = request_data["status"]

            try:
                ticket_id = add_ticket(user_id, code, description, status)
            except (ValidationError, DuplicationError) as err:
                response = {
                    "isOk": False,
                    "status": 400,
                    "message": f"{err}"
                }
            else:
                response = {
                    "isOk": True,
                    "status": 200,
                    "message": "Ticket added successfully",
                    "data": {
                        "ticket_id": ticket_id,
                    }
                }

    elif request.method == "GET":
        tickets = get_all_tickets(user_id)

        if tickets:
            response = {
                "isOk": True,
                "status": 200,
                "message": "Tickets fetched successfully",
                "data": {
                    "token": token,
                    "tickets": tickets
                }
            }
        else:
            response = {
                "isOk": True,
                "status": 200,
                "message": "No tickets found",
            }

    elif request.method == "PATCH":
        request_data = request.get_json()

        if "ticket_code" not in request_data or \
            "new_code" not in request_data or \
            "new_description" not in request_data or \
            "new_status" not in request_data:
            response = {
                "isOk": False,
                "status": 500,
                "message": "Invalid parameters passed"
            }

        else:
            ticket_code = request_data["ticket_code"]
            new_code = request_data["new_code"]
            new_description = request_data["new_description"]
            new_status = request_data["new_status"]

            try:
                status = update_ticket(ticket_code, user_id, new_code, new_description, new_status)
            except (ValidationError, DuplicationError) as err:
                response = {
                    "isOk": False,
                    "status": 400,
                    "message": f"{err}"
                }
            else:
                response = {
                    "isOk": True,
                    "status": 200,
                    "message": "Ticket updated successfully",
                    "data": {
                        "token": token
                    }
                }

    elif request.method == "DELETE":
        request_data = request.get_json()

        if "code" not in request_data:
            response = {
                "isOk": False,
                "status": 400,
                "message": "Invalid parameters passed"
            }

        else:
            code = request_data["code"]

            try:
                status = delete_ticket(code, user_id)
            except ValidationError as err:
                response = {
                    "isOk": False,
                    "status": 400,
                    "message": f"{err}",
                }
            else:
                response = {
                    "isOk": True,
                    "status": 200,
                    "message": "Ticket deleted successfully",
                    "data": {
                        "token": token
                    }
                }

    return jsonify(response), response["status"]


@main_blueprint.route("/ticket/<int:ticket_id>", methods=["GET"])
@token_required
def ticket_single(user_id, token, ticket_id):
    if request.method == "GET":
        try:
            ticket = get_single_ticket(ticket_id, user_id)
        except ValidationError as err:
            response = {
                "isOk": False,
                "status": 400,
                "message": f"{err}",
            }
        else:
            response = {
                "isOk": True,
                "status": 200,
                "message": "Ticket fetched successfully",
                "data": {
                    "token": token,
                    "ticket": ticket
                }
            }

    return jsonify(response), response["status"]


@main_blueprint.route("/branches/<int:ticket_code>", methods=["GET"])
@token_required
def getBranches(user_id, token, ticket_code):

    if not ticket_code:
        response = {
                "isOk": False,
                "status": 400,
                "message": "Invalid parameters passed",
            }
    else:
        try:
            branches = get_all_branches(user_id, ticket_code)
        except ValidationError as err:
            response = {
                "isOk": False,
                "status": 400,
                "message": f"{err}",
            }
        else:
            if branches:
                response = {
                    "isOk": True,
                    "status": 200,
                    "message": "Branches fetched successfully",
                    "data": {
                        "token": token,
                        "branches": branches
                    }
                }
            else:
                response = {
                    "isOk": True,
                    "status": 200,
                    "message": "No branches found",
                    "data": {
                        "token": token,
                    }
                }

    return jsonify(response), response["status"]


@main_blueprint.route("/branches", methods=["POST"])
@token_required
def addBranch(user_id, token):

    request_data = request.get_json()

    if "ticket_code" not in request_data or \
        "name" not in request_data or \
        "status" not in request_data:
        response = {
                "isOk": False,
                "status": 500,
                "message": "Invalid parameters passed"
            }
    else:
        ticket_code = request_data["ticket_code"]
        name = request_data["name"]
        status = request_data["status"]

        try:
            branch_id = add_branch(user_id, ticket_code, name, status)
        except (ValidationError, DuplicationError) as err:
            response = {
                "isOk": False,
                "status": 500,
                "message": f"{err}"
            }
        else:
            response = {
                "isOk": True,
                "status": 200,
                "message": "Branch added successfully",
                "data": {
                    "token": token,
                    "actions": {
                        "update": {
                            "uri": "/branches",
                            "method": "PATCH"
                        },
                        "delete": {
                            "uri": "/branches",
                            "method": "DELETE"
                        },
                        "fetchAll": {
                            "uri": f"/branches/${ticket_code}",
                            "method": "GET"
                        }
                    }
                }
            }

    return jsonify(response), response["status"]


@main_blueprint.route("/branches", methods=["PATCH"])
@token_required
def editBranch(user_id, token):

    request_data = request.get_json()

    if "old_name" not in request_data:
        response = {
            "isOk": False,
            "status": 400,
            "message": "Invalid parameters passed"
        }

    else:
        old_name = request_data["old_name"]
        new_name = request_data["new_name"]
        new_status = request_data["new_status"]

        try:
            branch = update_branch(user_id, old_name, new_name, new_status)
        except (ValidationError, DuplicationError) as err:
            response = {
                "isOk": False,
                "status": 400,
                "message": f"{err}"
            }
        else:
            response = {
                "isOk": True,
                "status": 200,
                "message": "Branch updated successfully",
                "data": {
                    "token": token,
                    "actions": {
                        "add": {
                            "uri": "/branches",
                            "method": "POST"
                        },
                        "delete": {
                            "uri": "/branches",
                            "method": "DELETE"
                        },
                        "fetchAll": {
                            "uri": f"/branches/{branch.ticket.t_code}",
                            "method": "GET"
                        }
                    }
                }
            }

    return jsonify(response), response["status"]


@main_blueprint.route("/branches", methods=["DELETE"])
@token_required
def deleteBranch(user_id, token):

    request_data = request.get_json()

    if "branch_name" not in request_data:
        response = {
            "isOk": False,
            "status": 400,
            "message": "Invalid parameters passed"
        }

    else:
        branch_name = request_data["branch_name"]

        try:
            status = delete_branch(user_id, branch_name)
        except ValidationError as err:
            response = {
                "isOk": False,
                "status": 400,
                "message": f"{err}",
            }
        else:
            response = {
                "isOk": True,
                "status": 200,
                "message": "Branch deleted successfully",
                "data": {
                    "token": token
                }
            }

    return jsonify(response), response["status"]
