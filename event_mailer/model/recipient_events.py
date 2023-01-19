from ..config import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

class RecipientEvents(db.Model):
    __tablename__ = 'recipient_events'
    recipient_id = Column(Integer, db.ForeignKey("recipients.id"),  primary_key=True)
    event_id = Column(Integer, primary_key=True)
    recipient = relationship("Recipients", foreign_keys=[recipient_id])

    def __init__(self, recipient_id, event_id):
        self.recipient_id = recipient_id
        self.event_id = event_id

    def __repr__(self):
        return f'<RecipientEvent recipient_id={self.recipient_id} event_id={self.event_id}>'