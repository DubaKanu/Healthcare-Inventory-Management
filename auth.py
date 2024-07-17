#!/bin/python3
from database import create_connection
import hashlib

#cursor = self.connection.cursor() - This line creates a cursor object, which is used to interact with the database and execute queries.
#hashed_password = hashlib.sha256(password.encode()).hexdigest() - This line creates a hashed version of the provided password.

class Auth:
    def __init__(self):
        self.connection = create_connection()

    def register_user(self, username, password):
        cursor = self.connection.cursor()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        cursor.execute("""
        INSERT INTO users (username, password)
        VALUES (?, ?)
        """, (username, hashed_password))
        self.connection.commit()

    def login_user(self, username, password):
        cursor = self.connection.cursor()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hashed_password))
        user = cursor.fetchone()
        return user is not None

    def close(self):
        self.connection.close()
