import time
from datetime import datetime
import pytz
import yagmail
import os
from dotenv import load_dotenv

def run_schedule(app):
    load_dotenv()

    SENDER_EMAIL = os.getenv('SENDER_EMAIL')
    OAUTH_FILE = os.getenv('OAUTH_FILE')

    with app.app_context():
        from .model import Emails, Recipients, RecipientEvents, serialize
        from .config import db, q

        def send_email(email):
            receivers = db.session.query(Recipients.email).join(RecipientEvents).filter(
                RecipientEvents.recipient_id == Recipients.id,
                RecipientEvents.event_id == email.event_id).all()
            receivers = [i[0] for i in receivers]

            yag = yagmail.SMTP(SENDER_EMAIL, oauth2_file=OAUTH_FILE)
            for receiver in receivers:
                yag.send(receiver,email.email_subject , email.email_content)

            email.sent = True
            db.session.commit()



        def run():
            stop_schedule = False
            emails = db.session.query(Emails).filter(Emails.sent == False).all()

            # Add the emails and timestamps to the queue
            for email in emails:
                q.put((email.timestamp, email.id, email))

            while True:
                sent = False
                if not q.empty():
                    timestamp, id, email_data = q.get()

                    # Assume timestamp of the event is Asia/Singapore
                    current_time = datetime.now(pytz.timezone(
                        "Asia/Singapore")).replace(tzinfo=None)
                    if current_time >= timestamp:
                        # Send the email
                        send_email(email_data)
                        sent = True
                    else:
                        q.put((timestamp, id, email_data))
                
                if not sent and stop_schedule:
                    break

                if app.config['TESTING']:
                    stop_schedule = True

                # If not sent check other email
                if not sent:
                    time.sleep(60)
        
        run()


