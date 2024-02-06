import secrets
import werkzeug.security as _ws
import re
from app import db
from flask import current_app
import json


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    u_email = db.Column(db.String(50), unique=True, nullable=False)
    u_password = db.Column(db.String(200), nullable=False)
    u_name = db.Column(db.String(50), nullable=False)
    u_secret = db.Column(db.String(15))
    status = db.Column(db.Enum('active', 'inactive'), default='active')
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())


    def validate(self):
        self.u_email = self.u_email.strip()
        self.u_password = self.u_password.strip()
        self.u_name = self.u_name.strip()

        if not self.u_email or not self.__is_valid_email():
            raise ValueError("InvalidEmail")
        if not self.u_password:
            raise ValueError("InvalidPassword")
        if not self.u_name:
            raise ValueError("InvalidName")

        user = self.get_user_by_email( self.u_email )

        if user:
            raise ValueError("UserExists")

        is_password_hashed = self.u_password.endswith("$HASHED$")
        if not is_password_hashed:
            self.hash_password( self.u_password )

        return self


    def hash_password(self, password):
        self.u_secret = secrets.token_urlsafe(10)
        self.u_password = _ws.generate_password_hash( password )
        self.u_password += "$HASHED$"


    @staticmethod
    def get_user_by_email(email):
        return User.query.filter_by( u_email = email, status = 'active').first()


    @staticmethod
    def check_password(provided_password, hashed_password):
        hashed_password = hashed_password[:-len("$HASHED$")]
        return _ws.check_password_hash( hashed_password, provided_password )


    def refresh_secret(self):
        self.u_secret = secrets.token_urlsafe(10)
        db.session.commit()
        return True

    def __is_valid_email(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        return re.fullmatch(regex, self.u_email)

    def to_json(self):
        return json.dumps({
            "email": self.u_email,
            "name": self.u_name,
        })


    def __repr__(self):
        return f"<User {self.u_email}, {self.u_password}, {self.u_name}, {self.status}, {self.created_at}>"
