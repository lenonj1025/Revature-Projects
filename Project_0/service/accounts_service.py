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

    def get_account_balance(self, customer_id, amount_greater_than, amount_less_than):
        list_of_accounts = self.accounts_dao.get_account_balance(customer_id, amount_greater_than, amount_less_than)

        return list(map(lambda y: y.to_dict(), list_of_accounts))

    def get_account_by_greater_than(self, customer_id, amount_greater_than):
        list_of_accounts = self.accounts_dao.get_account_by_greater_than(customer_id, amount_greater_than)

        return list(map(lambda y: y.to_dict(), list_of_accounts))

    def get_account_by_less_than(self, customer_id, amount_less_than):
        list_of_accounts = self.accounts_dao.get_account_by_less_than(customer_id, amount_less_than)

        return list(map(lambda y: y.to_dict(), list_of_accounts))

    def get_account_by_customer_and_account_id(self, customer_id, account_id):
        if not self.accounts_dao.get_account_by_customer_and_account_id(customer_id, account_id):
            raise CustomerNotFound(f"Customer with account id {account_id} was not found")

        return list(map(lambda y: y.to_dict(), self.accounts_dao.get_account_by_customer_and_account_id(customer_id,
                                                                                                        account_id)))

    def add_account_to_customer1(self, account_object):
        if account_object.balance < 0:
            raise CustomerNotFound("Cannot have a negative balance !")
        if account_object.account_type_id != 1 and account_object.account_type_id != 2:
            raise CustomerNotFound("Not a savings or checking account!")
        # if account_object.customer_id != customer_id:
        #     raise CustomerNotFound("Last name must be at least two characters")

        added_new_account = self.accounts_dao.add_account_to_customer2(account_object)
        return added_new_account.to_dict()

    def update_acct_by_cust_and_acct_id(self, account_object):
        updated_account_object = self.accounts_dao.update_acct_by_cust_and_acct_id(account_object)
        if updated_account_object is None:
            raise CustomerNotFound(f" Account with id {account_object.id} was not found")

        return updated_account_object.to_dict()

    def delete_account_by_account_id(self, customer_id, account_id):
        if not self.accounts_dao.delete_account_by_account_id(customer_id, account_id):
            raise CustomerNotFound(f"Customer with id {customer_id} was not found")

