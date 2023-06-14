from flask import jsonify, request, current_app
from . import main_blueprint

# from app.utils import add_ticket, get_all_tickets, get_single_ticket, update_ticket, delete_ticket, add_branch, get_all_branches, update_branch, delete_branch, health_check
from .utils import health_check
# from app.decorators import token_required

# import auth


@main_blueprint.route( '/health', methods=['GET'] )
def _health():
    current_app.logger.info("Logs Running")
    health_check()
    return jsonify({"status": 200, "data": "App Running..."})
