import os

# Database configuration
DATABASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'app.db')
SQLALCHEMY_DATABASE_URI = f'sqlite:///{DATABASE}'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# App configuration
SECRET_KEY = 'your-secret-key'
DEBUG = True