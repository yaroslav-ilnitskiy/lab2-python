from contact import Contact
from typing import List


class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact: Contact):
        self.contacts.append(contact)

    def remove_contact(self, contact: Contact):
        self.contacts.remove(contact)

    def find_contact(self, name: str):
        for contact in self.contacts:
            if contact.name == name:
                return contact

        return None

    def get_contacts(self) -> List[Contact]:
        return self.contacts

    def get_count(self) -> int:
        return len(self.contacts)
