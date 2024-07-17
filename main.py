#!/usr/bin/env python3
from inventory import Inventory
import time

class InventoryApp:
    def __init__(self):
        self.inventory = Inventory()

    def display_menu(self):
        print()
        print("Healthcare Inventory Management System")
        print()
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")
        print()

    def get_item_details(self):
        name = input("Enter item name: ")
        quantity = int(input("Enter item quantity: "))
        supplier = input("Enter item supplier: ")
        expiry_date = input("Enter item expiry date (YYYY-MM-DD): ")
        return name, quantity, supplier, expiry_date

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                name, quantity, supplier, expiry_date = self.get_item_details()
                self.inventory.add_item(name, quantity, supplier, expiry_date)
                print("Item added successfully.")
            elif choice == '2':
                items = self.inventory.view_inventory()
                for item in items:
                    print(f"ID: {item.item_id}, Name: {item.name}, Quantity: {item.quantity}, Supplier: {item.supplier}, Expiry Date: {item.expiry_date}")
            elif choice == '3':
                item_id = int(input("Enter item ID to update: "))
                name = input("Enter new name (leave blank to keep current): ")
                quantity = input("Enter new quantity (leave blank to keep current): ")
                supplier = input("Enter new supplier (leave blank to keep current): ")
                expiry_date = input("Enter new expiry date (leave blank to keep current): ")
                self.inventory.update_item(item_id, name if name else None, int(quantity) if quantity else None, supplier if supplier else None, expiry_date if expiry_date else None)
                print("Item updated successfully.")
            elif choice == '4':
                item_id = int(input("Enter item ID to delete: "))
                self.inventory.delete_item(item_id)
                print("Item deleted successfully.")
            elif choice == '5':
                print("Closing application...")
                time.sleep(2)
                print("Goodbye!")
                self.inventory.close()
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = InventoryApp()
    app.run()

