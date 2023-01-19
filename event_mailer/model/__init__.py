from .emails import Emails
from .recipient import Recipients
from .recipient_events import RecipientEvents
from sqlalchemy.orm import class_mapper
import json

def serialize(model):
    """Serialize a SQLAlchemy model to a JSON-formatted string"""
    columns = [c.key for c in class_mapper(model.__class__).columns]
    dict_model = {c: getattr(model, c) for c in columns}
    return dict_model
    return json.loads(json.dumps(dict_model, default=str))
