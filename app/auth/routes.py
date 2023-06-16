from flask import jsonify, request, current_app
from . import auth_blueprint

# from app.utils import add_ticket, get_all_tickets, get_single_ticket, update_ticket, delete_ticket, add_branch, get_all_branches, update_branch, delete_branch, health_check
# from app.decorators import token_required

from .utils import health_check

# import auth


@auth_blueprint.route( '/health', methods=['GET'] )
def _health():
    current_app.logger.info("auth Running")
    health_check()
    return jsonify({"status": 200, "data": "auth Running..."})
