from app import db

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    t_code = db.Column(db.String(20), unique=True, nullable=False)
    t_description = db.Column(db.String(100))
    t_status = db.Column(db.Enum('pending', 'ongoing', 'done'), default='pending')
    status = db.Column(db.Enum('active', 'inactive'), default='active')
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f"<User {self.t_code}>"
