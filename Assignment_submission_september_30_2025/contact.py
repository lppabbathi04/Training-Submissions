
contacts = {
    "Priya": {"phone": "1234567890", "email": "priya@gmail.com"},
    "Alex": {"phone": "9876543210", "email": "alex@yahoo.com"}
}

print(" Contact Book:")
for name, info in contacts.items():
    print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")


new_name = input("\nEnter new contact name: ")
new_phone = input("Enter phone number: ")
new_email = input("Enter email: ")

contacts[new_name] = {"phone": new_phone, "email": new_email}

print("\n Updated Contact Book:")
for name, info in contacts.items():
    print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
