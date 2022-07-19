from flask import Blueprint, request
from service.reimb_service import ReimbService
from model.reimbursement import Reimbursement
from controller.employee_controller import loginstatus
from exceptions.employee_not_found import EmployeeNotFound
from exceptions.reimb_not_found import ReimbNotFound
from exceptions.reimb_type_error import ReimbTypeError
from exceptions.reimb_status_error import ReimbStatusError

# add reimbursements
# update reimbursements (finance manager approving/denying)

reimb_control = Blueprint('reimb_controller', __name__)
reimb_service = ReimbService()

@reimb_control.route('/employee/<employee_id>/reimbursements', methods=['GET'])
def get_all_reimb_by_employee_id(employee_id):
    status = request.args.get('status')

    if status is not None:
        try:
            return {
                "reimbursements": reimb_service.get_reimb_by_status(employee_id, status)
            }
        except EmployeeNotFound as e:
            return {
                       "message": str(e)
                   }, 404
        except ReimbNotFound as e:
            return {
                       "message": str(e)
                   }, 404
    else:
        try:
            return {
                "reimbursements": reimb_service.get_all_reimb_by_employee_id(employee_id)
            }
        except EmployeeNotFound as e:
            return {
                       "message": str(e)
                   }, 404

@reimb_control.route('/employee/<employee_id>/reimbursements', methods=['POST'])
def add_reimb_to_employee(employee_id):
    reimb_json_dictionary = request.get_json()
    reimb_object = Reimbursement(None, reimb_json_dictionary['amount'], None, None, reimb_json_dictionary['status'],
                                 reimb_json_dictionary['reimb_type_id'], reimb_json_dictionary['description'],
                                 None, employee_id, None)
    try:
        return reimb_service.add_reimb_to_employee(reimb_object), 201
    except EmployeeNotFound as e:
        return{
            "message": str(e)
        }, 404
    except ReimbTypeError as e:
        return{
            "message": str(e)
        }, 404
    except ReimbStatusError as e:
        return{
            "message": str(e)
        }, 404

@reimb_control.route('/employee/<employee_id>/reimbursements/<reimbursements_id>', methods=['PUT'])
def update_reimb_by_ids(employee_id, reimbursements_id):
    try:
        reimb_json_dictionary = request.get_json()
        reimb_object = Reimbursement(reimbursements_id, None, None, None, reimb_json_dictionary['status'], None, None,
                                     None, employee_id, reimb_json_dictionary['resolver_id'])
        return reimb_service.update_reimb_by_ids(reimb_object), 201

    except EmployeeNotFound as e:
        return {
            "message": str(e)
        }, 404
    except ReimbNotFound as e:
        return {
            "message": str(e)
        }, 404
    except ReimbStatusError as e:
        return{
            "message": str(e)
        }, 404
