import json
from datetime import datetime
from flask import Flask
from event_mailer.model import Emails, Recipients, RecipientEvents
from event_mailer import app, db
import pytest


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testing.db'
    client = app.test_client()

    with app.app_context():
        db.create_all()

        yield client

        db.drop_all()


def test_hello_world(client):
    response = client.get('/')
    assert b'Hello, World!' in response.data

def test_save_emails(client):
    data = {
        'event_id': 1,
        'email_subject': 'Test Subject',
        'email_content': 'Test Content',
        'timestamp': '01/01/23 00:00:00'
    }
    response = client.post('/save_emails', data=data)
    assert response.status_code == 200

    email = json.loads(response.data)
    assert email['event_id'] == 1
    assert email['email_subject'] == 'Test Subject'
    assert email['email_content'] == 'Test Content'
    assert email['timestamp'] == 'Sun, 01 Jan 2023 00:00:00 GMT'

def test_add_recipient(client):
    data = {'email': 'test@example.com'}
    response = client.post('/add_recipient', data=data)
    assert response.status_code == 200

    recipient = json.loads(response.data)
    assert recipient['email'] == 'test@example.com'

def test_assign_event(client):
    # Add recipient first
    data = {'email': 'test@example.com'}
    response = client.post('/add_recipient', data=data)
    recipient = json.loads(response.data)

    data = {
        'recipient_id': recipient['id'],
        'event_list': '1,2,3'
    }
    response = client.post('/assign_event', data=data)
    assert response.status_code == 200

    result = json.loads(response.data)
    assert result['recipient'] == 'test@example.com'
    assert result['event_list'] == ['1', '2', '3']
