class Contact:
    """Represents a single contact."""

    def __init__(self, name, phone, email, address=""):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "address": self.address,
        }

    @staticmethod
    def from_dict(data):
        return Contact(
            data.get("name", ""),
            data.get("phone", ""),
            data.get("email", ""),
            data.get("address", ""),
        )

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Phone: {self.phone}\n"
            f"Email: {self.email}\n"
            f"Address: {self.address}"
        )
