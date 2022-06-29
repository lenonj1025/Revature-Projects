class Customer:
    def __init__(self, id, first_name, last_name, checking_account, savings_account):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.checking_account = checking_account
        self.savings_account = savings_account

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "checking_account": self.checking_account,
            "savings_account": self.savings_account
        }
