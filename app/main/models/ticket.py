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
    t_code = db.Column(db.String(20), unique=True, nullable=False)
    t_description = db.Column(db.String(100))
    t_status = db.Column(db.Enum(TicketStatus), default=TicketStatus.pending.value)
    status = db.Column(db.Enum('active', 'inactive'), default='active')
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    branches = db.relationship('Branch', backref='ticket', lazy=True)


    def save(self):
        self.t_code = self.t_code.strip()
        self.t_description = self.t_description.strip()

        if not self.t_code:
            raise ValueError(f"Ticket number is required.")
        if not self.t_description:
            raise ValueError(f"Ticket description is required")

        if self.t_status:
            self.t_status = self.t_status.strip()

            if not self.t_status:
                self.t_status = None
            elif self.t_status not in TicketStatus.__members__:
                raise ValueError("Invalid ticket status")

        ticket = self.get_ticket_by_code(self.t_code)

        if ticket:
            raise ValueError(f"{self.t_code} already exists")

        db.session.add(self)
        db.session.commit()
        return self


    @staticmethod
    def get_ticket_by_code(ticket_code):
        return Ticket.query.filter_by(t_code = ticket_code, status = "active").first()


    @staticmethod
    def get_user_tickets(user_id):
        return Ticket.query.filter_by(user_id = user_id, status = "active").all()


    @staticmethod
    def check_user_ticket(ticket_id, user_id):
        ticket = Ticket.query.filter_by(id = ticket_id).with_entities(Ticket.user_id).first()

        if ticket is None or ticket.user_id != user_id:
            return False

        return True


    def __repr__(self):
        return f"<Ticket {self.user_id}, {self.t_code}, {self.t_description}, {self.t_status}, {self.status}, {self.created_at}>"

from .branch import Branch

