from flask import request, jsonify, abort

from .config import app, db, q
from .model import Emails, Recipients, RecipientEvents, serialize
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
    db.session.refresh(new_email)

    # Add to queue
    q.put((new_email.timestamp, new_email.id, new_email))

    return jsonify(serialize(new_email))

@app.route("/add_recipient", methods=["POST"])
def add_recipient():
    email = request.form.get('email')

    new_recipient = Recipients(email=email)

    db.session.add(new_recipient)
    db.session.commit()
    db.session.refresh(new_recipient)

    return jsonify(serialize(new_recipient))

@app.route("/assign_event", methods=["POST"])
def assign_event():
    id = request.form.get('recipient_id')
    events = request.form.get('event_list').split(',')

    recipient = db.session.query(Recipients).get(id)
    if not recipient:
        return "Recipient ID not found", 404

    new_list_recipient_event = []
    for event in events:
        new_recipient_event = RecipientEvents(
            recipient_id=id,
            event_id=event
        )
        new_list_recipient_event.append(new_recipient_event)

    db.session.add_all(new_list_recipient_event)
    db.session.commit()

    
    return jsonify({
        "recipient": recipient.email,
        "event_list": events
    })
    




with app.app_context():
    from threading import Thread
    from .emailer import run_schedule

    thread = Thread(target = run_schedule, args=(app,))
    thread.start()
