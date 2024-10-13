# repositories/user_repository.py
from app.models.user_model import User
from app import db


# Dummy services
class UserRepository:
    @staticmethod
    def add_user(user):
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def update_user(user):
        db.session.commit()

    @staticmethod
    def delete_user(user):
        db.session.delete(user)
        db.session.commit()