from flask import Blueprint, request
from service.employee_service import EmployeeService
from model.employee import Employee
from exceptions.employee_registration import EmployeeRegisterError
from exceptions.employee_not_found import EmployeeNotFound

employee_control = Blueprint('employee_control', __name__)
employee_service = EmployeeService()

@employee_control.route('/employees', methods=['GET'])
def get_all_employees():
    return {
        "employees": employee_service.get_all_employees()
    }

@employee_control.route('/employees/<username>', methods=['GET'])
def get_employee_by_username(username):
    try:
        return employee_service.get_employee_by_username(username)
    except EmployeeNotFound as e:
        return{
            "message": str(e)
        }, 404

@employee_control.route('/employee', methods=['POST'])
def add_employee():
    employee_body_dict = request.get_json()

    username = employee_body_dict.get('username')
    password = employee_body_dict.get('password')
    first_name = employee_body_dict.get('first_name')
    last_name = employee_body_dict.get('last_name')
    phone_number = employee_body_dict.get('phone_number')
    email_address = employee_body_dict.get('email_address')

    try:
        added_employee = employee_service.add_employee(Employee(username, password, first_name, last_name,
                                                                phone_number, email_address))
    except EmployeeRegisterError as e:
        return {
            "messages": e.messages
        }

    return added_employee, 201
