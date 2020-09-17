from flask_sqlalchemy import SQLAlchemy

from .views import app

# Create database connection object
db = SQLAlchemy(app)

class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #description = db.Column(db.String(200), nullable=False)
    accuracy = db.Column(db.Float(), nullable=False)

    def __init__(self, accuracy):
            self.accuracy = accuracy

db.create_all()