#!/usr/bin/env python3

import os
from inventory import Inventory
from supplier import SupplierManager
from reports import ReportGenerator
from auth import Auth

class InventoryApp:
    def __init__(self):
        self.inventory = Inventory()
        self.supplier_manager = SupplierManager()
        self.report_generator = ReportGenerator()
        self.auth = Auth()
        self.current_user = None

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_header(self, title):
        print("=" * 50)
        print(f"{title:^50}")
        print("=" * 50)

    def display_menu(self):
        self.clear_screen()
        self.print_header("Healthcare Inventory Management System")
        if not self.current_user:
            print("1. Login")
            print("2. Register")
            print("3. Exit")
        else:
            print(f"Logged in as: {self.current_user}")
            print("1. Add Item")
            print("2. View Inventory")
            print("3. Update Item")
            print("4. Delete Item")
            print("5. Manage Suppliers")
            print("6. Generate Reports")
            print("7. Logout")
            print("8. Exit")

    def get_item_details(self):
        name = input("Enter item name: ")
        quantity = int(input("Enter item quantity: "))
        supplier = input("Enter item supplier: ")
        expiry_date = input("Enter item expiry date (YYYY-MM-DD): ")
        return name, quantity, supplier, expiry_date
    
    def get_supplier_details(self):
        name = input("Enter supplier name: ")
        contact = input("Enter supplier contact: ")
        email = input("Enter supplier email: ")
        return name, contact, email

    def manage_suppliers(self):
        while True:
            self.clear_screen()
            self.print_header("Supplier Management")
            print("1. Add Supplier")
            print("2. View Suppliers")
            print("3. Update Supplier")
            print("4. Delete Supplier")
            print("5. Return to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                name, contact, email = self.get_supplier_details()
                self.supplier_manager.add_supplier(name, contact, email)
                print("Supplier added successfully.")
            elif choice == '2':
                suppliers = self.supplier_manager.view_suppliers()
                for supplier in suppliers:
                    print(f"ID: {supplier.supplier_id}, Name: {supplier.name}, Contact: {supplier.contact}, Email: {supplier.email}")
            elif choice == '3':
                supplier_id = int(input("Enter supplier ID to update: "))
                name = input("Enter new name (leave blank to keep current): ")
                contact = input("Enter new contact (leave blank to keep current): ")
                email = input("Enter new email (leave blank to keep current): ")
                self.supplier_manager.update_supplier(supplier_id, name if name else None, contact if contact else None, email if email else None)
                print("Supplier updated successfully.")
            elif choice == '4':
                supplier_id = int(input("Enter supplier ID to delete: "))
                self.supplier_manager.delete_supplier(supplier_id)
                print("Supplier deleted successfully.")
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")
            input("\nPress Enter to continue...")

    def generate_reports(self):
        while True:
            self.clear_screen()
            self.print_header("Report Generation")
            print("1. Inventory Summary")
            print("2. Low Stock Alert")
            print("3. Supplier List")
            print("4. Return to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                report = self.report_generator.generate_inventory_summary()
                print("\nInventory Summary:")
                for item in report:
                    print(f"ID: {item[0]}, Name: {item[1]}, Quantity: {item[2]}, Supplier: {item[3]}, Expiry Date: {item[4]}")
            elif choice == '2':
                threshold = int(input("Enter low stock threshold: "))
                report = self.report_generator.generate_low_stock_alert(threshold)
                print("\nLow Stock Alert:")
                for item in report:
                    print(f"ID: {item[0]}, Name: {item[1]}, Quantity: {item[2]}, Supplier: {item[3]}, Expiry Date: {item[4]}")
            elif choice == '3':
                report = self.report_generator.generate_supplier_list()
                print("\nSupplier List:")
                for supplier in report:
                    print(f"ID: {supplier[0]}, Name: {supplier[1]}, Contact: {supplier[2]}, Email: {supplier[3]}")
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")
            input("\nPress Enter to continue...")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if not self.current_user:
                if choice == '1':
                    username = input("Enter username: ")
                    password = input("Enter password: ")
                    if self.auth.login_user(username, password):
                        self.current_user = username
                        print("Login successful.")
                    else:
                        print("Invalid username or password.")
                elif choice == '2':
                    username = input("Enter new username: ")
                    password = input("Enter new password: ")
                    self.auth.register_user(username, password)
                    print("User registered successfully.")
                elif choice == '3':
                    break
                else:
                    print("Invalid choice. Please try again.")
            else:
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
                    self.manage_suppliers()
                elif choice == '6':
                    self.generate_reports()
                elif choice == '7':
                    self.current_user = None
                    print("Logged out successfully.")
                elif choice == '8':
                    self.inventory.close()
                    self.supplier_manager.close()
                    self.report_generator.close()
                    self.auth.close()
                    break
                else:
                    print("Invalid choice. Please try again.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    app = InventoryApp()
    app.run()
