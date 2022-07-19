from dao.employee_dao import EmployeeDao
from dao.reimb_dao import ReimbDao
from model.reimbursement import Reimbursement
from exceptions.employee_not_found import EmployeeNotFound
from exceptions.reimb_not_found import ReimbNotFound
from exceptions.reimb_type_error import ReimbTypeError
from exceptions.reimb_status_error import ReimbStatusError
from exceptions.no_negative_amounts import ReimbNegativeError

class ReimbService:
    def __init__(self):
        self.employee_dao = EmployeeDao()
        self.reimb_dao = ReimbDao()

    def get_all_reimb_by_employee_id(self, employee_id):
        if self.employee_dao.get_employee_by_id(employee_id) is None:
            raise EmployeeNotFound(f"Employee with id {employee_id} was not found")
        return list(map(lambda y: y.to_dict(), self.reimb_dao.get_all_reimb_by_employee_id(employee_id)))

    def get_reimb_by_status(self, employee_id, status):
        list_of_reimbs = self.reimb_dao.get_reimbs_by_status(employee_id, status)
        if self.employee_dao.get_employee_by_id(employee_id) is None:
            raise EmployeeNotFound(f"Employee with id {employee_id} was not found")
        if not list_of_reimbs:
            raise ReimbNotFound(f"No reimbursement(s) with {status} status")
        if isinstance(list_of_reimbs, Reimbursement):
            return list_of_reimbs.to_dict()
        else:
            return list(map(lambda y: y.to_dict(), list_of_reimbs))

    def add_reimb_to_employee(self, reimb_object):
        if self.employee_dao.get_employee_by_id(reimb_object.employee_id) is None:
            raise EmployeeNotFound(f"Employee with id {reimb_object.employee_id} was not found")
        if int(reimb_object.amount) < 0:
            raise ReimbNegativeError("Cannot have a negative amount!")
        # if reimb_object.status != 'pending' or reimb_object.status != 'approved' or \
        #         reimb_object.status != 'denied':
        #     raise ReimbStatusError("Status for reimbursements must be pending, approved, or denied only!")
        # if reimb_object.reimb_type_id != 'A' or reimb_object.reimb_type_id != 'B' or \
        #         reimb_object.reimb_type_id != 'C' or reimb_object.reimb_type_id != 'D':
        #     raise ReimbTypeError("Reimbursement type can only be A: Lodging, B: Travel, C: Food, or D: Other")
        added_new_reimb = self.reimb_dao.add_reimb_to_employee(reimb_object)
        return added_new_reimb.to_dict()

    def update_reimb_by_ids(self, reimb_object):
        updated_reimb_object = self.reimb_dao.update_reimb_by_ids(reimb_object)
        # if updated_reimb_object is None:
        #     raise ReimbNotFound(f"Reimbursement with {reimb_object.id} was not found")

        return updated_reimb_object.to_dict()
