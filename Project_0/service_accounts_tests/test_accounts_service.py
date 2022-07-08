from modelcu.customer import Customer
from modelcu.accounts import Accounts
from service.customer_service import CustomerService
from service.accounts_service import AccountsService
import exceptions.customer_exceptions as ce
import exceptions.accounts_exceptions as ae
import pytest

def test_get_all_accounts_by_customer_id(mocker):
    def mock_get_all_accounts_by_customer_id(self, customer_id):
        return [Accounts(1, 1000, 1, 1), Accounts(2, 1000, 1, 2)]
    mocker.patch('dao.accounts_dao.AccountsDao.get_all_accounts_by_customer_id',
                 mock_get_all_accounts_by_customer_id)
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
        if amount_greater_than >= 500 and amount_less_than <= 2000:
            return Accounts(1, 1000, 1, 1)
        else:
            return None
    mocker.patch("dao.accounts_dao.AccountsDao.get_account_balance", mock_get_account_balance)
    accounts_service = AccountsService()
    actual = accounts_service.get_account_balance(1, 500, 2000)
    assert actual == {
        "id": 1,
        "balance": 1000,
        "customer_id": 1,
        "account_type_id": 1
    }

def test_get_account_balance_positive_multiple(mocker):
    def mock_get_account_balance(self, customer_id, amount_greater_than, amount_less_than):
        if amount_greater_than >= 500 and amount_less_than <= 2000:
            return [Accounts(1, 1000, 1, 1), Accounts(2, 1500, 1, 2)]
        else:
            return None
    mocker.patch("dao.accounts_dao.AccountsDao.get_account_balance", mock_get_account_balance)
    accounts_service = AccountsService()
    actual = accounts_service.get_account_balance(1, 500, 2000)
    assert actual == [
        {
            "id": 1,
            "balance": 1000,
            "customer_id": 1,
            "account_type_id": 1
        },
        {
            "id": 2,
            "balance": 1500,
            "customer_id": 1,
            "account_type_id": 2
        }
    ]

def test_get_account_balance_negative(mocker):
    def mock_get_account_balance(self, customer_id, amount_greater_than, amount_less_than):
        if amount_greater_than > 500 and amount_less_than < 2000:
            return Accounts(1, 5000, 1, 1)
        else:
            return None
    mocker.patch("dao.accounts_dao.AccountsDao.get_account_balance", mock_get_account_balance)
    accounts_service = AccountsService()
    with pytest.raises(ae.AccountNotFound) as excinfo:
        actual = accounts_service.get_account_balance(1, 500, 2000)
    assert str(excinfo.value) == "No account(s) with amount greater than 500 or amount less than 2000 was found"

def test_get_account_balance_negative_multiple(mocker):
    def mock_get_account_balance(self, customer_id, amount_greater_than, amount_less_than):
        if amount_greater_than > 500 and amount_less_than < 2000:
            return [Accounts(1, 5000, 1, 1), Accounts(2, 20000, 1, 2)]
        else:
            return None
    mocker.patch("dao.accounts_dao.AccountsDao.get_account_balance", mock_get_account_balance)
    accounts_service = AccountsService()
    with pytest.raises(ae.AccountNotFound) as excinfo:
        actual = accounts_service.get_account_balance(1, 500, 2000)
    assert str(excinfo.value) == "No account(s) with amount greater than 500 or amount less than 2000 was found"

def test_get_account_by_greater_than_positive(mocker):
    def mock_get_account_by_greater_than(self, customer_id, amount_greater_than):
        if amount_greater_than >= 500:
            return Accounts(1, 1000, 1, 1)
        else:
            return None
    mocker.patch("dao.accounts_dao.AccountsDao.get_account_by_greater_than", mock_get_account_by_greater_than)
    accounts_service = AccountsService()
    actual = accounts_service.get_account_by_greater_than(1, 500)
    assert actual == {
        "id": 1,
        "balance": 1000,
        "customer_id": 1,
        "account_type_id": 1
    }

def test_get_account_by_greater_than_positive_multiple(mocker):
    def mock_get_account_by_greater_than(self, customer_id, amount_greater_than):
        if amount_greater_than >= 500:
            return [Accounts(1, 1000, 1, 1), Accounts(2, 1500, 1, 2)]
        else:
            return None
    mocker.patch("dao.accounts_dao.AccountsDao.get_account_by_greater_than", mock_get_account_by_greater_than)
    accounts_service = AccountsService()
    actual = accounts_service.get_account_by_greater_than(1, 500)
    assert actual == [
        {
            "id": 1,
            "balance": 1000,
            "customer_id": 1,
            "account_type_id": 1
        },
        {
            "id": 2,
            "balance": 1500,
            "customer_id": 1,
            "account_type_id": 2
        }
    ]

