from app import db

class Branch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticket_id = db.Column(db.Integer, nullable=False)
    b_name = db.Column(db.String(20))
    b_status = db.Column(db.Enum('live', 'not_live',), default='not_live')
    status = db.Column(db.Enum('active', 'inactive'), default='active')
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f"<User {self.t_code}>"
