from flask import current_app
from app import db
from .models.ticket import Ticket
from .models.branch import Branch
from .exc import *


# functions
def health_check():
    from sqlalchemy import text

    query = text("SELECT 1;")
    with db.engine.connect() as connection:
        result = connection.execute( query )

    return


def add_ticket( user_id, ticket_number, ticket_description, ticket_status ):
    try:
        new_ticket = Ticket()
        new_ticket.user_id = user_id
        new_ticket.t_code = ticket_number
        new_ticket.t_description = ticket_description
        new_ticket.t_status = ticket_status
        new_ticket.validate()
    except ValueError as err:
        err = f"{err}"
        if err == "InvalidCode":
            raise ValidationError(f"Invalid Ticket Code")
        elif err == "InvalidDescription":
            raise ValidationError(f"Invalid Ticket Description")
        elif err == "InvalidStatus":
            raise ValidationError(f"Invalid Ticket Status")
        elif err == "DuplicateCode":
            raise DuplicationError(f"{ticket_number} already exists")

    db.session.add(new_ticket)
    db.session.commit()

    return new_ticket.id


def get_all_tickets( user_id ):
    tickets = Ticket.get_user_tickets( user_id )

    tickets_dict = {}

    if tickets:
        for t_count, ticket in enumerate(tickets):
            tickets_dict[t_count] = {}
            tickets_dict[t_count]["id"] = ticket.id
            tickets_dict[t_count]["code"] = ticket.t_code
            tickets_dict[t_count]["description"] = ticket.t_description
            tickets_dict[t_count]["status"] = ticket.t_status.value

            tickets_dict[t_count]["branches"] = {}
            for b_count, branch in enumerate(ticket.branches):
                tickets_dict[t_count]["branches"][b_count] = {}
                tickets_dict[t_count]["branches"][b_count]['id'] = branch.id
                tickets_dict[t_count]["branches"][b_count]['name'] = branch.b_name
                tickets_dict[t_count]["branches"][b_count]['status'] = branch.b_status.value

    return tickets_dict


def get_single_ticket( ticket_code, user_id ):
    ticket = Ticket.get_ticket_by_code(ticket_code)

    if ticket is None or ticket.user_id != user_id:
        raise ValidationError("Invalid ticket")

    ticket_dict = {}
    if ticket:
        ticket_dict["id"] = ticket.id
        ticket_dict["code"] = ticket.t_code
        ticket_dict["description"] = ticket.t_description
        ticket_dict["status"] = ticket.t_status.value

    return ticket_dict


def update_ticket( old_code, user_id, new_code, new_description, new_status ):
    ticket = Ticket.get_ticket_by_code(old_code)

    if ticket is None or ticket.user_id != user_id:
        raise ValidationError("Invalid ticket")

    try:
        ticket.t_code = new_code
        ticket.t_description = new_description
        ticket.t_status = new_status
        ticket.validate()
    except ValueError as err:
        err = f"{err}"
        if err == "InvalidCode":
            raise ValidationError(f"Invalid Ticket Code")
        elif err == "InvalidDescription":
            raise ValidationError(f"Invalid Ticket Description")
        elif err == "InvalidStatus":
            raise ValidationError(f"Invalid Ticket Status")
        elif err == "DuplicateCode":
            raise DuplicationError(f"{ticket_number} already exists")

    db.session.commit()

    return True


def delete_ticket( code, user_id ):
    ticket = Ticket.get_ticket_by_code(code)

    if ticket is None or ticket.user_id != user_id:
        raise ValidationError("Invalid ticket")

    ticket.status = "inactive"

    for branch in ticket.branches:
        branch.status = "inactive"

    db.session.commit()

    return True


def add_branch( user_id, ticket_code, name, status ):
    ticket = Ticket.get_ticket_by_code(ticket_code)

    if ticket is None or ticket.user_id != user_id:
        raise ValidationError("Invalid ticket")

    try:
        new_branch = Branch()
        new_branch.ticket_id = ticket.id
        new_branch.b_name = name
        new_branch.b_status = status
        new_branch.validate()
    except ValueError as err:
        err = f"{err}"
        if err == "InvalidName":
            raise ValidationError(f"Invalid branch name")
        elif err == "InvalidStatus":
            raise ValidationError(f"Invalid branch status")
        elif err == "DuplicateBranch":
            raise DuplicationError(f"{name} already exists for this ticket")

    db.session.add(new_branch)
    db.session.commit()

    return new_branch.id


def get_all_branches( user_id, ticket_code ):
    ticket = Ticket.get_ticket_by_code(ticket_code)

    if ticket is None or ticket.user_id != user_id:
        raise ValidationError("Invalid ticket")

    branches = Branch.get_branches_by_ticket( ticket.id )

    branches_dict = {}

    if branches:
        for count, branch in enumerate(branches):
            branches_dict[count] = {}
            branches_dict[count]["id"] = branch.id
            branches_dict[count]["name"] = branch.b_name
            branches_dict[count]["status"] = branch.b_status.value

    return branches_dict


def update_branch( user_id, old_name, new_name, new_status ):
    branch = Branch.get_branch_by_name( old_name )

    is_valid_branch = branch is None or branch.ticket.user_id == user_id
    if not is_valid_branch:
        raise ValidationError("Invalid branch")

    try:
        branch.b_name = new_name
        branch.b_status = new_status
        branch.validate()
    except ValueError as err:
        err = f"{err}"
        if err == "InvalidName":
            raise ValidationError(f"Invalid branch name")
        elif err == "InvalidStatus":
            raise ValidationError(f"Invalid branch status")
        elif err == "DuplicateBranch":
            raise DuplicationError(f"{name} already exists for this ticket")

    db.session.commit()

    return True


def delete_branch( user_id, name ):
    branch = Branch.get_branch_by_name( name )

    is_valid_branch = branch is None or branch.ticket.user_id == user_id

    if not is_valid_branch:
        raise ValidationError("Invalid branch")

    branch.status = "inactive"

    db.session.commit()

    return True
