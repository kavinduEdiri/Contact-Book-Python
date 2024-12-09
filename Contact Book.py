import json
import os

# File where the contacts will be stored
CONTACT_FILE = "contacts.json"


if not os.path.exists(CONTACT_FILE):
    with open(CONTACT_FILE, 'w') as f:
        json.dump([], f)



class Contact:
    def __init__(self, fname, lname, mobile, email, phone_type):
        self.fname = fname
        self.lname = lname
        self.mobile = mobile
        self.email = email
        self.phone_type = phone_type

    def to_dict(self):

        return {
            'fname': self.fname,
            'lname': self.lname,
            'mobile': self.mobile,
            'email': self.email,
            'phone_type': self.phone_type
        }

    @classmethod
    def from_dict(cls, data):

        return cls(data['fname'], data['lname'], data['mobile'], data['email'], data['phone_type'])



def load_contacts():

    with open(CONTACT_FILE, 'r') as f:
        contacts = json.load(f)
    return [Contact.from_dict(contact) for contact in contacts]



def save_contacts(contacts):

    with open(CONTACT_FILE, 'w') as f:
        json.dump([contact.to_dict() for contact in contacts], f)


# Function to add a new contact to the contact book
def add_contact():

    print("Adding New Contact:")
    fname = input("First Name: ")
    lname = input("Last Name: ")
    mobile = input("Mobile Number: ")
    email = input("Email Address: ")
    phone_type = input("Phone Type (Mobile/Home/Work): ")


    contact = Contact(fname, lname, mobile, email, phone_type)


    contacts = load_contacts()
    contacts.append(contact)


    save_contacts(contacts)
    print(f"Contact {fname} {lname} added successfully.")


# Function to display all the contacts
def view_contacts():

    contacts = load_contacts()
    if not contacts:
        print("No contacts available.")
        return
    for idx, contact in enumerate(contacts, 1):
        print(f"{idx}. {contact.fname} {contact.lname} - {contact.mobile} ({contact.phone_type}) - {contact.email}")


# Function to search for contacts based on a query (partial/full match)
def search_contact():

    query = input("Enter search query (First Name, Last Name, Mobile, Email): ").lower()
    contacts = load_contacts()


    found_contacts = [contact for contact in contacts if
                      any(query in value.lower() for value in contact.to_dict().values())]

    if not found_contacts:
        print("No matching contacts found.")
    else:
        for contact in found_contacts:
            print(f"{contact.fname} {contact.lname} - {contact.mobile} ({contact.phone_type}) - {contact.email}")


# Function to update an existing contact
def update_contact():

    view_contacts()  # Show all contacts to the user
    idx = int(input("Enter the contact number to update: ")) - 1
    contacts = load_contacts()


    if idx < 0 or idx >= len(contacts):
        print("Invalid contact number.")
        return

    contact = contacts[idx]

    print(f"Updating Contact: {contact.fname} {contact.lname}")
    fname = input(f"New First Name (Current: {contact.fname}): ") or contact.fname
    lname = input(f"New Last Name (Current: {contact.lname}): ") or contact.lname
    mobile = input(f"New Mobile Number (Current: {contact.mobile}): ") or contact.mobile
    email = input(f"New Email (Current: {contact.email}): ") or contact.email
    phone_type = input(f"New Phone Type (Current: {contact.phone_type}): ") or contact.phone_type


    contact.fname, contact.lname, contact.mobile, contact.email, contact.phone_type = fname, lname, mobile, email, phone_type


    save_contacts(contacts)
    print("Contact updated successfully.")


# Function to delete a contact
def delete_contact():

    view_contacts()  # Show all contacts to the user
    idx = int(input("Enter the contact number to delete: ")) - 1
    contacts = load_contacts()

    # Check if the contact index is valid
    if idx < 0 or idx >= len(contacts):
        print("Invalid contact number.")
        return

    deleted_contact = contacts.pop(idx)
    save_contacts(contacts)
    print(f"Contact {deleted_contact.fname} {deleted_contact.lname} deleted successfully.")


# Main menu
def main_menu():

    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contacts")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")


# Start
if __name__ == "__main__":
    main_menu()