def test_get_account_by_greater_than_negative(mocker):
    def mock_get_account_by_greater_than(self, customer_id, amount_greater_than):
        if amount_greater_than > 500:
            return Accounts(1, 200, 1, 1)
        else:
            return None
    mocker.patch("dao.accounts_dao.AccountsDao.get_account_by_greater_than", mock_get_account_by_greater_than)
    accounts_service = AccountsService()
    with pytest.raises(ae.AccountNotFound) as excinfo:
        actual = accounts_service.get_account_by_greater_than(1, 500)
    assert str(excinfo.value) == "No account(s) with amount greater than 500 was found"

def test_get_account_by_greater_than_negative_multiple(mocker):
    def mock_get_account_by_greater_than(self, customer_id, amount_greater_than):
        if amount_greater_than > 500:
            return [Accounts(1, 200, 1, 1), Accounts(2, 300, 1, 2)]
        else:
            return None
    mocker.patch("dao.accounts_dao.AccountsDao.get_account_by_greater_than", mock_get_account_by_greater_than)
    accounts_service = AccountsService()
    with pytest.raises(ae.AccountNotFound) as excinfo:
        actual = accounts_service.get_account_by_greater_than(1, 500)
    assert str(excinfo.value) == "No account(s) with amount greater than 500 was found"

def test_get_account_by_less_than_positive(mocker):
    def mock_get_account_by_less_than(self, customer_id, amount_less_than):
        if amount_less_than <= 2000:
            return Accounts(1, 1000, 1, 1)
        else:
            return None
    mocker.patch("dao.accounts_dao.AccountsDao.get_account_by_less_than", mock_get_account_by_less_than)
    accounts_service = AccountsService()
    actual = accounts_service.get_account_by_less_than(1, 2000)
    assert actual == {
        "id": 1,
        "balance": 1000,
        "customer_id": 1,
        "account_type_id": 1
    }

def test_get_account_by_less_positive_multiple(mocker):
    def mock_get_account_by_less_than(self, customer_id, amount_less_than):
        if amount_less_than <= 2000:
            return [Accounts(1, 1000, 1, 1), Accounts(2, 1500, 1, 2)]
        else:
            return None
    mocker.patch("dao.accounts_dao.AccountsDao.get_account_by_less_than", mock_get_account_by_less_than)
    accounts_service = AccountsService()
    actual = accounts_service.get_account_by_less_than(1, 2000)
    assert actual == [
        {
            "id": 1,
            "balance": 1000,
            "customer_id": 1,
            "account_type_id": 1
        },
        {
            "id": 2,
            "balance": 1500,
            "customer_id": 1,
            "account_type_id": 2
        }
    ]

def test_get_account_by_less_than_negative(mocker):
    def mock_get_account_by_less_than(self, customer_id, amount_less_than):
        if amount_less_than < 2000:
            return Accounts(1, 5000, 1, 1)
        else:
            return None
    mocker.patch("dao.accounts_dao.AccountsDao.get_account_by_less_than", mock_get_account_by_less_than)
    accounts_service = AccountsService()
    with pytest.raises(ae.AccountNotFound) as excinfo:
        actual = accounts_service.get_account_by_less_than(1, 2000)
    assert str(excinfo.value) == "No account(s) with amount less than 2000 was found"

def test_get_account_by_less_than_negative_multiple(mocker):
    def mock_get_account_by_less_than(self, customer_id, amount_less_than):
        if amount_less_than < 2000:
            return [Accounts(1, 5000, 1, 1), Accounts(2, 20000, 1, 2)]
        else:
            return None
    mocker.patch("dao.accounts_dao.AccountsDao.get_account_by_less_than", mock_get_account_by_less_than)
    accounts_service = AccountsService()
    with pytest.raises(ae.AccountNotFound) as excinfo:
        actual = accounts_service.get_account_by_less_than(1, 2000)
    assert str(excinfo.value) == "No account(s) with amount less than 2000 was found"

def test_get_account_by_customer_and_account_id_positive(mocker):
    def mock_get_account_by_customer_and_account_id(self, customer_id, account_id):
        if customer_id == "1" and account_id == "1":
            return Accounts(1, 200, 1, 1)
        else:
            return None
    mocker.patch("dao.accounts_dao.AccountsDao.get_account_by_customer_and_account_id",
                 mock_get_account_by_customer_and_account_id)
    accounts_service = AccountsService()
    actual = accounts_service.get_account_by_customer_and_account_id("1", "1")
    assert actual == {
            "id": 1,
            "balance": 200,
            "customer_id": 1,
            "account_type_id": 1
        }

def test_get_account_by_customer_and_account_id_negative_customer_id(mocker):
    def mock_get_customer_by_id(self, customer_id):
        if customer_id == "1":
            return Customer(1, "test1a", "test1b")
        else:
            return None
    mocker.patch("dao.customer_dao.CustomerDao.get_customer_by_id", mock_get_customer_by_id)
    customer_service = CustomerService()
    with pytest.raises(ce.CustomerNotFound) as excinfo:
        actual = customer_service.get_customer_by_id("1000")
    assert str(excinfo.value) == "Customer with the id 1000 was not found"

