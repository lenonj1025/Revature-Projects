import dao.customer_dao
from modelcu.customer import Customer
from service.customer_service import CustomerService
import exceptions.customer_exceptions as ce
import pytest

def test_get_all_customers(mocker):
    def mock_get_all_customers(self):
        return [Customer(1, 'test1a', 'test1b'), Customer(2, 'test2a', 'test2b'), Customer(3, 'test3a', 'test3b')]
    mocker.patch('dao.customer_dao.CustomerDao.get_all_customers', mock_get_all_customers)
    customer_service = CustomerService()
    actual = customer_service.get_all_customers()
    assert actual == [
        {
            "id": 1,
            "first_name": "test1a",
            "last_name": "test1b"
        },
        {
            "id": 2,
            "first_name": "test2a",
            "last_name": "test2b"
        },
        {
            "id": 3,
            "first_name": "test3a",
            "last_name": "test3b"
        }
    ]

def test_get_customer_by_name_positive(mocker):
    def mock_get_customer_by_name(self, first_name, last_name):
        if first_name == "test1a" and last_name == "test1b":
            return Customer(1, "test1a",  "test1b")
        else:
            return None
    mocker.patch("dao.customer_dao.CustomerDao.get_customer_by_name", mock_get_customer_by_name)
    customer_service = CustomerService()
    actual = customer_service.get_customer_by_name("test1a", "test1b")
    assert actual == {
        "id": 1,
        "first_name": "test1a",
        "last_name": "test1b"
    }

def test_get_customer_by_name_negative(mocker):
    def mock_get_customer_by_name(self, first_name, last_name):
        if first_name == "test1a" and last_name == "test1b":
            return Customer(1, "test1a", "test1b")
        else:
            return None
    mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_name', mock_get_customer_by_name)
    customer_service = CustomerService()
    with pytest.raises(ce.CustomerNotFound) as excinfo:
        actual = customer_service.get_customer_by_name("test2a", "test2b")
    assert str(excinfo.value) == "Customer with name test2a test2b was not found"

def test_get_customer_by_first_name_positive(mocker):
    def mock_get_customer_by_first_name(self, first_name):
        if first_name == "test1a":
            return [Customer(1, "test1a", "test1b")]
        else:
            return None
    mocker.patch("dao.customer_dao.CustomerDao.get_customer_by_first_name", mock_get_customer_by_first_name)
    customer_service = CustomerService()
    actual = customer_service.get_customer_by_first_name("test1a")
    assert actual == [{
        "id": 1,
        "first_name": "test1a",
        "last_name": "test1b"
    }]

def test_get_customer_by_first_name_negative(mocker):

    def mock_get_customer_by_first_name(self, first_name):
        if first_name == "test1a":
            return [Customer(1, "test1a", "test1b")]
        else:
            return None

    mocker.patch("dao.customer_dao.CustomerDao.get_customer_by_first_name", mock_get_customer_by_first_name)

    customer_service = CustomerService()

    with pytest.raises(ce.CustomerNotFound) as excinfo:
        actual = customer_service.get_customer_by_first_name("test2a")

    assert str(excinfo.value) == "Customer with first name test2a was not found"

def test_get_customer_by_last_name_positive(mocker):
    def mock_get_customer_by_last_name(self, last_name):
        if last_name == "test1b":
            return [Customer(1, "test1a", "test1b")]
        else:
            return None
    mocker.patch("dao.customer_dao.CustomerDao.get_customer_by_last_name", mock_get_customer_by_last_name)
    customer_service = CustomerService()
    actual = customer_service.get_customer_by_last_name("test1b")
    assert actual == [{
        "id": 1,
        "first_name": "test1a",
        "last_name": "test1b"
    }]

def test_get_customer_by_last_name_negative(mocker):

    def mock_get_customer_by_last_name(self, last_name):
        if last_name == "test1b":
            return [Customer(1, "test1a", "test1b")]
        else:
            return None

    mocker.patch("dao.customer_dao.CustomerDao.get_customer_by_last_name", mock_get_customer_by_last_name)

    customer_service = CustomerService()

    with pytest.raises(ce.CustomerNotFound) as excinfo:
        actual = customer_service.get_customer_by_last_name("test2b")

    assert str(excinfo.value) == "Customer with last name test2b was not found"

def test_get_customer_by_id_positive(mocker):
    def mock_get_customer_by_id(self, customer_id):
        if customer_id == "1":
            return Customer(1, "test1a", "test1b")
        else:
            return None
    mocker.patch("dao.customer_dao.CustomerDao.get_customer_by_id", mock_get_customer_by_id)
    customer_service = CustomerService()
    actual = customer_service.get_customer_by_id("1")
    assert actual == {
        "id": 1,
        "first_name": "test1a",
        "last_name": "test1b"
    }

