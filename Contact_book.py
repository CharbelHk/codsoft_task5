import re
import tkinter as tk
from tkinter import messagebox
from tkinter import font

class ContactManager:
    def __init__(self):
        self.contacts = []  # List to store contacts (dictionary for each contact)
        self.root = tk.Tk()
        self.root.title("Contact Management System")

        self.create_widgets()

    def create_widgets(self):
        custom_font = font.Font(family="Roboto", size=9, weight="bold")

        tk.Label(self.root, text="Name:", font=custom_font).grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Phone Number:", font=custom_font).grid(row=1, column=0, padx=10, pady=5)
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Email:", font=custom_font).grid(row=2, column=0, padx=10, pady=5)
        self.email_entry = tk.Entry(self.root)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Address:", font=custom_font).grid(row=3, column=0, padx=10, pady=5)
        self.address_entry = tk.Entry(self.root)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Button(self.root, text="Add Contact", font=custom_font, command=self.add_contact).grid(row=4, column=0, padx=10, pady=10)
        tk.Button(self.root, text="View Contacts", font=custom_font, command=self.view_contacts).grid(row=4, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Search Contact", font=custom_font, command=self.search_contact_window).grid(row=4, column=2, padx=10,pady=10)
        tk.Button(self.root, text="Update Contact", font=custom_font, command=self.update_contact_window).grid(row=5, column=1, padx=10,pady=10)
        tk.Button(self.root, text="Delete Contact", font=custom_font, command=self.delete_contact_window).grid(row=5, column=0, padx=10,pady=10)
        tk.Button(self.root, text="Exit", font=custom_font, command=self.root.destroy).grid(row=5, column=2, padx=10, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone_number = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if not re.match("^[a-zA-Z ]+$", name):
            messagebox.showerror("Error", "Invalid name. Please use only letters.")
            return

        if len(phone_number) < 8 or len(phone_number) > 20:
            messagebox.showerror("Error", "Invalid phone number length. Please provide a valid number.")
            return

        if not re.match(r"[^@]+@(gmail\.com|hotmail\.com|yahoo\.com)$", email):
            messagebox.showerror("Error", "Invalid email format. Please provide a valid email (gmail.com, hotmail.com, yahoo.com).")
            return

        contact = {
            "name": name,
            "phone_number": phone_number,
            "email": email,
            "address": address
        }
        self.contacts.append(contact)
        messagebox.showinfo("Success", "Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Contacts", "No contacts found.")
            return

        contacts_list = ""
        for contact in self.contacts:
            contacts_list += f"Name: {contact['name']}\nPhone: {contact['phone_number']}\nEmail: {contact['email']}\nAddress: {contact['address']}\n\n"

        contacts_window = tk.Toplevel(self.root)
        contacts_window.title("Contacts")
        tk.Label(contacts_window, text=contacts_list).pack(padx=10, pady=10)

    def search_contact_window(self):
        search_window = tk.Toplevel(self.root)
        search_window.title("Search Contact")

        tk.Label(search_window, text="Enter name or phone number to search:").grid(row=0, column=0, padx=10, pady=5)
        search_entry = tk.Entry(search_window)
        search_entry.grid(row=0, column=1, padx=10, pady=5)

        def search_contact():
            search_query = search_entry.get()
            if search_query:
                found_contacts = self.search_contact(search_query)
                if found_contacts:
                    found_contacts_list = ""
                    for contact in found_contacts:
                        found_contacts_list += f"Name: {contact['name']}\nPhone: {contact['phone_number']}\nEmail: {contact['email']}\nAddress: {contact['address']}\n\n"
                    messagebox.showinfo("Matching Contacts", found_contacts_list)
                else:
                    messagebox.showinfo("Matching Contacts", "No matching contacts found.")
            else:
                messagebox.showerror("Error", "Please enter a search query.")

        search_button = tk.Button(search_window, text="Search", command=search_contact)
        search_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    def update_contact_window(self):
        update_window = tk.Toplevel(self.root)
        update_window.title("Update Contact")

        tk.Label(update_window, text="Enter the index of the contact to update:").grid(row=0, column=0, padx=10, pady=5)
        update_index_entry = tk.Entry(update_window)
        update_index_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(update_window, text="Enter new name (leave blank to keep unchanged):").grid(row=1, column=0, padx=10, pady=5)
        update_name_entry = tk.Entry(update_window)
        update_name_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(update_window, text="Enter new phone number (leave blank to keep unchanged):").grid(row=2, column=0, padx=10, pady=5)
        update_phone_entry = tk.Entry(update_window)
        update_phone_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(update_window, text="Enter new email (leave blank to keep unchanged):").grid(row=3, column=0, padx=10,pady=5)

        update_email_entry = tk.Entry(update_window)
        update_email_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(update_window, text="Enter new address (leave blank to keep unchanged):").grid(row=4, column=0,padx=10, pady=5)

        update_address_entry = tk.Entry(update_window)
        update_address_entry.grid(row=4, column=1, padx=10, pady=5)

        def update_contact():
            index = int(update_index_entry.get())
            new_name = update_name_entry.get()
            new_phone = update_phone_entry.get()
            new_email = update_email_entry.get()
            new_address = update_address_entry.get()

            self.update_contact_entry(index, new_name, new_phone, new_email, new_address)
            messagebox.showinfo("Success", "Contact updated successfully.")

        update_button = tk.Button(update_window, text="Update", command=update_contact)
        update_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def delete_contact_window(self):
        delete_window = tk.Toplevel(self.root)
        delete_window.title("Delete Contact")

        tk.Label(delete_window, text="Enter the index of the contact to delete:").grid(row=0, column=0, padx=10, pady=5)
        delete_index_entry = tk.Entry(delete_window)
        delete_index_entry.grid(row=0, column=1, padx=10, pady=5)

        def delete_contact():
            index = int(delete_index_entry.get())
            self.delete_contact_entry(index)
            messagebox.showinfo("Success", "Contact deleted successfully.")

        delete_button = tk.Button(delete_window, text="Delete", command=delete_contact)
        delete_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    def run(self):
        self.root.mainloop()
    def search_contact(self, search_query):
        found_contacts = []
        for contact in self.contacts:
            if (
                search_query.lower() in contact["name"].lower() or
                search_query in contact["phone_number"]
            ):
                found_contacts.append(contact)
        return found_contacts

    def update_contact_entry(self, index, name=None, phone_number=None, email=None, address=None):
        if 0 < index <= len(self.contacts):
            contact = self.contacts[index - 1]
            if name:
                contact["name"] = name
            if phone_number:
                contact["phone_number"] = phone_number
            if email:
                contact["email"] = email
            if address:
                contact["address"] = address


    def delete_contact_entry(self, index):
        if 0 < index <= len(self.contacts):
            del self.contacts[index - 1]


if __name__ == "__main__":
    contact_manager = ContactManager()
    contact_manager.run()