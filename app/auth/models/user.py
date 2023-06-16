from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    u_username = db.Column(db.String(50), unique=True, nullable=False)
    u_password = db.Column(db.String(200), nullable=False)
    u_name = db.Column(db.String(50), nullable=False)
    u_secret = db.Column(db.String(15))
    status = db.Column(db.Enum('active', 'inactive'), default='active')
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f"<User {self.username}>"
