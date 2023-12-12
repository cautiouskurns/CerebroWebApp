import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Execute a query
cursor.execute("SELECT * FROM product")

# Fetch and display the data
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
conn.close()