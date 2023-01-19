from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import queue


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database.db'
db = SQLAlchemy(app)

q = queue.PriorityQueue()