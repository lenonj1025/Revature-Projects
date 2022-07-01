class Accounts:
    def __init__(self, id, balance, customer_id, account_type_id):
        self.id = id
        self.balance = balance
        self.customer_id = customer_id
        self.account_type_id = account_type_id

    def to_dict(self):
        return {
            "id": self.id,
            "balance": self.balance,
            "customer_id": self.customer_id,
            "account_type_id": self.account_type_id
        }

class CustomersAccounts:
    def __init__(self, id, balance, customer_id, account_type, first_name, last_name):
        self.id = id
        self.balance = balance
        self.customer_id = customer_id
        self.account_type = account_type
        self.first_name = first_name
        self.last_name = last_name

    def to_dict(self):
        return {
            "id": self.id,
            "customer_id": self.customer_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "balance": self.balance,
            "account_type": self.account_type
        }
