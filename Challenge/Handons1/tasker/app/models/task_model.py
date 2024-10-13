from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    priority = db.Column(db.Integer, nullable=False)
    duedate = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

    def __init__(self, name, description, priority, duedate, user_id):
        self.name = name
        self.description = description
        self.priority = priority
        self.duedate = duedate
        self.user_id = user_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Task.query.all()

    @staticmethod
    def get_by_id(task_id):
        return Task.query.get(task_id)

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()