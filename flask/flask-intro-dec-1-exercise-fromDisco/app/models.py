from . import db
from sqlalchemy.orm import declared_attr
from werkzeug.security import generate_password_hash, check_password_hash

# TODO: Add a User model with username and password.
# When the user is saved to the database, the password should not be stored as clear text
# Find out how to safely store passwords in databases in applications built with Flask


class Reminder(db.Model):
    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "user_id": self.user_id,
        }


class User(db.Model):
    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    contributions = db.relationship("Reminder", backref="user")

    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password_hash,
            "contributions": [
                contribution.to_json() for contribution in self.contributions
            ],
        }

    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password_hash(self, password):
        return check_password_hash(self.password, password)
