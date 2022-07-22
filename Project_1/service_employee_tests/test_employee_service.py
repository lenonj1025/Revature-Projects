import pytest

from exceptions.employee_registration import EmployeeRegisterError
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

def test_add_employee_positive(mocker):
    def mock_add_employee(username, password, first_name, last_name, gender, phone_number, email_address,
                          role_employee):
        if username == "username123" and password == "Password123!" and first_name == "TestA" and \
                last_name == "TestB" and gender == "Male" and phone_number == "000-000-0000" and \
                email_address == "username123@test.com" and role_employee == "employee":
            return None
    mocker.patch("dao.employee_dao.EmployeeDao.add_employee", mock_add_employee)
    employee_object_to_add = Employee(None, "username123", "Password123!", "TestA", "TestB", "Male", "000-000-0000",
                                      "username123@test.com", "employee")

    def mock_add_employee(self, employee_object):
        if employee_object == employee_object_to_add:
            return Employee(1, "username123", "Password123!", "TestA", "TestB", "Male", "000-000-0000",
                            "username123@test.com", "employee")
        else:
            return None
    mocker.patch("dao.employee_dao.EmployeeDao.add_employee", mock_add_employee)
    employee_service = EmployeeService()
    actual = employee_service.add_employee(employee_object_to_add)
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

def test_add_employee_negative_username_no_alphanumeric(mocker):
    def mock_add_employee(username, password, first_name, last_name, gender, phone_number, email_address,
                          role_employee):
        if username == "!@#!@#" and password == "Password123!" and first_name == "TestA" and \
                last_name == "TestB" and gender == "Male" and phone_number == "000-000-0000" and \
                email_address == "username123@test.com" and role_employee == "employee":
            return None
    mocker.patch("dao.employee_dao.EmployeeDao.add_employee", mock_add_employee)
    employee_object_to_add = Employee(None, "!@#!@#", "Password123!", "TestA", "TestB", "Male", "000-000-0000",
                                      "username123@test.com", "employee")

    def mock_add_employee(self, employee_object):
        if employee_object == employee_object_to_add:
            return Employee(1, "!@#!@#", "Password123!", "TestA", "TestB", "Male", "000-000-0000",
                            "username123@test.com", "employee")
        else:
            return None

    mocker.patch("dao.employee_dao.EmployeeDao.add_employee", mock_add_employee)
    employee_service = EmployeeService()
    employee_register_error = EmployeeRegisterError()
    employee_service.add_employee(employee_object_to_add)
    if not employee_object_to_add.username.isalnum():
        employee_register_error.messages.append("Username can only contain alphabetical and numerical characters")
    if len(employee_register_error.messages) > 0:
        raise employee_register_error
    with pytest.raises(EmployeeRegisterError) as excinfo:
        employee_service.add_employee(employee_object_to_add)
    assert str(excinfo.value) == "Username can only contain alphabetical and numerical characters"
