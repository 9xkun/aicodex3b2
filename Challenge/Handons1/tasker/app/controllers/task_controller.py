from flask import Blueprint, request, jsonify
from app.models.task_model import Task

task_bp = Blueprint('task_api', __name__, url_prefix='/tasks')

@task_bp.route('/', methods=['GET'])
def get_tasks():
    tasks = Task.get_all_tasks()
    return jsonify(tasks)

@task_bp.route('/', methods=['POST'])
def create_task():
    data = request.get_json()
    task = Task.create_task(data)
    return jsonify(task)

@task_bp.route('/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.get_task_by_id(task_id)
    if task:
        return jsonify(task)
    else:
        return jsonify({'message': 'Task not found'}), 404

@task_bp.route('/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    task = Task.update_task(task_id, data)
    if task:
        return jsonify(task)
    else:
        return jsonify({'message': 'Task not found'}), 404

@task_bp.route('/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    result = Task.delete_task(task_id)
    if result:
        return jsonify({'message': 'Task deleted'})
    else:
        return jsonify({'message': 'Task not found'}), 404