import dao.accounts_dao
from modelcu.customer import Customer
from modelcu.accounts import Accounts
from service.customer_service import CustomerService
from service.accounts_service import AccountsService
import exceptions.customer_exceptions as ce
import exceptions.accounts_exceptions as ae
import pytest

def test_get_all_accounts_by_customer_id(mocker):
    def mock_test_get_all_accounts_by_customer_id(self, customer_id):
        return [Accounts(1, 1000, 1, 1), Accounts(2, 1000, 1, 2)]

    mocker.patch('dao.accounts_dao.AccountsDao.get_all_accounts_by_customer_id',
                 mock_test_get_all_accounts_by_customer_id)
    accounts_service = AccountsService()
    actual = accounts_service.get_all_accounts_by_customer_id(customer_id=1)
    assert actual == [
        {
            "id": 1,
            "balance": 1000,
            "customer_id": 1,
            "account_type_id": 1
        },
        {
            "id": 2,
            "balance": 1000,
            "customer_id": 1,
            "account_type_id": 2
        }
    ]

def test_get_account_balance_positive(mocker):
    def mock_get_account_balance(self, customer_id, amount_greater_than, amount_less_than):
        if amount_greater_than > 500 and amount_less_than < 2000:
            return Accounts(1, 1000, 1, 1)
        else:
            return None
    mocker.patch("dao.accounts_dao.AccountsDao.get_account_balance", mock_get_account_balance)
    accounts_service = AccountsService()
    actual = accounts_service.get_account_balance(customer_id=1, amount_greater_than=500, amount_less_than=2000)
    assert actual == {
        "id": 1,
        "balance": 1000,
        "customer_id": 1,
        "account_type_id": 1
    }
