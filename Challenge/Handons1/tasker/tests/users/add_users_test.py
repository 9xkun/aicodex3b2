import unittest
import json

from tests.basttest import BaseTestController

# tests/test_user_controller.py
class TestUserController(BaseTestController):

    # test create user
    def test_create_user(self):
        user_data = {
            "name": "John Doe",
            "password": "password123",
            "email": "john.doe@example.com",
            "phone": "0912106111"
        }

        response = self.client.post('/api/users', data=json.dumps(user_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone(response.data)

    
    def test_create_user_invalid_email(self):
        user_data = {
            "name": "John Doe",
            "password": "password123",
            "email": "john.doe@invalid",
            "phone": "0912106111"
        }

        response = self.client.post('/api/users', data=json.dumps(user_data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid email format', response.get_json()['message'])

    def test_create_user_invalid_phone_length(self):
        user_data = {
            "name": "John Doe",
            "password": "password123",
            "email": "john.doe@example.com",
            "phone": "0912"
        }
        response = self.client.post('/api/users', data=json.dumps(user_data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid phone length', response.get_json()['message'])

    def test_create_user_invalid_name_length_smaller(self):
        user_data = {
            "name": "J",
            "password": "password123",
            "email": "john.doe@example.com",
            "phone": "0912106111"
        }
        response = self.client.post('/api/users', data=json.dumps(user_data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Name must be between 6 and 50 characters', response.get_json()['message'])

    def test_create_user_invalid_name_length_bigger(self):
        user_data = {
            "name": "J" * 100,
            "password": "password123",
            "email": "john.doe@example.com",
            "phone": "0912106111"
        }

        response = self.client.post('/api/users', data=json.dumps(user_data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Name must be between 6 and 50 characters', response.get_json()['message'])

    def test_create_user_invalid_password_length(self):
        user_data = {
            "name": "John Doe",
            "password": "pass",
            "email": "john.doe@example.com",
            "phone": "0912106111"
        }
        response = self.client.post('/api/users', data=json.dumps(user_data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid password length', response.get_json()['message'])

    def test_create_user_email_unique(self):
        user_data = {
            "name": "John Doe",
            "password": "password123",
            "email": "john.doe@example.com",
            "phone": "0912106111"
        }
        self.client.post('/api/users', data=json.dumps(user_data), content_type='application/json')
        response = self.client.post('/api/users', data=json.dumps(user_data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Email already exists', response.get_json()['message'])

    def test_create_user_phone_unique(self):
        user_data = {
            "name": "John Doe",
            "password": "password123",
            "email": "john.doe@example.com",
            "phone": "0912106111"
        }
        self.client.post('/api/users', data=json.dumps(user_data), content_type='application/json')
        user_data["email"] = "john.doe2@example.com"
        response = self.client.post('/api/users', data=json.dumps(user_data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Phone number already exists', response.get_json()['message'])    

if __name__ == "__main__":
    unittest.main()