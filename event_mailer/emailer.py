import time
from datetime import datetime
import pytz


def run_schedule(app):
    with app.app_context():
        from .model import Emails, Recipients, RecipientEvents, serialize
        from .config import db, q

        def send_email(email):
            print(f"Send Email {serialize(email)}")

        def run():
            emails = db.session.query(Emails).all()

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

                # If not sent check other email
                if not sent:
                    time.sleep(60)
        
        run()


