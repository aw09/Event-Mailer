from ..config import db

class Emails(db.Model):
    __tablename__ = 'emails'

    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, nullable=False)
    email_subject = db.Column(db.NVARCHAR(255), nullable=False)
    email_content = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.TIMESTAMP, nullable=False)
    sent = db.Column(db.Boolean, default=0)