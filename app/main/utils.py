from flask import current_app
from app import db
from sqlalchemy.exc import IntegrityError
from .models.ticket import Ticket
from .models.branch import Branch


# functions
def health_check():
    from sqlalchemy import text

    query = text("SELECT 1;")
    with db.engine.connect() as connection:
        result = connection.execute( query )

    return


def add_ticket( user_id, ticket_number, ticket_description, ticket_status ):
    new_ticket = Ticket()
    new_ticket.user_id = user_id
    new_ticket.t_code = ticket_number
    new_ticket.t_description = ticket_description
    new_ticket.t_status = ticket_status
    ticket = new_ticket.save()

    return ticket.id


# def get_all_tickets( user_id ):
#     tickets = Ticket.get_user_tickets( user_id )
#     return tickets


# def get_single_ticket( ticket_id ):
#     con = db_connection()
#     cur = con.cursor()
#     try:
#         is_user_ticket = check_user_ticket( con, ticket_id, user_id )
#         if is_user_ticket:
#             cur.execute(
#                 "SELECT * FROM tickets WHERE id = %s;",
#                 (ticket_id,)
#             )
#             ticket = cur.fetchone()
#         else:
#             raise Exception("Invalid ticket id")
#     except Exception as err:
#         raise Exception(err)
#     finally:
#         cur.close()
#         con.close()
#     return ticket


# def update_ticket( ticket_id, ticket_code, ticket_description, ticket_status ):
#     con = db_connection()
#     cur = con.cursor()
#     if ticket_status not in TICKET_STATUS_TUPLE:
#         raise Exception("Invalid Status")
#     try:
#         is_user_ticket = check_user_ticket( con, ticket_id, user_id )
#         if is_user_ticket:
#             cur.execute(
#                 "UPDATE tickets SET t_code = %s, t_description = %s, t_status = %s WHERE id = %s;",
#                 (ticket_code, ticket_description, ticket_status, ticket_id)
#             )
#             con.commit()
#         else:
#             raise Exception("Invalid ticket id")
#     except pymysql.err.IntegrityError:
#         con.rollback()
#         raise Exception(f"Ticket {ticket_code} already exists")
#     finally:
#         cur.close()
#         cur.close()
#     return True


# def delete_ticket( ticket_id ):
#     con = db_connection()
#     cur = con.cursor()
#     try:
#         is_user_ticket = check_user_ticket( con, ticket_id, user_id )
#         if is_user_ticket:
#             cur.execute(
#                 "DELETE FROM tickets WHERE id = %s;",
#                 (ticket_id,)
#             )
#             cur.execute(
#                 "DELETE FROM branches WHERE ticket_id = %s;",
#                 (ticket_id,)
#             )
#             con.commit()
#         else:
#             raise Exception("Invalid ticket id")
#     except Exception as err:
#         con.rollback()
#         raise Exception(err)
#     finally:
#         cur.close()
#         con.close()
#     return True


def add_branch( user_id, ticket_id, name, status ):
    new_branch = Branch()
    new_branch.ticket_id = ticket_id
    new_branch.b_name = name
    new_branch.b_status = status
    branch = new_branch.save(user_id)

    return branch.id


# def get_all_branches( user_id, ticket_id ):
#     con = db_connection()
#     cur = con.cursor()
#     try:
#         is_user_ticket = check_user_ticket( con, ticket_id, user_id )
#         if is_user_ticket:
#             cur.execute(
#                 "SELECT id, b_name, b_status FROM branches WHERE ticket_id = %s;",
#                 (ticket_id,)
#             )
#             branches = cur.fetchall()
#         else:
#             raise Exception("Invalid ticket id")
#     except Exception as err:
#         raise Exception(err)
#     finally:
#         cur.close()
#         con.close()
#     return branches


# def update_branch( branch_id, branch_name, branch_status ):
#     con = db_connection()
#     cur = con.cursor()
#     if branch_status not in BRANCH_STATUS_TUPLE:
#         raise Exception("Invalid Status")
#     try:
#         cur.execute(
#             "UPDATE branches SET b_name = %s, b_status = %s WHERE id = %s;",
#             (branch_name, branch_status, branch_id,)
#         )
#         con.commit()
#     except pymysql.err.IntegrityError:
#         con.rollback()
#         raise Exception(f"Branch {branch_name} already exists")
#     finally:
#         cur.close()
#         con.close()
#     return True


# def delete_branch( branch_id ):
#     con = db_connection()
#     cur = con.cursor()
#     try:
#         cur.execute(
#             "DELETE FROM branches WHERE id = %s;",
#             (branch_id,)
#         )
#         con.commit()
#     except Exception as err:
#         con.rollback()
#         raise Exception(err)
#     finally:
#         cur.close()
#         con.close()
#     return True


# def check_user_ticket( dbcon :pymysql.connections.Connection, ticket_id :int, user_id :int ) -> bool:
#     cur = dbcon.cursor()
#     cur.execute(
#         "SELECT user_id from tickets WHERE id = %s;",
#         (ticket_id)
#     )
#     ticket_user_id = cur.fetchone()['user_id']
#     if user_id != ticket_user_id:
#         return False
#     else:
#         return True
