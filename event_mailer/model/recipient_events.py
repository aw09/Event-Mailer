from app import db

class RecipientEvent(db.Model):
    __tablename__ = 'recipient_events'
    recipient_id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, primary_key=True)
    recipient = db.relationship("Recipient", foreign_keys=[recipient_id])

    def __init__(self, recipient_id, event_id):
        self.recipient_id = recipient_id
        self.event_id = event_id

    def __repr__(self):
        return f'<RecipientEvent recipient_id={self.recipient_id} event_id={self.event_id}>'