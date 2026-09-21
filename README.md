# Contact Book (Python)

A simple command-line contact book built with Python. Contacts are stored
persistently in a JSON file, so your data is still there next time you run
the program.

## Features
- Add a contact (name, phone, email, address)
- View all contacts
- Search contacts by name, phone, or email
- Update an existing contact
- Delete a contact
- Data automatically saved to `contacts.json`

## Project structure
```
contact_book/
├── main.py            # menu loop / user interaction
├── contact.py         # Contact class
├── contact_book.py     # ContactBook class (manages contacts + storage)
└── contacts.json       # created automatically after first run
```

## How to run
```bash
python main.py
```

## Possible extensions (for extra credit)
- Add input validation (e.g. phone number format, duplicate email checks)
- Add a GUI with `tkinter`
- Switch storage to a SQLite database
- Add contact categories/groups (family, work, etc.)
- Export contacts to CSV
