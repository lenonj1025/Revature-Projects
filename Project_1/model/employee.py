class Employee:
    def __init__(self, username, password, first_name, last_name, phone_number, email_address):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email_address = email_address


    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone_number": self.phone_number,
            "email_address": self.email_address
        }
