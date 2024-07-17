#!/bin/python3
from database import create_connection

class Supplier:
    def __init__(self, supplier_id, name, contact, email):
        self.supplier_id = supplier_id
        self.name = name
        self.contact = contact
        self.email = email

class SupplierManager:
    def __init__(self):
        self.connection = create_connection()

    def add_supplier(self, name, contact, email):
        cursor = self.connection.cursor()
        cursor.execute("""
        INSERT INTO suppliers (name, contact, email)
        VALUES (?, ?, ?)
        """, (name, contact, email))
        self.connection.commit()

    def view_suppliers(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM suppliers")
        suppliers = cursor.fetchall()
        return [Supplier(*supplier) for supplier in suppliers]

    def update_supplier(self, supplier_id, name=None, contact=None, email=None):
        cursor = self.connection.cursor()
        if name:
            cursor.execute("UPDATE suppliers SET name = ? WHERE id = ?", (name, supplier_id))
        if contact:
            cursor.execute("UPDATE suppliers SET contact = ? WHERE id = ?", (contact, supplier_id))
        if email:
            cursor.execute("UPDATE suppliers SET email = ? WHERE id = ?", (email, supplier_id))
        self.connection.commit()

    def delete_supplier(self, supplier_id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM suppliers WHERE id = ?", (supplier_id,))
        self.connection.commit()

    def close(self):
        self.connection.close()
