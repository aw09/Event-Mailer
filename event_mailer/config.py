from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import queue
from dotenv import load_dotenv
import os


load_dotenv()

DB_FILE = os.getenv('DB_FILE')
CWD = os.getcwd()


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{CWD}/{DB_FILE}'
db = SQLAlchemy(app)

q = queue.PriorityQueue()