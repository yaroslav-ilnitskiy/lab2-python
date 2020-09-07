from contact import Contact
from phone_book import PhoneBook

print("Phone book")

phoneBook = PhoneBook()


def write_contacts(phone_book: PhoneBook):
    if phone_book.get_count() == 0:
        print("List is empty")
        return

    for contact in phone_book.get_contacts():
        print(
            f'Name: {contact.get_name()} PersonalPhone: {contact.get_personal_phone()} Phone {contact.get_phone()}'
            f' Description {contact.get_description()}'
        )


def add_contact(phone_book: PhoneBook):
    name = input("Enter name")
    contact = Contact(name)

    contact.personal_phone = input("Enter PersonalPhone")
    contact.phone = input("Enter Phone")
    contact.description = input("Enter Description")

    phone_book.add_contact(contact)

    print("Contact successfully added")


def remove_contact(phone_book: PhoneBook):
    name = input("Enter name")

    contact = phone_book.find_contact(name)

    if contact is not None:
        phone_book.remove_contact(contact)
        print("Contact successfully removed")


while 1:
    command = input("Enter command, a - show all contacts, n - add new contact, r - remove contact")

    switcher = {
        "a": write_contacts,
        "n": add_contact,
        "r": remove_contact,
    }

    func = switcher.get(command, "nothing")

    func(phoneBook)
