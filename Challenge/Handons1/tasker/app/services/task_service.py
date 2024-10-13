from app.models.task_model import Task

class TaskService:
    def create_task(self, name, description, priority, duedate, user_id):
        task = Task(name=name, description=description, priority=priority, duedate=duedate, user_id=user_id)
        task.save()
        return task

    def get_task(self, task_id):
        return Task.get_by_id(task_id)

    def get_all_tasks(self):
        return Task.get_all()

    def update_task(self, task_id, name=None, description=None, priority=None, duedate=None, user_id=None):
        task = Task.get_by_id(task_id)
        if task:
            if name:
                task.name = name
            if description:
                task.description = description
            if priority:
                task.priority = priority
            if duedate:
                task.duedate = duedate
            if user_id:
                task.user_id = user_id
            task.save()
            return task
        return None

    def delete_task(self, task_id):
        task = Task.get_by_id(task_id)
        if task:
            task.delete()
            return True
        return False