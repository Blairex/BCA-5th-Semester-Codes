# Program Q4 updated header
# 4. Build a contact book program using dictionaries to store and manage contact details. Allow users to update phone numbers.
contacts = {}

while True:
    choice = input("1. Add Contact\n2. Update Contact\n3. View Contacts\n4. Exit\nEnter choice: ")
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        contacts[name] = phone
    elif choice == "2":
        name = input("Enter name to update: ")
        if name in contacts:
            contacts[name] = input("Enter new phone: ")
        else:
            print("Contact not found")
    elif choice == "3":
        for k,v in contacts.items():
            print(k, ":", v)
    elif choice == "4":
        break
    else:
        print("Invalid choice")
# Extra feature note
