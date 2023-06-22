from flask import jsonify, request, current_app
from . import main_blueprint

# from app.utils import add_ticket, get_all_tickets, get_single_ticket, update_ticket, delete_ticket, add_branch, get_all_branches, update_branch, delete_branch, health_check
from .utils import health_check, add_ticket, add_branch
from .decorators import token_required

# import auth


@main_blueprint.route( '/health', methods=['GET'] )
def _health():
    current_app.logger.info("Main Logs Running")
    health_check()
    return jsonify({"status": 200, "data": "App Running..."})


@main_blueprint.route( '/tickets', methods=['GET', 'POST', 'PATCH', 'DELETE'] )
@token_required
def _tickets( user_id, token ):
    if request.method == 'POST':
        request_data = request.get_json()

        if 'code' not in request_data or \
            'description' not in request_data or \
            'status' not in request_data:
            response = {
                "isOk": False,
                "status": 500,
                "message": "Invalid Parameters passed"
            }

        else:
            code = request_data['code']
            description = request_data['description']
            status = request_data['status']

            try:
                ticket_id = add_ticket( user_id, code, description, status )
            except ValueError as err:
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

    # elif request.method == 'GET':
    #     try:
    #         tickets = get_all_tickets( user_id )
    #     except ValueError as err:
    #         response = {
    #             "isOk": False,
    #             "status": 400,
    #             "message": f"{err}"
    #         }
    #     else:
    #         if tickets:
    #             tickets_dict = {}
    #             for count, ticket in enumerate(tickets):
    #                 tickets_dict[count] = {}
    #                 tickets_dict[count]["id"] = ticket['id']
    #                 tickets_dict[count]["code"] = ticket['t_code']
    #                 tickets_dict[count]["description"] = ticket['t_description']
    #                 tickets_dict[count]["status"] = ticket['t_status']
    #             response = {
    #                 "isOk": True,
    #                 "status": 200,
    #                 "message": "Tickets fetched successfully",
    #                 "data": {
    #                     "token": token,
    #                     "tickets": tickets_dict
    #                 }
    #             }
    #         else:
    #             response = {
    #                 "isOk": True,
    #                 "status": 200,
    #                 "message": "No tickets found",
    #             }
    # elif request.method == 'PATCH':
    #     request_data = request.get_json()
    #     if 'ticket_id' not in request_data or \
    #         'code' not in request_data or \
    #         'description' not in request_data or \
    #         'status' not in request_data:
    #         response = {
    #             "isOk": False,
    #             "status": 500,
    #             "message": "Invalid parameters passed"
    #         }
    #     else:
    #         ticket_id = request_data['ticket_id']
    #         code = request_data['code']
    #         description = request_data['description']
    #         status = request_data['status']
    #         try:
    #             message = update_ticket( ticket_id, code, description, status )
    #         except Exception as err:
    #             response = {
    #                 "isOk": False,
    #                 "status": 500,
    #                 "message": f"{err}"
    #             }
    #         else:
    #             response = {
    #                 "isOk": True,
    #                 "status": 200,
    #                 "message": "Ticket updated successfully",
    #                 "data": {
    #                     "token": token
    #                 }
    #             }
    # elif request.method == 'DELETE':
    #     request_data = request.get_json()
    #     if 'ticket_id' not in request_data:
    #         response = {
    #             "isOk": False,
    #             "status": 500,
    #             "message": "Invalid parameters passed"
    #         }
    #     else:
    #         ticket_id = request_data['ticket_id']
    #         try:
    #             message = delete_ticket( ticket_id )
    #         except Exception as err:
    #             response = {
    #                 "isOk": False,
    #                 "status": 500,
    #                 "message": f"{err}",
    #             }
    #         else:
    #             response = {
    #                 "isOk": True,
    #                 "status": 200,
    #                 "message": "Ticket deleted successfully",
    #                 "data": {
    #                     "token": token
    #                 }
    #             }
    
    return jsonify(response), response["status"]


@main_blueprint.route( '/branches', methods=['GET', 'POST', 'PATCH', 'DELETE'] )
@token_required
def _branches( user_id, token ):
    if request.method == 'POST':
        request_data = request.get_json()
        if 'ticket_id' not in request_data or \
            'name' not in request_data or \
            'status' not in request_data:
            response = {
                    "isOk": False,
                    "status": 500,
                    "message": "Invalid parameters passed"
                }
        else:
            ticket_id = request_data['ticket_id']
            name = request_data['name']
            status = request_data['status']

            try:
                branch_id = add_branch( user_id, ticket_id, name, status )
            except ValueError as err:
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
                        "id": branch_id
                    }
                }

    # elif request.method == 'GET':
    #     request_data = request.get_json()
    #     if 'ticket_id' not in request_data:
    #         response = {
    #                 "isOk": False,
    #                 "status": 500,
    #                 "message": "Invalid parameters passed",
    #             }
    #     else:
    #         ticket_id = request_data['ticket_id']
    #         try:
    #             branches = get_all_branches( user_id, ticket_id )
    #         except Exception as err:
    #             response = {
    #                 "isOk": False,
    #                 "status": 500,
    #                 "message": f"{err}",
    #             }
    #         else:
    #             if branches:
    #                 branches_dict = {}
    #                 for count, branch in enumerate(branches):
    #                     branches_dict[count] = {}
    #                     branches_dict[count]["id"] = branch['id']
    #                     branches_dict[count]["name"] = branch['b_name']
    #                     branches_dict[count]["status"] = branch['b_status']
    #                 response = {
    #                     "isOk": True,
    #                     "status": 200,
    #                     "message": "Branches fetched successfully",
    #                     "data": {
    #                         "token": token,
    #                         "branches": branches_dict
    #                     }
    #                 }
    #             else:
    #                 response = {
    #                     "isOk": False,
    #                     "status": 500,
    #                     "message": "No Branches Found",
    #                 }

    # elif request.method == 'PATCH':
    #     request_data = request.get_json()
    #     if 'branch_id' not in request_data or \
    #         'name' not in request_data or \
    #         'status' not in request_data:
    #         response = {
    #             "isOk": False,
    #             "status": 500,
    #             "message": "Invalid parameters passed"
    #         }
    #     else:
    #         branch_id = request_data['branch_id']
    #         name = request_data['name']
    #         status = request_data['status']
    #         try:
    #             message = update_branch( branch_id, name, status )
    #         except Exception as err:
    #             response = {
    #                 "isOk": False,
    #                 "status": 500,
    #                 "message": f"{err}"
    #             }
    #         else:
    #             response = {
    #                 "isOk": True,
    #                 "status": 200,
    #                 "message": "Branch updated successfully",
    #                 "data": {
    #                     "token": token
    #                 }
    #             }

    # elif request.method == "DELETE":
    #     request_data = request.get_json()
    #     if 'branch_id' not in request_data:
    #         response = {
    #             "isOk": False,
    #             "status": 500,
    #             "message": "Invalid parameters passed"
    #         }
    #     else:
    #         branch_id = request_data['branch_id']
    #         try:
    #             message = delete_branch( branch_id )
    #         except Exception as err:
    #             response = {
    #                 "isOk": False,
    #                 "status": 500,
    #                 "message": f"{err}",
    #             }
    #         else:
    #             response = {
    #                 "isOk": True,
    #                 "status": 200,
    #                 "message": "Branch deleted successfully",
    #                 "data": {
    #                     "token": token
    #                 }
    #             }

    return jsonify(response), response["status"]

