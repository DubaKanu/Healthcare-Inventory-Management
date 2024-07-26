import sqlite3

def create_connection():
 # Connect to the SQLite database file named 'inventory.db'   
    connection = sqlite3.connect("inventory.db")
    return connection

def create_tables():
 # Get a connection to the database   
    connection = create_connection()
    cursor = connection.cursor()

# SQL command to create the 'inventory' table if it doesn't already exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        supplier TEXT NOT NULL,
        expiry_date TEXT NOT NULL
    )
    """)

    connection.commit()
    connection.close()

# Create the table when the module is imported
create_tables()
