import sqlite3

# Connect to the database
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Create the user table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS product(
        id INTEGER PRIMARY KEY,
        product_name TEXT NOT NULL,
        price INTEGER NOT NULL
    )
''')

# Insert data into the user table
cursor.execute("INSERT INTO product (product_name, price) VALUES (?, ?)", ("Product1", 12))

# Commit your changes
conn.commit()

# Close the connection
conn.close()