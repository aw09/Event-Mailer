from ..config import db

class Emails(db.Model):
    __tablename__ = 'emails'

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True, default=db.Sequence('id_seq'))
    event_id = db.Column(db.Integer, nullable=False)
    email_subject = db.Column(db.VARCHAR(255), nullable=False)
    email_content = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.TIMESTAMP, nullable=False)
    sent = db.Column(db.Boolean, default=0)