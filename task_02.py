contacts = []

def display_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        print("\nContact List:")
        print("{:<15} {:<15} {:<20} {:<30}".format("Name", "Phone", "Email", "Address"))
        for contact in contacts:
            print("{:<15} {:<15} {:<20} {:<30}".format(contact['name'], contact['phone'], contact['email'], contact['address']))
            
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contacts.append({
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    })
    print(f"Contact for {name} added successfully.")
    
def search_contact():
    search_term = input("Enter name or phone number to search: ").lower()
    found_contacts = [contact for contact in contacts if search_term in contact['name'].lower() or search_term in contact['phone']]
    if found_contacts:
        print("\nSearch Results:")
        print("{:<15} {:<15} {:<20} {:<30}".format("Name", "Phone", "Email", "Address"))
        for contact in found_contacts:
            print("{:<15} {:<15} {:<20} {:<30}".format(contact['name'], contact['phone'], contact['email'], contact['address']))
    else:
        print("No contacts found.")

def update_contact():
    name = input("Enter the name of the contact you want to update: ")
    contact_to_update = next((contact for contact in contacts if contact['name'].lower() == name.lower()), None)
    
    if contact_to_update:
        print(f"Updating contact for {name}")
        contact_to_update['phone'] = input(f"Enter new phone number (current: {contact_to_update['phone']}): ") or contact_to_update['phone']
        contact_to_update['email'] = input(f"Enter new email (current: {contact_to_update['email']}): ") or contact_to_update['email']
        contact_to_update['address'] = input(f"Enter new address (current: {contact_to_update['address']}): ") or contact_to_update['address']
        print(f"Contact for {name} updated successfully.")
    else:
        print(f"Contact for {name} not found.")

def delete_contact():
    name = input("Enter the name of the contact you want to delete: ")
    contact_to_delete = next((contact for contact in contacts if contact['name'].lower() == name.lower()), None)
    
    if contact_to_delete:
        contacts.remove(contact_to_delete)
        print(f"Contact for {name} deleted successfully.")
    else:
        print(f"Contact for {name} not found.")

def menu():
    while True:
        print("\n===== Contact Book =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            display_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the contact book...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
