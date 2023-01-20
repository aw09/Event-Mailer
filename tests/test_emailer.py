import os
import yagmail

from event_mailer import db
from event_mailer.emailer import run_schedule
from event_mailer.model import Emails, Recipients, RecipientEvents
from concurrent.futures import ThreadPoolExecutor
from event_mailer import app, db
import pytest
from datetime import datetime

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testing.db'
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()



def test_run_schedule_thread(client, mocker):
    os.environ['SENDER_EMAIL'] = 'sender@example.com'
    os.environ['OAUTH_FILE'] = 'oauth.json'
    os.environ['DB_FILE'] = 'testing.db'

    mocker.patch('yagmail.SMTP')
    yagmail.SMTP.return_value.send.return_value = None

    recipient1 = Recipients(email='recipient1@example.com')
    recipient2 = Recipients(email='recipient2@example.com')
    db.session.add(recipient1)
    db.session.add(recipient2)
    db.session.commit()

    event1 = Emails(event_id=1, email_subject='Test Subject', email_content='Test Content', timestamp=datetime.now(), sent=False)
    event2 = Emails(event_id=2, email_subject='Test Subject', email_content='Test Content', timestamp=datetime.now(), sent=False)
    db.session.add(event1)
    db.session.add(event2)
    db.session.commit()

    recipient_event1 = RecipientEvents(recipient_id=recipient1.id, event_id=1)
    recipient_event2 = RecipientEvents(recipient_id=recipient2.id, event_id=1)
    recipient_event3 = RecipientEvents(recipient_id=recipient1.id, event_id=2)
    db.session.add(recipient_event1)
    db.session.add(recipient_event2)
    db.session.add(recipient_event3)
    db.session.commit()

    with ThreadPoolExecutor() as executor:
        future = executor.submit(run_schedule, app)
        future.result()

    yagmail.SMTP.return_value.send.assert_any_call('recipient1@example.com', 'Test Subject', 'Test Content')
    yagmail.SMTP.return_value.send.assert_any_call('recipient2@example.com', 'Test Subject', 'Test Content')

    db.session.refresh(event1)
    db.session.refresh(event2)
    assert event1.sent == True
    assert event2.sent == True