contacts = []

while True:
    print("\n--- Contact Management System ---")
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Delete Contact")
    print("4. Sort Contacts by Name")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        name = input("Enter name: ")
        email = input("Enter email: ")
        mobile = input("Enter mobile: ")
        contact = {'name': name, 'email': email, 'mobile': mobile}
        contacts.append(contact)
        print("Contact added successfully!")
    elif choice == '2':
        if len(contacts) == 0:
            print("No contacts found.")
        else:
            for contact in contacts:
                print(f"Name: {contact['name']}, Email: {contact['email']}, Mobile: {contact['mobile']}")
    elif choice == '3':
        name = input("Enter the name of the contact to delete: ")
        found = False
        for contact in contacts:
            if contact['name'] == name:
                contacts.remove(contact)
                found = True
                print(f"Contact '{name}' deleted successfully!")
                break
        if not found:
            print("Contact not found.")
    elif choice == '4':
        contacts.sort(key=lambda x: x['name'])
        print("Contacts sorted in ascending order by name.")
    elif choice == '5':
        print("Thank you for using the Contact Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")