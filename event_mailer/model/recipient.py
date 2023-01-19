from ..config import db

class Recipients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Unicode(255), unique=True, nullable=False)