import sqlite3
import csv

class ContactManager:
    def __init__(self):
        self.conn = sqlite3.connect("contacts.db")
        self.create_table()

    
    # Create table
    def create_table(self):
        """Create the contacts table if it doesn't already exist."""
        query = """
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone_number TEXT NOT NULL,
            email TEXT,
            address TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    # Add data
    def add_contact(self):
        """Add a new contact to the database."""
        name = input("Enter contact name: ")
        phone_number = input("Enter contact phone number: ")
        email = input("Enter contact email: ")
        address = input("Enter contact address: ")

        query = """
        INSERT INTO contacts (name, phone_number, email, address) 
        VALUES (?, ?, ?, ?)
        """
        self.conn.execute(query, (name, phone_number, email, address))
        self.conn.commit()
        print("Contact added successfully!")

    # Delete data
    def delete_contact(self):
        """Delete a contact from the database by name."""
        name = input("Enter the name of the contact to delete: ")

        query = "DELETE FROM contacts WHERE name = ?"
        cursor = self.conn.execute(query, (name,))
        self.conn.commit()

        if cursor.rowcount > 0:
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

    # Search data
    def search_contact(self):
        """Search for a contact by name."""
        name = input("Enter the name of the contact to search: ")

        query = "SELECT * FROM contacts WHERE name = ?"
        cursor = self.conn.execute(query, (name,))
        contact = cursor.fetchone()

        if contact:
            print(f"ID: {contact[0]}")
            print(f"Name: {contact[1]}")
            print(f"Phone Number: {contact[2]}")
            print(f"Email: {contact[3]}")
            print(f"Address: {contact[4]}")
        else:
            print("Contact not found!")
    
    # Edit data
    def edit_contact(self):
        """Edit an existing contact's details."""
        name = input("Enter the name of the contact to edit: ")

        query = "SELECT * FROM contacts WHERE name = ?"
        cursor = self.conn.execute(query, (name,))
        contact = cursor.fetchone()

        if contact:
            print("Leave blank to keep the current value.")
            new_name = input(f"Enter new name (current: {contact[1]}): ") or contact[1]
            new_phone = input(f"Enter new phone number (current: {contact[2]}): ") or contact[2]
            new_email = input(f"Enter new email (current: {contact[3]}): ") or contact[3]
            new_address = input(f"Enter new address (current: {contact[4]}): ") or contact[4]

            update_query = """
            UPDATE contacts
            SET name = ?, phone_number = ?, email = ?, address = ?
            WHERE id = ?
            """
            self.conn.execute(update_query, (new_name, new_phone, new_email, new_address, contact[0]))
            self.conn.commit()
            print("Contact updated successfully!")
        else:
            print("Contact not found!")

    # Show all data
    def show_all_contacts(self):
        """Display all contacts in the database."""
        query = "SELECT * FROM contacts"
        cursor = self.conn.execute(query)
        contacts = cursor.fetchall()

        if contacts:
            print("Contact List:")
            for contact in contacts:
                print(f"ID: {contact[0]}, Name: {contact[1]}, Phone: {contact[2]}, Email: {contact[3]}, Address: {contact[4]}")
        else:
            print("No contacts available.")

    # Exposrt data
    def export_to_csv(self):
        """Export all contact data to a CSV file."""
        query = "SELECT * FROM contacts"
        cursor = self.conn.execute(query)
        contacts = cursor.fetchall()

        if contacts:
            with open("contacts.csv", mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Name", "Phone Number", "Email", "Address"])
                writer.writerows(contacts)
            print("Contacts exported to contacts.csv successfully!")
        else:
            print("No contacts available to export.")

    
    # Option 
    def show_menu(self):
        """Display the menu and process user input."""
        while True:
            print("\n--- ContactMaster ---")
            print("1. Add Contact")
            print("2. Delete Contact")
            print("3. Search Contact")
            print("4. Edit Contact")
            print("5. Show All Contacts")
            print("6. Export Contacts to CSV")
            print("7. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.delete_contact()
            elif choice == '3':
                self.search_contact()
            elif choice == '4':
                self.edit_contact()
            elif choice == '5':
                self.show_all_contacts()
            elif choice == '6':
                self.export_to_csv()
            elif choice == '7':
                print("Exiting ContactMaster. Goodbye!")
                break
            else:
                print("Invalid option! Please try again.")

if __name__ == "__main__":
    manager = ContactManager()
    manager.show_menu()
