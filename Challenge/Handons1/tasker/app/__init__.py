# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flasgger import Swagger

db = SQLAlchemy()
migrate = Migrate()

def create_app(config = None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../instance/task_manager.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if config is not None:
        app.config.update(config)

    db.init_app(app)
    migrate.init_app(app, db)
    Swagger(app)  # Initialize Swagger

    # init routers
    # TODO: router.py
    from app.controllers.user_controller import user_bp
    from app.controllers.task_controller import task_bp
    app.register_blueprint(user_bp, url_prefix='/api')
    app.register_blueprint(task_bp, url_prefix='/api')

    @app.route('/')
    def index():
        return 'Welcome to the Task Manager'

    return app