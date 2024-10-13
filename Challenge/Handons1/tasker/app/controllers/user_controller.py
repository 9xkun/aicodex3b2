# controllers/user_controller.py
from flask import Blueprint, request, jsonify
from app.services.user_service import UserService
from app.utils.stringvalidator import StringValidator
from flasgger import swag_from
import re

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['POST'])
@swag_from({
    'responses': {
        201: {
            'description': 'User created successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {
                        'type': 'integer'
                    }
                }
            }
        }
    },
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {
                        'type': 'string'
                    },
                    'password': {
                        'type': 'string'
                    },
                    'email': {
                        'type': 'string'
                    },
                    'phone': {
                        'type': 'string'
                    }
                },
                'required': ['name', 'password', 'email', 'phone']
            }
        }
    ]
})
def create_user():
    data = request.get_json()

    # vaildate name < 80 characters
    if len(data['name']) > 80:
        return jsonify({'message': 'Name must be less than 80 characters'}), 400

    # validate password > 8 characters < 50
    if len(data['password']) < 8 or len(data['password']) > 50:
        return jsonify({'message': 'Password must be between 8 and 50 characters'}), 400
    
    # validate email < 120 characters

    # validate email format
    if not StringValidator.validate_email_format(data['email']):
        return jsonify({'message': 'Invalid email format'}), 400

    # validate phone format
    # example: 0912106111 -> true
    # example: 091210611 -> false
    if len(data['phone']) != 10:
        return jsonify({'message': 'Phone number must be 10 characters'}), 400

    user = UserService.create_user(data['name'], data['password'], data['email'], data['phone'])
    return jsonify(user.id), 201

@user_bp.route('/users/<int:user_id>', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'User retrieved successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {
                        'type': 'integer'
                    },
                    'name': {
                        'type': 'string'
                    },
                    'email': {
                        'type': 'string'
                    },
                    'phone': {
                        'type': 'string'
                    }
                }
            }
        },
        404: {
            'description': 'User not found'
        }
    }
})
def get_user(user_id):
    user = UserService.get_user_by_id(user_id)
    if user:
        return jsonify({
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'phone': user.phone
        })
    return jsonify({'message': 'User not found'}), 404

@user_bp.route('/users', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'Users retrieved successfully',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {
                            'type': 'integer'
                        },
                        'name': {
                            'type': 'string'
                        },
                        'email': {
                            'type': 'string'
                        },
                        'phone': {
                            'type': 'string'
                        }
                    }
                }
            }
        }
    }
})
def get_all_users():
    users = UserService.get_all_users()
    return jsonify([{
        'id': user.id,
        'name': user.name,
        'email': user.email,
        'phone': user.phone
    } for user in users])

@user_bp.route('/users/<int:user_id>', methods=['PUT'])
@swag_from({
    'responses': {
        200: {
            'description': 'User updated successfully'
        },
        404: {
            'description': 'User not found'
        }
    },
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {
                        'type': 'string'
                    },
                    'password': {
                        'type': 'string'
                    },
                    'email': {
                        'type': 'string'
                    },
                    'phone': {
                        'type': 'string'
                    }
                }
            }
        }
    ]
})
def update_user(user_id):
    data = request.get_json()
    user = UserService.update_user(user_id, data.get('name'), data.get('password'), data.get('email'), data.get('phone'))
    if user:
        return jsonify({'message': 'User updated successfully'})
    return jsonify({'message': 'User not found'}), 404

@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
@swag_from({
    'responses': {
        200: {
            'description': 'User deleted successfully'
        },
        404: {
            'description': 'User not found'
        }
    }
})
def delete_user(user_id):
    user = UserService.delete_user(user_id)
    if user:
        return jsonify({'message': 'User deleted successfully'})
    return jsonify({'message': 'User not found'}), 404