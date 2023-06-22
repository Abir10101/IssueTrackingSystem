import enum
from app import db
from flask import current_app


class BranchStatus(enum.Enum):
    live = 'live'
    not_live = 'not_live'


class Branch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    b_name = db.Column(db.String(20))
    b_status = db.Column(db.Enum(BranchStatus), default=BranchStatus.not_live.value)
    status = db.Column(db.Enum('active', 'inactive'), default='active')
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    ticket_id = db.Column(db.Integer, db.ForeignKey('ticket.id'), nullable=False)


    def save(self, user_id):
        self.b_name = self.b_name.strip()

        if not self.b_name:
            raise ValueError(f"Branch name is required.")

        if self.b_status:
            self.b_status = self.b_status.strip()

            if not self.b_status:
                self.b_status = None
            elif self.b_status not in BranchStatus.__members__:
                raise ValueError("Invalid Branch status")

        branch = self.get_branch_by_name( self.b_name, self.ticket_id )

        if branch:
            raise ValueError(f"{self.b_name} already exists for this ticket.")

        is_user_ticket = Ticket.check_user_ticket( self.ticket_id, user_id )

        if not is_user_ticket:
            raise ValueError(f"Invalid Ticket id")

        db.session.add(self)
        db.session.commit()
        return self


    @staticmethod
    def get_branch_by_name(branch_name, ticket_id):
        return Branch.query.filter_by(ticket_id = ticket_id, b_name = branch_name, status = 'active').first()


    def __repr__(self):
        return f"<Branch {self.ticket_id}, {self.b_name}, {self.b_status}, {self.ticket_id}, {self.status}, {self.created_at}>"


from .ticket import Ticket
