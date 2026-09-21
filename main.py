from contact_book import ContactBook


def print_menu():
    print("\n===== CONTACT BOOK =====")
    print("1. Add contact")
    print("2. View all contacts")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Exit")


def add_contact_flow(book):
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    address = input("Address (optional): ").strip()
    if book.add_contact(name, phone, email, address):
        print(f"Contact '{name}' added.")


def view_all_flow(book):
    contacts = book.view_all()
    if not contacts:
        print("No contacts saved yet.")
        return
    for i, c in enumerate(contacts, start=1):
        print(f"\n--- Contact {i} ---")
        print(c)


def search_flow(book):
    query = input("Search by name, phone, or email: ").strip()
    results = book.search(query)
    if not results:
        print("No matches found.")
        return
    for c in results:
        print("\n---")
        print(c)


def update_flow(book):
    name = input("Name of contact to update: ").strip()
    if not book.find_by_name(name):
        print("Contact not found.")
        return
    print("Leave a field blank to keep it unchanged.")
    phone = input("New phone: ").strip()
    email = input("New email: ").strip()
    address = input("New address: ").strip()
    book.update_contact(name, phone or None, email or None, address or None)
    print("Contact updated.")


def delete_flow(book):
    name = input("Name of contact to delete: ").strip()
    if book.delete_contact(name):
        print(f"Contact '{name}' deleted.")
    else:
        print("Contact not found.")


def main():
    book = ContactBook()
    actions = {
        "1": add_contact_flow,
        "2": view_all_flow,
        "3": search_flow,
        "4": update_flow,
        "5": delete_flow,
    }

    while True:
        print_menu()
        choice = input("Choose an option (1-6): ").strip()
        if choice == "6":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action(book)
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()
