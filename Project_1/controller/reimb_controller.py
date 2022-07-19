from flask import Blueprint, request
from service.reimb_service import ReimbService
from controller.employee_controller import loginstatus
from exceptions.employee_not_found import EmployeeNotFound
from exceptions.reimb_not_found import ReimbNotFound

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
