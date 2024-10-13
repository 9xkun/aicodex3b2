import unittest
from app.models.task_model import Task

class TestTaskModel(unittest.TestCase):
    def test_task_properties(self):
        task = Task(id=1, name="Task 1", description="Description 1", priority="High", duedate="2022-01-01", user_id=1)
        self.assertEqual(task.id, 1)
        self.assertEqual(task.name, "Task 1")
        self.assertEqual(task.description, "Description 1")
        self.assertEqual(task.priority, "High")
        self.assertEqual(task.duedate, "2022-01-01")
        self.assertEqual(task.user_id, 1)

    def test_save_task(self):
        task = Task(id=1, name="Task 1", description="Description 1", priority="High", duedate="2022-01-01", user_id=1)
        saved_task = task.save()
        self.assertEqual(saved_task.id, 1)
        self.assertEqual(saved_task.name, "Task 1")
        self.assertEqual(saved_task.description, "Description 1")
        self.assertEqual(saved_task.priority, "High")
        self.assertEqual(saved_task.duedate, "2022-01-01")
        self.assertEqual(saved_task.user_id, 1)

    def test_get_task(self):
        task = Task.get(1)
        self.assertEqual(task.id, 1)
        self.assertEqual(task.name, "Task 1")
        self.assertEqual(task.description, "Description 1")
        self.assertEqual(task.priority, "High")
        self.assertEqual(task.duedate, "2022-01-01")
        self.assertEqual(task.user_id, 1)

    def test_update_task(self):
        task = Task.get(1)
        task.name = "Updated Task 1"
        task.save()
        updated_task = Task.get(1)
        self.assertEqual(updated_task.name, "Updated Task 1")

    def test_delete_task(self):
        task = Task.get(1)
        task.delete()
        deleted_task = Task.get(1)
        self.assertIsNone(deleted_task)

if __name__ == '__main__':
    unittest.main()