import unittest
import json
from flask import Flask
from app.controllers.user_controller import user_bp
from app.services.user_service import UserService

# tests/test_user_controller.py

class TestUserController(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(user_bp)
        self.client = self.app.test_client()
        self.app.testing = True

    def test_get_user(self):
        user_id = 1
        response = self.client.get(f'/users/{user_id}')
        self.assertEqual(response.status_code, 200)

    def test_get_all_users(self):
        response = self.client.get('/users')
        self.assertEqual(response.status_code, 200)

    def test_update_user(self):
        user_id = 1
        updated_user_data = {
            "name": "Jane Doe",
            "password": "newpassword123",
            "email": "jane.doe@example.com",
            "phone": "0912106112"
        }
        response = self.client.put(f'/users/{user_id}', data=json.dumps(updated_user_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_delete_user(self):
        user_id = 1
        response = self.client.delete(f'/users/{user_id}')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()