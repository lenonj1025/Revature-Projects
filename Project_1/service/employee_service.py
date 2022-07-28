from dao.employee_dao import EmployeeDao
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

    # def get_employee_by_username(self, username):
    #     employee_object = self.employee_dao.get_employee_by_username(username)
    #     if not employee_object:
    #         raise EmployeeNotFound(f"Employee with username {username} was not found")
    #     return employee_object.to_dict()

    def login(self, username, password):
        employee_object = self.employee_dao.get_employee_by_username_and_password(username, password)
        if employee_object is None:
            raise LoginError("Invalid username and/or password")
        return employee_object.to_dict()

    def update_employee_by_id(self, employee_object):
        updated_employee_object = self.employee_dao.update_employee_by_id(employee_object)
        if updated_employee_object is None:
            raise EmployeeNotFound(f"Customer with id {employee_object.id} was not found")

        return updated_employee_object.to_dict()
