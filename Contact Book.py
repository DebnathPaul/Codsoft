

import json

contact_file = 'contacts.json'

def load():
    try:
        with open(contact_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save(contacts):
    with open(contact_file, 'w') as file:
        json.dump(contacts, file)

def add(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    save(contacts)

def view(contacts):
    print("Contact list ")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}.Name : {contact['name']}  \n  Phone no : {contact['phone']}  \n  Email : {contact['email']}  \n  Address : {contact['address']}")
        print("")
        
def search(contacts):
    search = input("Enter name or phone number to search: ")
    for contact in contacts:
        if search in contact['name'] or search in contact['phone']:
            print(f"Found: \nName : {contact['name']}  \nPhone no : {contact['phone']}  \nEmail : {contact['email']}  \nAddress : {contact['address']}")
            print("")

def update(contacts):
    print("Contact list ")
    view(contacts)
    
    contact_number = int(input("Enter contact number to update: "))
    if (0 < contact_number <= len(contacts)):
        contact = contacts[contact_number - 1]
        contact['name'] = input("Enter new name: ")
        contact['phone'] = input("Enter new phone number: ")
        contact['email'] = input("Enter new email: ")
        contact['address'] = input("Enter new address: ")
        save(contacts)
    print("Contact list after update ")
    view(contacts)

def delete(contacts):
    print("Contact list ")
    view(contacts)
    
    contact_number = int(input("Enter contact number to delete: "))
    if (0 < contact_number <= len(contacts)):
        contacts.pop(contact_number - 1)
        save(contacts)
    print("Contact list After delete ")
    view(contacts)

def ABCD():
    contacts = load()
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option: ")
        print("")

        if choice == '1':
            add(contacts)
        elif choice == '2':
            view(contacts)
        elif choice == '3':
            search(contacts)
        elif choice == '4':
            update(contacts)
        elif choice == '5':
            delete(contacts)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")


ABCD()









































