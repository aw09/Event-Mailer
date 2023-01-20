import sqlite3
from dotenv import load_dotenv
import os

load_dotenv()

DB_FILE = os.getenv('DB_FILE')

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect(DB_FILE)

# Open the SQL file
with open('schema.sql', 'r') as f:
    sql = f.read()

# Execute the SQL
conn.executescript(sql)

# Save the changes and close the connection
conn.commit()
conn.close()
