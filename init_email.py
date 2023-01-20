import yagmail
from dotenv import load_dotenv
import os

load_dotenv()

SENDER_EMAIL = os.getenv('SENDER_EMAIL')
OAUTH_FILE = os.getenv('OAUTH_FILE')

yag = yagmail.SMTP(SENDER_EMAIL, oauth2_file=OAUTH_FILE)
yag.send(subject="Great!")
