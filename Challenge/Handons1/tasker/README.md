# Flask Task Manager

This is a task management system built with Flask and SQLite. It allows users to create, read, update, and delete tasks.

## Project Structure

```
flask-task-manager
├── app
│   ├── __init__.py
│   ├── controllers
│   │   └── task_controller.py
│   ├── models
│   │   └── task_model.py
│   ├── services
│   │   └── task_service.py
│   ├── templates
│   │   └── index.html
│   └── static
│       ├── css
│       │   └── styles.css
│       └── js
│           └── scripts.js
├── instance
│   └── config.py
├── migrations
│   └── README.md
├── tests
│   ├── test_task_controller.py
│   ├── test_task_model.py
│   └── test_task_service.py
├── .env
├── config.py
├── requirements.txt
└── README.md
```

## Files

### `app/__init__.py`

This file initializes the Flask application and sets up the database connection.

### `app/controllers/task_controller.py`

This file exports a class `TaskController` which handles the HTTP requests and responses for managing tasks. It includes methods for creating, reading, updating, and deleting tasks.

### `app/models/task_model.py`

This file exports a class `Task` which represents the task model. It includes properties for the task fields: id, name, description, priority, duedate, and user_id. It also includes methods for saving and retrieving tasks from the database.

### `app/services/task_service.py`

This file exports a class `TaskService` which provides the business logic for managing tasks. It interacts with the task model to perform CRUD operations on tasks.

### `app/templates/index.html`

This file is an HTML template for the task management system. It can be used to display the tasks in a web interface.

### `app/static/css/styles.css`

This file contains the CSS styles for the web interface.

### `app/static/js/scripts.js`

This file contains the JavaScript code for the web interface.

### `instance/config.py`

This file contains the configuration settings for the Flask application. It can be used to set up the database connection and other application-specific settings.

### `migrations/README.md`

This file provides information about the database migrations. It can be used to track and manage changes to the database schema.

### `tests/test_task_controller.py`

This file contains unit tests for the task controller. It can be used to ensure that the controller functions correctly.

### `tests/test_task_model.py`

This file contains unit tests for the task model. It can be used to ensure that the model functions correctly.

### `tests/test_task_service.py`

This file contains unit tests for the task service. It can be used to ensure that the service functions correctly.

### `.env`

This file is used to store environment variables for the project. It can be used to store sensitive information such as database credentials.

### `config.py`

This file contains the configuration settings for the project. It can be used to specify the database connection details and other project-specific settings.

### `requirements.txt`

This file lists the Python dependencies required for the project. It can be used to install the necessary packages using pip.

### `README.md`

This file contains the documentation for the project. It can be used to provide an overview of the project and instructions for setting it up and running it.