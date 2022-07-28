import pytest
from service.employee_service import EmployeeService
from model.employee import Employee
from exceptions.employee_not_found import EmployeeNotFound

def test_get_employee_by_id_positive(mocker):
    def mock_get_employee_by_id(self, employee_id):
        if employee_id == "1":
            return Employee(1, "username123", "password123", "Test1A", "Test1B", "Male", "000-000-0000",
                            "test123@test.com", "employee")
        else:
            return None
    mocker.patch("dao.employee_dao.EmployeeDao.get_employee_by_id", mock_get_employee_by_id)
    employee_service = EmployeeService()
    actual = employee_service.get_employee_by_id("1")
    assert actual == {
        "id": 1,
        "username": "username123",
        "password": "password123",
        "first_name": "Test1A",
        "last_name": "Test1B",
        "gender": "Male",
        "phone_number": "000-000-0000",
        "email_address": "test123@test.com",
        "role_employee": "employee"
    }

def test_get_employee_by_id_negative(mocker):
    def mock_get_employee_by_id(self, employee_id):
        if employee_id == "1":
            return Employee(1, "username123", "password123", "Test1A", "Test1B", "Male", "000-000-0000",
                            "test123@test.com", "employee")
        else:
            return None
    mocker.patch("dao.employee_dao.EmployeeDao.get_employee_by_id", mock_get_employee_by_id)
    employee_service = EmployeeService()
    with pytest.raises(EmployeeNotFound) as excinfo:
        employee_service.get_employee_by_id("1000")
    assert str(excinfo.value) == "Employee with the id 1000 was not found"

def test_update_employee_by_id_positive(mocker):
    updated_employee_object = Employee(1, "username123", "Password123!", "TestA", "TestB", "Male", "000-000-0000",
                                       "username123@test.com", "employee")

    def mock_update_employee_by_id(self, employee_object):
        if employee_object.id == 1:
            return Employee(1, "username123", "Password123!", "TestA", "TestB", "Male", "000-000-0000",
                            "username123@test.com", "employee")
        else:
            return None
    mocker.patch("dao.employee_dao.EmployeeDao.update_employee_by_id", mock_update_employee_by_id)
    employee_service = EmployeeService()
    actual = employee_service.update_employee_by_id(updated_employee_object)
    assert actual == {
        "id": 1,
        "username": "username123",
        "password": "Password123!",
        "first_name": "TestA",
        "last_name": "TestB",
        "gender": "Male",
        "phone_number": "000-000-0000",
        "email_address": "username123@test.com",
        "role_employee": "employee"
    }

def test_update_employee_by_id_negative(mocker):
    updated_employee_object = Employee(10, "username123", "Password123!", "TestA", "TestB", "Male", "000-000-0000",
                                       "username123@test.com", "employee")

    def mock_update_employee_by_id(self, employee_object):
        if employee_object.id == 1:
            return Employee(1, "username123", "Password123!", "TestA", "TestB", "Male", "000-000-0000",
                            "username123@test.com", "employee")
        else:
            return None
    mocker.patch("dao.employee_dao.EmployeeDao.update_employee_by_id", mock_update_employee_by_id)
    employee_service = EmployeeService()
    with pytest.raises(EmployeeNotFound) as excinfo:
        employee_service.update_employee_by_id(updated_employee_object)
    assert str(excinfo.value) == "Customer with id 10 was not found"

def test_login_positive(mocker):
    def mock_login(self, username, password):
        if username == "username123" and password == "password123":
            return Employee(1, "username123", "password123", "Test1A", "Test1B", "Male", "000-000-0000",
                            "test123@test.com", "employee")
        else:
            return None
    mocker.patch("dao.employee_dao.EmployeeDao.get_employee_by_username_and_password", mock_login)
    employee_service = EmployeeService()
    actual = employee_service.login("username123", "password123")
    assert actual == {
        "id": 1,
        "username": "username123",
        "password": "password123",
        "first_name": "Test1A",
        "last_name": "Test1B",
        "gender": "Male",
        "phone_number": "000-000-0000",
        "email_address": "test123@test.com",
        "role_employee": "employee"
    }