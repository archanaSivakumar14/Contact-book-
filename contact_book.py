
import os

CONTACTS_FILE = "contacts.txt"

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")

    with open(CONTACTS_FILE, "a") as file:
        file.write(f"{name},{phone},{email}\n")
    print("Contact added successfully.\n")

def view_contacts():
    if not os.path.exists(CONTACTS_FILE):
        print("No contacts found.\n")
        return

    with open(CONTACTS_FILE, "r") as file:
        lines = file.readlines()

    if not lines:
        print("No contacts to display.\n")
        return

    print("\n--- All Contacts ---")
    for line in lines:
        name, phone, email = line.strip().split(",")
        print(f"Name: {name}, Phone: {phone}, Email: {email}")
    print()

def search_contact():
    search_name = input("Enter name to search: ").lower()

    found = False
    with open(CONTACTS_FILE, "r") as file:
        for line in file:
            name, phone, email = line.strip().split(",")
            if search_name in name.lower():
                print(f"Found - Name: {name}, Phone: {phone}, Email: {email}")
                found = True
    if not found:
        print("No contact found with that name.\n")

def update_contact():
    name_to_update = input("Enter the name of the contact to update: ")
    updated_lines = []
    found = False

    with open(CONTACTS_FILE, "r") as file:
        lines = file.readlines()

    for line in lines:
        name, phone, email = line.strip().split(",")
        if name.lower() == name_to_update.lower():
            new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            updated_lines.append(f"{name},{new_phone},{new_email}\n")
            found = True
        else:
            updated_lines.append(line)

    with open(CONTACTS_FILE, "w") as file:
        file.writelines(updated_lines)

    if found:
        print("Contact updated successfully.\n")
    else:
        print("Contact not found.\n")

def delete_contact():
    name_to_delete = input("Enter the name of the contact to delete: ")
    updated_lines = []
    deleted = False

    with open(CONTACTS_FILE, "r") as file:
        lines = file.readlines()

    for line in lines:
        name, phone, email = line.strip().split(",")
        if name.lower() == name_to_delete.lower():
            deleted = True
            continue
        updated_lines.append(line)

    with open(CONTACTS_FILE, "w") as file:
        file.writelines(updated_lines)

    if deleted:
        print("Contact deleted successfully.\n")
    else:
        print("Contact not found.\n")

def menu():
    while True:
        print("=== Contact Book Menu ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")

if __name__ == "__main__":
    menu()
