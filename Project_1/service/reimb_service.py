from dao.employee_dao import EmployeeDao
from dao.reimb_dao import ReimbDao
from model.reimbursement import Reimbursement
from exceptions.employee_not_found import EmployeeNotFound
from exceptions.reimb_not_found import ReimbNotFound

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