#
# def test_add_employee_negative_username_length(mocker):
#     employee_object_to_add = Employee(None, "user", "Password123!", "TestA", "TestB", "Male", "000-000-0000",
#                                       "username123@test.com", "employee")
#     employee_service = EmployeeService()
#     with pytest.raises(EmployeeRegisterError) as excinfo:
#         actual = employee_service.add_employee(employee_object_to_add)
#     assert str(excinfo.value) == ''
#
# def test_add_employee_negative_username_no_blank(mocker):
#     employee_object_to_add = Employee(None, "user", " ", "TestA", "TestB", "Male", "000-000-0000",
#                                       "username123@test.com", "employee")
#     employee_service = EmployeeService()
#     with pytest.raises(EmployeeRegisterError) as excinfo:
#         actual = employee_service.add_employee(employee_object_to_add)
#     assert str(excinfo.value) == ''
#
# def test_add_employee_negative_employee_already_exists(mocker):
#     employee_object_to_add = Employee(None, "username123", "Password123!", "TestA", "TestB", "Male", "000-000-0000",
#                                       "username123@test.com", "employee")
#
#     def mock_get_employee_by_username(self, username):
#         if username == "username123":
#             return Employee(1, "username123", "Password123!", "TestA", "TestB", "Male", "000-000-0000",
#                             "username123@test.com", "employee")
#     mocker.patch("dao.employee_dao.EmployeeDao.get_employee_by_username", mock_get_employee_by_username)
#     employee_service = EmployeeService()
#     with pytest.raises(EmployeeRegisterError) as excinfo:
#         actual = employee_service.add_employee(employee_object_to_add)
#     assert str(excinfo.value) == ''
#
# def test_add_employee_negative_password_no_lowercase(mocker):
#     employee_object_to_add = Employee(None, "username123", "PASSWORD123!", "TestA", "TestB", "Male", "000-000-0000",
#                                       "username123@test.com", "employee")
#     employee_service = EmployeeService()
#     with pytest.raises(EmployeeRegisterError) as excinfo:
#         actual = employee_service.add_employee(employee_object_to_add)
#     assert str(excinfo.value) == ''
#
# def test_add_employee_negative_password_no_uppercase(mocker):
#     employee_object_to_add = Employee(None, "username123", "password123!", "TestA", "TestB", "Male", "000-000-0000",
#                                       "username123@test.com", "employee")
#     employee_service = EmployeeService()
#     with pytest.raises(EmployeeRegisterError) as excinfo:
#         actual = employee_service.add_employee(employee_object_to_add)
#     assert str(excinfo.value) == ''
#
# def test_add_employee_negative_password_no_special_characters(mocker):
#     employee_object_to_add = Employee(None, "username123", "PASSWORD123", "TestA", "TestB", "Male", "000-000-0000",
#                                       "username123@test.com", "employee")
#     employee_service = EmployeeService()
#     with pytest.raises(EmployeeRegisterError) as excinfo:
#         actual = employee_service.add_employee(employee_object_to_add)
#     assert str(excinfo.value) == ''
#
# def test_add_employee_negative_password_no_numerical(mocker):
#     employee_object_to_add = Employee(None, "username123", "PASSWORD!", "TestA", "TestB", "Male", "000-000-0000",
#                                       "username123@test.com", "employee")
#     employee_service = EmployeeService()
#     with pytest.raises(EmployeeRegisterError) as excinfo:
#         actual = employee_service.add_employee(employee_object_to_add)
#     assert str(excinfo.value) == ''
#
# def test_add_employee_negative_password_length(mocker):
#     employee_object_to_add = Employee(None, "username123", "Pa1!", "TestA", "TestB", "Male", "000-000-0000",
#                                       "username123@test.com", "employee")
#     employee_service = EmployeeService()
#     with pytest.raises(EmployeeRegisterError) as excinfo:
#         actual = employee_service.add_employee(employee_object_to_add)
#     assert str(excinfo.value) == ''
#
# def test_add_employee_negative_password_no_blank(mocker):
#     employee_object_to_add = Employee(None, "username123", " ", "TestA", "TestB", "Male", "000-000-0000",
#                                       "username123@test.com", "employee")
#     employee_service = EmployeeService()
#     with pytest.raises(EmployeeRegisterError) as excinfo:
#         actual = employee_service.add_employee(employee_object_to_add)
#     assert str(excinfo.value) == ''
#
# def test_add_employee_negative_first_name_no_alphabetical(mocker):
#     employee_object_to_add = Employee(None, "username123", "password123!", "1234", "TestB", "Male", "000-000-0000",
#                                       "username123@test.com", "employee")
#     employee_service = EmployeeService()
#     with pytest.raises(EmployeeRegisterError) as excinfo:
#         actual = employee_service.add_employee(employee_object_to_add)
#     assert str(excinfo.value) == ''
#
# def test_add_employee_negative_first_name_no_blank(mocker):
#     employee_object_to_add = Employee(None, "username123", "password123!", " ", "TestB", "Male", "000-000-0000",
#                                       "username123@test.com", "employee")
#     employee_service = EmployeeService()
#     with pytest.raises(EmployeeRegisterError) as excinfo:
#         actual = employee_service.add_employee(employee_object_to_add)
#     assert str(excinfo.value) == ''
#
# def test_add_employee_negative_last_name_no_alphabetical(mocker):
#     employee_object_to_add = Employee(None, "username123", "password123!", "TestA", "1234", "Male", "000-000-0000",
#                                       "username123@test.com", "employee")
#     employee_service = EmployeeService()
#     with pytest.raises(EmployeeRegisterError) as excinfo:
#         actual = employee_service.add_employee(employee_object_to_add)
#     assert str(excinfo.value) == ''
#
# def test_add_employee_negative_last_name_no_blank(mocker):
#     employee_object_to_add = Employee(None, "username123", "password123!", "TestA", " ", "Male", "000-000-0000",
#                                       "username123@test.com", "employee")
#     employee_service = EmployeeService()
#     with pytest.raises(EmployeeRegisterError) as excinfo:
#         actual = employee_service.add_employee(employee_object_to_add)
#     assert str(excinfo.value) == ''
#
# def test_add_employee_negative_gender(mocker):
#     employee_object_to_add = Employee(None, "username123", "password123!", "TestA", "TestB", "1234", "000-000-0000",
#                                       "username123@test.com", "employee")
#     employee_service = EmployeeService()
#     with pytest.raises(EmployeeRegisterError) as excinfo:
#         actual = employee_service.add_employee(employee_object_to_add)
#     assert str(excinfo.value) == ''
#
# def test_add_employee_negative_phone_number_format(mocker):
#     employee_object_to_add = Employee(None, "username123", "password123!", "TestA", "TestB", "Male", "0000000000",
#                                       "username123@test.com", "employee")
#     employee_service = EmployeeService()
#     with pytest.raises(EmployeeRegisterError) as excinfo:
#         actual = employee_service.add_employee(employee_object_to_add)
#     assert str(excinfo.value) == ''
#
# def test_add_employee_negative_phone_number_blank(mocker):
#     employee_object_to_add = Employee(None, "username123", "password123!", "TestA", "TestB", "Male", " ",
#                                       "username123@test.com", "employee")
#     employee_service = EmployeeService()
#     with pytest.raises(EmployeeRegisterError) as excinfo:
#         actual = employee_service.add_employee(employee_object_to_add)
#     assert str(excinfo.value) == ''
#
# def test_add_employee_negative_email_address_format(mocker):
#     employee_object_to_add = Employee(None, "username123", "password123!", "TestA", "TestB", "Male", "000-000-0000",
#                                       "username123@test", "employee")
#     employee_service = EmployeeService()
#     with pytest.raises(EmployeeRegisterError) as excinfo:
#         actual = employee_service.add_employee(employee_object_to_add)
#     assert str(excinfo.value) == ''
#
# def test_add_employee_negative_email_address_already_exists(mocker):
#     employee_object_to_add = Employee(None, "username123", "Password123!", "TestA", "TestB", "Male", "000-000-0000",
#                                       "username123@test.com", "employee")
#
#     def mock_get_employee_by_email(self, email_address):
#         if email_address == "username123@test.com":
#             return Employee(1, "username123", "Password123!", "TestA", "TestB", "Male", "000-000-0000",
#                             "username123@test.com", "employee")
#     mocker.patch("dao.employee_dao.EmployeeDao.get_employee_by_email", mock_get_employee_by_email)
#     employee_service = EmployeeService()
#     with pytest.raises(EmployeeRegisterError) as excinfo:
#         actual = employee_service.add_employee(employee_object_to_add)
#     assert str(excinfo.value) == ''
#
# def test_add_employee_negative_email_address_no_blank(mocker):
#     employee_object_to_add = Employee(None, "username123", "password123!", "TestA", "TestB", "Male", "000-000-0000",
#                                       " ", "employee")
#     employee_service = EmployeeService()
#     with pytest.raises(EmployeeRegisterError) as excinfo:
#         actual = employee_service.add_employee(employee_object_to_add)
#     assert str(excinfo.value) == ''

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

# def test_login_positive(mocker):
#     def mock_login(self, username, password):
#         if username == "username123" and password == "password123":
#             return None
#     mocker.patch("dao.customer_dao.CustomerDao.add_customer", mock_add_customer_by_name)
#     customer_object_to_add = Customer(None, "test123a", "test123b")
