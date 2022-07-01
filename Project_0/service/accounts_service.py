from dao.customer_dao import CustomerDao
from dao.accounts_dao import AccountsDao
from exceptions.customer_not_found import CustomerNotFound

class AccountsService:

    def __init__(self):
        self.accounts_dao = AccountsDao()
        self.customer_dao = CustomerDao()

    def get_all_accounts_by_customer_id(self, customer_id):
        if self.customer_dao.get_customer_by_id(customer_id) is None:
            raise CustomerNotFound(f"Customer with id {customer_id} was not found")

        return list(map(lambda y: y.to_dict(), self.accounts_dao.get_all_accounts_by_customer_id(customer_id)))

    def get_account_balance(self, customer_id, balance_gt, balance_lt):
        list_of_accounts = self.accounts_dao.get_account_balance(customer_id, balance_gt, balance_lt)

        return list(map(lambda y: y.to_dict(), list_of_accounts))

    # def get_account_by_customer_and_account_id(self, account_id):
    #     account_object = self.customer_dao.get_account_by_id(account_id)
    #     if not customer_object:
    #         raise CustomerNotFound(f"User with the id {customer_id} was not found")
    #
    #     return customer_object.to_dict()
