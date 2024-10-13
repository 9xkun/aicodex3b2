# services/user_service.py
from app.models.user_model import User
from app.repositories.user_repository import UserRepository

# Smart services
class UserService:
    """
    Creates a new user with the provided details.
    Args:
        name (str): The name of the user, required.
        password (str): The password for the user, optional (default: random)
        email (str): The email address of the user, required (send email)
        phone (str): The phone number of the user, optional (default: None)
    Returns:
        User: The newly created user object.
    # Example usage:
    # user_service = UserService()
    # new_user = user_service.create_user("John Doe", "password123", "john.doe@example.com", "123-456-7890")
    # new_user = user_service.create_user("Jane", None, "hoang@mail.com", None)
    # print(new_user)
    """
    @staticmethod
    def create_user(name, password, email, phone):
        new_user = User(name=name, password=password, email=email, phone=phone)
        UserRepository.add_user(new_user)

        # send email to user_email

        # sync user to firebase

        return new_user

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)
        return UserRepository.get_user_by_id(user_id)
    @staticmethod
    def get_all_users():
        return User.query.all()
        return UserRepository.get_all_users()
    @staticmethod
    def update_user(user_id, name=None, password=None, email=None, phone=None):
        user = User.query.get(user_id)
        if user:
            if name:
                user.name = name
            if password:
                user.password = password
            if email:
                user.email = email
            if phone:
                user.phone = phone
            db.session.commit()
        return user

    @staticmethod
    def delete_user(user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            UserRepository.delete_user(user)
