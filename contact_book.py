import json
import os
from contact import Contact


class ContactBook:
    """Manages a collection of Contact objects and handles saving/loading."""

    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = []
        self.load()

    def add_contact(self, name, phone, email, address=""):
        if self.find_by_name(name):
            print(f"A contact named '{name}' already exists.")
            return False
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        self.save()
        return True

    def view_all(self):
        return self.contacts

    def find_by_name(self, name):
        return [c for c in self.contacts if c.name.lower() == name.lower()]

    def search(self, query):
        query = query.lower()
        return [
            c for c in self.contacts
            if query in c.name.lower()
            or query in c.phone.lower()
            or query in c.email.lower()
        ]

    def update_contact(self, name, phone=None, email=None, address=None):
        matches = self.find_by_name(name)
        if not matches:
            return False
        contact = matches[0]
        if phone:
            contact.phone = phone
        if email:
            contact.email = email
        if address:
            contact.address = address
        self.save()
        return True

    def delete_contact(self, name):
        matches = self.find_by_name(name)
        if not matches:
            return False
        self.contacts = [c for c in self.contacts if c.name.lower() != name.lower()]
        self.save()
        return True

    def save(self):
        with open(self.filename, "w") as f:
            json.dump([c.to_dict() for c in self.contacts], f, indent=4)

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                try:
                    data = json.load(f)
                    self.contacts = [Contact.from_dict(d) for d in data]
                except json.JSONDecodeError:
                    self.contacts = []
        else:
            self.contacts = []
