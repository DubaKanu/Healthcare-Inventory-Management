from database import create_connection

class Item:
    def __init__(self, item_id, name, quantity, supplier, expiry_date):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.supplier = supplier
        self.expiry_date = expiry_date

class Inventory:
    def __init__(self):
        self.connection = create_connection()

    def add_item(self, name, quantity, supplier, expiry_date):
        cursor = self.connection.cursor()
        cursor.execute("""
        INSERT INTO inventory (name, quantity, supplier, expiry_date)
        VALUES (?, ?, ?, ?)
        """, (name, quantity, supplier, expiry_date))
        self.connection.commit()

    def view_inventory(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM inventory")
        items = cursor.fetchall()
        return [Item(*item) for item in items]

    def update_item(self, item_id, name=None, quantity=None, supplier=None, expiry_date=None):
        cursor = self.connection.cursor()
        if name:
            cursor.execute("UPDATE inventory SET name = ? WHERE id = ?", (name, item_id))
        if quantity:
            cursor.execute("UPDATE inventory SET quantity = ? WHERE id = ?", (quantity, item_id))
        if supplier:
            cursor.execute("UPDATE inventory SET supplier = ? WHERE id = ?", (supplier, item_id))
        if expiry_date:
            cursor.execute("UPDATE inventory SET expiry_date = ? WHERE id = ?", (expiry_date, item_id))
        self.connection.commit()

    def delete_item(self, item_id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM inventory WHERE id = ?", (item_id,))
        self.connection.commit()

    def close(self):
        self.connection.close()

