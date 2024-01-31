import enum
from app import db
from flask import current_app


class BranchStatus(enum.Enum):
    live = 'live'
    not_live = 'not_live'


class Branch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticket_id = db.Column(db.Integer, db.ForeignKey('ticket.id'), nullable=False)
    b_name = db.Column(db.String(20))
    b_status = db.Column(db.Enum(BranchStatus), default=BranchStatus.not_live.value)
    status = db.Column(db.Enum('active', 'inactive'), default='active')
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())


    def validate(self):
        self.b_name = self.b_name.strip()

        if not self.b_name:
            raise ValueError(f"InvalidName")

        if self.b_status:
            self.b_status = self.b_status.strip()

            if not self.b_status:
                self.b_status = None
            elif self.b_status not in BranchStatus.__members__:
                raise ValueError("InvalidStatus")

        branch = self.get_branch_by_name( self.b_name )

        is_duplicate_branch = branch is not None and branch.ticket.id == self.ticket_id

        if is_duplicate_branch:
            raise ValueError("DuplicateBranch")

        return self


    @staticmethod
    def get_branch_by_name(branch_name):
        with db.session.no_autoflush:
            return Branch.query.filter_by(b_name = branch_name, status = 'active').first()


    @staticmethod
    def get_branches_by_ticket(ticket_id):
        with db.session.no_autoflush:
            return Branch.query.filter_by(ticket_id = ticket_id, status = 'active').order_by(Branch.created_at.desc()).all()


    def __repr__(self):
        return f"<Branch {self.ticket_id}, {self.b_name}, {self.b_status.value}, {self.ticket_id}, {self.status}, {self.created_at}>"


from .ticket import Ticket