def test_get_customer_by_id_negative(mocker):
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

def test_add_customer(mocker):
    def mock_add_customer_by_name(self, first_name, last_name):
        if first_name == "test123a" and last_name == "test123b":
            return None
    mocker.patch("dao.customer_dao.CustomerDao.add_customer", mock_add_customer_by_name)
    customer_object_to_add = Customer(None, "test123a", "test123b")

    def mock_add_customer(self, customer_object):
        if customer_object == customer_object_to_add:
            return Customer(1, "test123a", "test123b")
        else:
            return None
    mocker.patch("dao.customer_dao.CustomerDao.add_customer", mock_add_customer)
    customer_service = CustomerService()
    actual = customer_service.add_customer(customer_object_to_add)
    assert actual == {
        "id": 1,
        "first_name": "test123a",
        "last_name": "test123b"
    }

def test_add_customer_negative_name_contains_spaces(mocker):
    customer_object_to_add = Customer(None, "  test123a  ", "test123b")
    customer_service = CustomerService()
    with pytest.raises(ce.InvalidCustomerName) as excinfo:
        actual = customer_service.add_customer(customer_object_to_add)
    assert str(excinfo.value) == "First name and Last name cannot contain spaces!"

def test_add_customer_negative_first_name_less_than_2_characters(mocker):
    customer_object_to_add = Customer(None, "t", "test123b")
    customer_service = CustomerService()
    with pytest.raises(ce.InvalidCustomerName) as excinfo:
        actual = customer_service.add_customer(customer_object_to_add)
    assert str(excinfo.value) == "First name must be at least two characters"

def test_add_customer_negative_last_name_less_than_2_characters(mocker):
    customer_object_to_add = Customer(None, "test123a", "t")
    customer_service = CustomerService()
    with pytest.raises(ce.InvalidCustomerName) as excinfo:
        actual = customer_service.add_customer(customer_object_to_add)
    assert str(excinfo.value) == "Last name must be at least two characters"

def test_add_customer_negative_customer_already_exists(mocker):
    customer_object_to_add = Customer(None, "test123a", "test123b")

    def mock_get_customer_by_name(self, first_name, last_name):
        if first_name == "test123a" and last_name == "test123b":
            return Customer(1, "test123a", "test123b")
    mocker.patch("dao.customer_dao.CustomerDao.get_customer_by_name", mock_get_customer_by_name)
    customer_service = CustomerService()
    with pytest.raises(ce.CustomerAlreadyExists) as excinfo:
        actual = customer_service.add_customer(customer_object_to_add)
    assert str(excinfo.value) == f"Customer with name {customer_object_to_add.first_name} {customer_object_to_add.last_name} already exists"

def test_update_customer_by_id_positive(mocker):
    updated_customer_object = Customer(1, "test123a", "test123b")

    def mock_update_customer_by_id(self, customer_object):
        if customer_object.id == 1:
            return Customer(1, "test123a", "test123b")
        else:
            return None
    mocker.patch("dao.customer_dao.CustomerDao.update_customer_by_id", mock_update_customer_by_id)
    customer_service = CustomerService()
    actual = customer_service.update_customer_by_id(updated_customer_object)
    assert actual == {
        "id": 1,
        "first_name": "test123a",
        "last_name": "test123b"
    }

def test_update_customer_by_id_negative(mocker):
    updated_customer_object = Customer(10, "test123a", "test123b")

    def mock_update_customer_by_id(self, customer_object):
        if customer_object.id == 1:
            return Customer(1, "test123a", "test123b")
        else:
            return None
    mocker.patch("dao.customer_dao.CustomerDao.update_customer_by_id", mock_update_customer_by_id)
    customer_service = CustomerService()
    with pytest.raises(ce.CustomerNotFound) as excinfo:
        actual = customer_service.update_customer_by_id(updated_customer_object)
    assert str(excinfo.value) == "Customer with id 10 was not found"

def test_delete_customer_by_id_positive(mocker):
    def mock_delete_customer_by_id(self, customer_id):
        if customer_id == "1":
            return True
        else:
            return False
    mocker.patch("dao.customer_dao.CustomerDao.delete_customer_by_id", mock_delete_customer_by_id)
    customer_service = CustomerService()
    actual = customer_service.delete_customer_by_id("1")
    assert actual is None

def test_delete_customer_by_id_negative(mocker):
    def mock_delete_customer_by_id(self, customer_id):
        if customer_id == "1":
            return True
        else:
            return False
    mocker.patch("dao.customer_dao.CustomerDao.delete_customer_by_id", mock_delete_customer_by_id)
    customer_service = CustomerService()
    with pytest.raises(ce.CustomerNotFound) as excinfo:
        customer_service.delete_customer_by_id("100")
    assert str(excinfo.value) == "Customer with id 100 was not found"
