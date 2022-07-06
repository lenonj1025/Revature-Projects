from dao.customer_dao import CustomerDao
from dao.accounts_dao import AccountsDao
import exceptions.customer_exceptions as ce
import exceptions.accounts_exceptions as ae

class AccountsService:

    def __init__(self):
        self.accounts_dao = AccountsDao()
        self.customer_dao = CustomerDao()

    def get_all_accounts_by_customer_id(self, customer_id):
        if self.customer_dao.get_customer_by_id(customer_id) is None:
            raise ce.CustomerNotFound(f"Customer with id {customer_id} was not found")
        return list(map(lambda y: y.to_dict(), self.accounts_dao.get_all_accounts_by_customer_id(customer_id)))

    def get_account_balance(self, customer_id, amount_greater_than, amount_less_than):
        list_of_accounts = self.accounts_dao.get_account_balance(customer_id, amount_greater_than, amount_less_than)
        if self.customer_dao.get_customer_by_id(customer_id) is None:
            raise ce.CustomerNotFound(f"Customer with id {customer_id} was not found")
        if len(list_of_accounts) == 0:
            raise ae.AccountNotFound(f"No account with amount greater than {amount_greater_than} or amount less "
                                     f"than {amount_less_than} was found")
        return list(map(lambda y: y.to_dict(), list_of_accounts))

    def get_account_by_greater_than(self, customer_id, amount_greater_than):
        list_of_accounts = self.accounts_dao.get_account_by_greater_than(customer_id, amount_greater_than)
        if self.customer_dao.get_customer_by_id(customer_id) is None:
            raise ce.CustomerNotFound(f"Customer with id {customer_id} was not found")
        if len(list_of_accounts) == 0:
            raise ae.AccountNotFound(f"No account with amount greater than {amount_greater_than} was found")
        return list(map(lambda y: y.to_dict(), list_of_accounts))

    def get_account_by_less_than(self, customer_id, amount_less_than):
        list_of_accounts = self.accounts_dao.get_account_by_less_than(customer_id, amount_less_than)
        if self.customer_dao.get_customer_by_id(customer_id) is None:
            raise ce.CustomerNotFound(f"Customer with id {customer_id} was not found")
        if len(list_of_accounts) == 0:
            raise ae.AccountNotFound(f"No account with amount less than {amount_less_than} was found")
        return list(map(lambda y: y.to_dict(), list_of_accounts))

    def get_account_by_customer_and_account_id(self, customer_id, account_id):
        a = self.accounts_dao.get_account_by_customer_and_account_id(customer_id, account_id)
        if self.customer_dao.get_customer_by_id(customer_id) is None:
            raise ce.CustomerNotFound(f"Customer with id {customer_id} was not found")
        if len(a) == 0:
            raise ae.AccountNotFound(f"Account with id {account_id} was not found")
        return list(map(lambda y: y.to_dict(), self.accounts_dao.get_account_by_customer_and_account_id(customer_id,
                                                                                                        account_id)))

    def add_account_to_customer(self, account_object):
        if self.customer_dao.get_customer_by_id(account_object.customer_id) is None:
            raise ce.CustomerNotFound(f"Customer with id {account_object.customer_id} was not found")
        if int(account_object.balance) < 0:
            raise ce.CustomerNotFound("Cannot have a negative balance!")
        if int(account_object.account_type_id) not in range(1, 3):
            raise ae.AccountTypeError("Not a savings or checking account!")
        added_new_account = self.accounts_dao.add_account_to_customer(account_object)
        return added_new_account.to_dict()

    def update_acct_by_cust_and_acct_id(self, account_object):
        updated_account_object = self.accounts_dao.update_acct_by_cust_and_acct_id(account_object)
        if int(account_object.account_type_id) not in range(1, 3):
            raise ae.AccountTypeError("Not a savings or checking account!")
        if updated_account_object is None:
            raise ae.AccountNotFound(f" Account with id {account_object.id} was not found")
        return updated_account_object.to_dict()

    def delete_account_by_account_id(self, customer_id, account_id):
        if not self.customer_dao.get_customer_by_id(customer_id):
            raise ce.CustomerNotFound(f"Customer with id {customer_id} was not found")
        if not self.accounts_dao.delete_account_by_account_id(customer_id, account_id):
            raise ae.AccountNotFound(f"Account with id {account_id} for customer was not found")
        return self.accounts_dao.delete_account_by_account_id(customer_id, account_id)



