import unittest

from app import create_app, db

# tests/basetest.py
class BaseTestController(unittest.TestCase):
    def setUp(self):
        # python server
        config = {
            'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
            # 'SQLALCHEMY_DATABASE_URI': 'sqlite:///../instance/task_tests.db',
            'SQLALCHEMY_TRACK_MODIFICATIONS': False,
            'TESTING': True
        }
        self.app = create_app(config)

        with self.app.app_context():
            db.create_all()

        # TODO: populate data

        # python browser
        self.client = self.app.test_client()
        self.app.testing = True

    # teardown
    def tearDown(self):
        with self.app.app_context():
            db.drop_all()
