import unittest
from flask import Flask
from app.controllers.task_controller import TaskController

class TestTaskController(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.task_controller = TaskController(self.app.test_client())

    def test_get_all_tasks(self):
        response = self.task_controller.get_all_tasks()
        self.assertEqual(response.status_code, 200)

    def test_get_task(self):
        task_id = 1
        response = self.task_controller.get_task(task_id)
        self.assertEqual(response.status_code, 200)

    def test_create_task(self):
        task_data = {
            'name': 'Task 1',
            'description': 'This is task 1',
            'priority': 'High',
            'duedate': '2022-01-01',
            'user_id': 1
        }
        response = self.task_controller.create_task(task_data)
        self.assertEqual(response.status_code, 201)

    def test_update_task(self):
        task_id = 1
        task_data = {
            'name': 'Updated Task 1',
            'description': 'This is an updated task',
            'priority': 'Medium',
            'duedate': '2022-02-01',
            'user_id': 1
        }
        response = self.task_controller.update_task(task_id, task_data)
        self.assertEqual(response.status_code, 200)

    def test_delete_task(self):
        task_id = 1
        response = self.task_controller.delete_task(task_id)
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()