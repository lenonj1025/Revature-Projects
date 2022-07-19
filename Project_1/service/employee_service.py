import re
from dao.employee_dao import EmployeeDao
from exceptions.employee_registration import EmployeeRegisterError
from exceptions.employee_not_found import EmployeeNotFound
from exceptions.login_error import LoginError
from exceptions.employee_not_found import EmployeeNotFound

class EmployeeService:
    def __init__(self):
        self.employee_dao = EmployeeDao()

    def get_employee_by_id(self, employee_id):
        employee_object = self.employee_dao.get_employee_by_id(employee_id)
        if not employee_object:
            raise EmployeeNotFound(f"Employee with the id {employee_id} was not found")
        return employee_object.to_dict()

    # def get_all_employees(self):
    #     list_of_employees = self.employee_dao.get_all_employees()
    #
    #     return list(map(lambda y: y.to_dict(), list_of_employees))
    #
    # def get_employee_by_username(self, username):
    #     employee_object = self.employee_dao.get_employee_by_username(username)
    #     if not employee_object:
    #         raise EmployeeNotFound(f"Employee with username {username} was not found")
    #     return employee_object.to_dict()
    #
    # def get_employee_by_email(self, email_address):
    #     employee_object = self.employee_dao.get_employee_by_email(email_address)
    #     if not employee_object:
    #         raise EmployeeNotFound(f"Employee with username {email_address} was not found")
    #     return employee_object.to_dict()

    def login(self, username, password):
        employee_object = self.employee_dao.get_employee_by_username_and_password(username, password)
        # if employee_object is None:
        #     raise LoginError("Invalid username and/or password")
        return employee_object.to_dict()

    def add_employee(self, employee_object):
        employee_register_error = EmployeeRegisterError()

        # Employee Username Validation
        if not employee_object.username.isalnum():
            employee_register_error.messages.append("Username can only contain alphabetical and numerical characters")
        if len(employee_object) < 6 or len(employee_object) > 20:
            employee_register_error.messages.append("Username can only be greater than 6 characters or "
                                                    "less than 20 characters")
        if self.employee_dao.get_employee_by_username(employee_object.username) is not None:
            employee_register_error.messages.append("Username is already taken. Create another username")
        if employee_object.username == '':
            employee_register_error.messages.append("Username cannot be blank")
        # Employee Password Validation
        alphabetical_characters = "abcdefghijklmnopqrstuvwxyz"
        special_characters = "!@#$%^&*"
        numeric_characters = "0123456789"

        lower_alpha_count = 0
        upper_alpha_count = 0
        special_character_count = 0
        numeric_character_count = 0
        for char in employee_object.password:
            if char in alphabetical_characters:
                lower_alpha_count += 1
            if char in alphabetical_characters.upper():
                upper_alpha_count += 1
            if char in special_characters:
                special_character_count += 1
            if char in numeric_characters:
                numeric_character_count += 1
        if lower_alpha_count == 0:
            employee_register_error.messages.append("Password must contain at least 1 lowercase character")
        if upper_alpha_count == 0:
            employee_register_error.messages.append("Password must contain at least 1 uppercase character")
        if special_character_count == 0:
            employee_register_error.messages.append("Password must contain at least 1 special (!@#$%^&*) character")
        if numeric_character_count == 0:
            employee_register_error.messages.append("Password must contain at least 1 numeric character")
        if len(employee_object.password) < 6 or len(employee_object.password) > 20:
            employee_register_error.messages.append("Password can only be greater than 6 characters or "
                                                    "less than 20 characters")
        if len(employee_object.password) != lower_alpha_count + upper_alpha_count + \
                special_character_count + numeric_character_count:
            employee_register_error.messages.append("Password can contain only alphabetical, "
                                                    "numerical and special characters")
        if employee_object.password == '':
            employee_register_error.messages.append("password cannot be blank")
        # Employee First Name Validation
        if not employee_object.first_name.isalpha():
            employee_register_error.messages.append("First name can contain only alphabetical characters")
        if employee_object.first_name == '':
            employee_register_error.messages.append("First name cannot be blank")
        # Employee Last Name Validation
        if not employee_object.last_name.isalpha():
            employee_register_error.messages.append("Last name can contain only alphabetical characters")
        if employee_object.ulast_name == '':
            employee_register_error.messages.append("Last name cannot be blank")
        # Employee Gender Validation
        if not (employee_object.gender == "Male" or employee_object.gender == "Female"
                or employee_object.gender == "Other"):
            employee_register_error.messages.append("Gender can only be male, female or other")
        # Employee Phone Number Validation
        if not re.fullmatch("\d{3}-\d{3}-\d{4}", employee_object.phone_number):
            employee_register_error.messages.append("Phone number can only be of the format XXX-XXX-XXXX")
        if employee_object.phone_number == '':
            employee_register_error.messages.append("Phone number cannot be blank")
        # Employee Email Address Validation
        if not re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', employee_object.email_address):
            employee_register_error.messages.append("Email address can only be of the format <username>@<domain>")
        if self.employee_dao.get_employee_by_email(employee_object.email_address) is not None:
            employee_register_error.messages.append("Email address is already taken")
        if employee_object.email_address == '':
            employee_register_error.messages.append("Email address cannot be blank")

        if len(employee_register_error.messages) > 0:
            raise employee_register_error

        added_employee_obj = self.employee_dao.add_employee(employee_object)

        return added_employee_obj.to_dict()
