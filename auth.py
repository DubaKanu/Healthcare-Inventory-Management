#!/bin/python3
from database import create_connection
import hashlib

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
