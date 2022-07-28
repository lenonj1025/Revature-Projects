from flask import Blueprint, request, session

from service.employee_service import EmployeeService
from model.employee import Employee
from exceptions.login_error import LoginError
from exceptions.employee_not_found import EmployeeNotFound

employee_control = Blueprint('employee_control', __name__)
employee_service = EmployeeService()

@employee_control.route('/employees/<employee_id>', methods=['GET'])
def get_employee_by_id(employee_id):
    try:
        return employee_service.get_employee_by_id(employee_id)
    except EmployeeNotFound as e:
        return{
            "message": str(e)
        }, 404

# @employee_control.route('/employees/<username>', methods=['GET'])
# def get_employee_by_username(username):
#     username = request.args.get('username')
#     try:
#         return employee_service.get_employee_by_username(username)
#     except EmployeeNotFound as e:
#         return {
#             "message": str(e)
#         }, 404

@employee_control.route('/loginstatus', methods=['GET'])
def loginstatus():
    if session.get('employee_info') is not None:
        return {
            "message": "You are currently logged in",
            "logged_in_employee": session.get('employee_info')
        }, 200
    else:
        return {
            "message": "You are currently not logged in"
        }, 200

@employee_control.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return {
        "message": "You successfully logged out"
    }, 200

@employee_control.route('/login', methods=['POST'])
def login():
    login_body_dict = request.get_json()

    username = login_body_dict['username']
    password = login_body_dict['password']

    try:
        employee_dict = employee_service.login(username, password)
        session['employee_info'] = employee_dict
        return employee_dict, 200
    except LoginError as e:
        return {
            "message": str(e)
        }, 400

@employee_control.route('/employees/<employee_id>', methods=['PUT'])
def update_customer_by_id(employee_id):
    try:
        employee_body_dict = request.get_json()
        return employee_service.update_employee_by_id(Employee(employee_id, employee_body_dict['username'],
                                                               employee_body_dict['password'],
                                                               employee_body_dict['first_name'],
                                                               employee_body_dict['last_name'],
                                                               employee_body_dict['gender'],
                                                               employee_body_dict['phone_number'],
                                                               employee_body_dict['email_address'],
                                                               employee_body_dict['role_employee']))
    except EmployeeNotFound as e:
        return{
            "message": str(e)
        }, 404