def test_get_account_by_customer_and_account_id_negative_account_id(mocker):
    def mock_get_account_by_customer_and_account_id(self, customer_id, account_id):
        if account_id == "1":
            return Accounts(1, 200, 1, 1)
        else:
            return None
    mocker.patch("dao.accounts_dao.AccountsDao.get_account_by_customer_and_account_id",
                 mock_get_account_by_customer_and_account_id)
    accounts_service = AccountsService()
    with pytest.raises(ae.AccountNotFound) as excinfo:
        actual = accounts_service.get_account_by_customer_and_account_id(1, "1000")
    assert str(excinfo.value) == "Account with id 1000 was not found"

def test_add_account_to_customer_positive(mocker):
    def mock_get_account_by_customer_and_account_id(self, customer_id, account_id):
        if customer_id == "1" and account_id == "3":
            return None
    mocker.patch("dao.accounts_dao.AccountsDao.get_account_by_customer_and_account_id",
                 mock_get_account_by_customer_and_account_id)
    account_object_to_add = Accounts(None, 20000, 1, 2)

    def mock_add_account(self, account_object):
        if account_object == account_object_to_add:
            return Accounts(3, 20000, 1, 2)
        else:
            return None
    mocker.patch("dao.accounts_dao.AccountsDao.add_account_to_customer", mock_add_account)
    accounts_service = AccountsService()
    actual = accounts_service.add_account_to_customer(account_object_to_add)
    assert actual == {
        "id": 3,
        "balance": 20000,
        "customer_id": 1,
        "account_type_id": 2
    }

def test_add_account_to_customer_negative_balance(mocker):
    account_object_to_add = Accounts(None, -231, 1, 2)

    def mock_get_account_by_less_than(self, customer_id, amount_less_than):
        if amount_less_than <= 0:
            return Accounts(1, -231, 1, 2)
    mocker.patch("dao.accounts_dao.AccountsDao.get_account_by_less_than", mock_get_account_by_less_than)
    accounts_service = AccountsService()
    with pytest.raises(ae.AccountsNegativeBalance) as excinfo:
        actual = accounts_service.add_account_to_customer(account_object_to_add)
    assert str(excinfo.value) == "Cannot have a negative balance!"

def test_add_account_to_customer_negative_wrong_type(mocker):
    account_object_to_add = Accounts(None, 1000, 1, 6)

    def mock_get_account_by_account_type_id(self, customer_id, account_type_id):
        if account_type_id not in range(1, 3):
            return Accounts(1, 1000, 1, 6)
        mocker.patch("dao.accounts_dao.AccountsDao.get_account_by_account_type_id", mock_get_account_by_account_type_id)
        accounts_service = AccountsService()
        with pytest.raises(ae.AccountTypeError) as excinfo:
            actual = accounts_service.add_account_to_customer(account_object_to_add)
        assert str(excinfo.value) == "Not a savings or checking account!"

def test_update_acct_by_cust_and_acct_id_positive(mocker):
    update_account_object = Accounts(3, 10000, 1, 1)

    def mock_update_account(self, account_object):
        if account_object.id == 3:
            return Accounts(3, 10000, 1, 1)
        else:
            return None
    mocker.patch("dao.accounts_dao.AccountsDao.update_acct_by_cust_and_acct_id", mock_update_account)
    accounts_service = AccountsService()
    actual = accounts_service.update_acct_by_cust_and_acct_id(update_account_object)
    assert actual == {
        "id": 3,
        "balance": 10000,
        "customer_id": 1,
        "account_type_id": 1
    }

def test_update_acct_by_cust_and_acct_id_negative(mocker):
    update_account_object = Accounts(6, 10000, 1, 1)

    def mock_update_account(self, account_object):
        if account_object.id == 3:
            return Accounts(3, 10000, 1, 1)
        else:
            return None
    mocker.patch("dao.accounts_dao.AccountsDao.update_acct_by_cust_and_acct_id", mock_update_account)
    accounts_service = AccountsService()
    with pytest.raises(ae.AccountNotFound) as excinfo:
        actual = accounts_service.update_acct_by_cust_and_acct_id(update_account_object)
    assert str(excinfo.value) == " Account with id 6 was not found"

def test_delete_account_by_account_id_positive(mocker):

    def mock_delete_account_by_account_id(self, customer_id, account_id):
        if account_id == "1":
            return True
        else:
            return False
    mocker.patch("dao.accounts_dao.AccountsDao.delete_account_by_account_id", mock_delete_account_by_account_id)
    accounts_service = AccountsService()
    actual = accounts_service.delete_account_by_account_id(1, "1")
    assert actual is True

def test_delete_account_by_account_id_negative(mocker):

    def mock_delete_account_by_account_id(self, customer_id, account_id):
        if account_id == "2":
            return True
        else:
            return False
    mocker.patch("dao.accounts_dao.AccountsDao.delete_account_by_account_id", mock_delete_account_by_account_id)
    accounts_service = AccountsService()
    with pytest.raises(ae.AccountNotFound) as excinfo:
        accounts_service.delete_account_by_account_id(1, "60")
    assert str(excinfo.value) == "Account with id 60 for customer was not found"
