import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('database.db')

# Open the SQL file
with open('schema.sql', 'r') as f:
    sql = f.read()

# Execute the SQL
conn.executescript(sql)

# Save the changes and close the connection
conn.commit()
conn.close()
