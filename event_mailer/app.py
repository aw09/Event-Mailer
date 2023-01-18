from flask import request

from .config import app, db
from .model.emails import Emails
from datetime import datetime

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/save_emails", methods=['POST'])
def save_emails():
    event_id = request.form.get('event_id')
    email_subject = request.form.get('email_subject')
    email_content = request.form.get('email_content')
    timestamp = request.form.get('timestamp')

    new_email = Emails(
        event_id=event_id,
        email_subject=email_subject,
        email_content=email_content,
        timestamp=datetime.strptime(timestamp, '%m/%d/%y %H:%M:%S')

    )
    db.session.add(new_email)
    db.session.commit()

    # TODO: Add to queue
    return "Success"