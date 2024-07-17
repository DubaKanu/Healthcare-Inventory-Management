#!/bin/python3
from database import create_connection

class ReportGenerator:
    def __init__(self):
        self.connection = create_connection()

    def generate_inventory_summary(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM inventory")
        return cursor.fetchall()

    def generate_low_stock_alert(self, threshold=50):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM inventory WHERE quantity < ?", (threshold,))
        return cursor.fetchall()

    def generate_supplier_list(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM suppliers")
        return cursor.fetchall()

    def close(self):
        self.connection.close()
