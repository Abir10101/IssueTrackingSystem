import enum
from app import db
from flask import current_app


class TicketStatus(enum.Enum):
    pending = 'pending'
    ongoing = 'ongoing'
    done = 'done'


class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    t_code = db.Column(db.Integer, nullable=False)
    t_description = db.Column(db.String(100))
    t_status = db.Column(db.Enum(TicketStatus), default=TicketStatus.pending.value)
    status = db.Column(db.Enum('active', 'inactive'), default='active')
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    branches = db.relationship('Branch', backref='ticket', lazy=True)


    def validate(self):
        self.t_code = str(self.t_code).strip()
        self.t_description = str(self.t_description).strip()

        if not self.t_code:
            raise ValueError(f"InvalidCode")
        if not self.t_description:
            raise ValueError(f"InvalidDescription")

        if self.t_status:
            self.t_status = self.t_status.strip()

            if not self.t_status:
                self.t_status = None
            elif self.t_status not in TicketStatus.__members__:
                raise ValueError("InvalidStatus")

        try:
            self.t_code = int(self.t_code)
        except ValueError:
            raise ValueError(f"InvalidCode")

        ticket = self.get_ticket_by_code(self.t_code)

        if self.id is None:
            # inserting a ticket
            if ticket:
                raise ValueError("DuplicateCode")
        else:
            # updating a ticket
            if ticket.id != self.id:
                raise ValueError("DuplicateCode")

        return self


    @staticmethod
    def get_ticket_by_code(ticket_code):
        with db.session.no_autoflush:
            return Ticket.query.filter_by(t_code = ticket_code, status = "active").first()


    @staticmethod
    def get_user_tickets(user_id):
        with db.session.no_autoflush:
            return Ticket.query.filter_by(user_id = user_id, status = "active").order_by(Ticket.created_at.desc()).all()


    def __repr__(self):
        return f"<Ticket {self.user_id}, {self.t_code}, {self.t_description}, {self.t_status.value}, {self.status}, {self.created_at}>"

from .branch import Branch

