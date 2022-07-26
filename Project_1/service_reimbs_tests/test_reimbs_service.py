import pytest
from model.reimbursement import Reimbursement
from service.reimb_service import ReimbService
from exceptions.reimb_not_found import ReimbNotFound
from exceptions.no_negative_amounts import ReimbNegativeError

def test_get_all_reimb_by_employee_id_positive(mocker):
    def mock_get_all_reimb_by_employee_id(self, employee_id):
        return [Reimbursement(1, 1000, 10, 20, "denied", "Lodging", "Hotel for work meeting", None, 2, 3),
                Reimbursement(2, 1500, 11, 21, "approved", "Travel", "Gas", None, 2, 3)]

    mocker.patch('dao.reimb_dao.ReimbDao.get_all_reimb_by_employee_id', mock_get_all_reimb_by_employee_id)
    reimb_service = ReimbService()
    actual = reimb_service.get_all_reimb_by_employee_id(employee_id=2)
    assert actual == [
        {
            "id": 1,
            "amount": 1000,
            "submitted": 10,
            "resolved": 20,
            "status": "denied",
            "reimb_type_id": "Lodging",
            "description": "Hotel for work meeting",
            "receipt": None,
            "employee_id": 2,
            "resolver": 3,
        },
        {
            "id": 2,
            "amount": 1500,
            "submitted": 11,
            "resolved": 21,
            "status": "approved",
            "reimb_type_id": "Travel",
            "description": "Gas",
            "receipt": None,
            "employee_id": 2,
            "resolver": 3,
        }
    ]

def test_get_reimb_by_status_positive_pending(mocker):
    def mock_get_reimb_by_status(self, employee_id, status):
        if status == "pending" and employee_id == 2:
            return Reimbursement(1, 1000, 10, None, "pending", "Lodging", "Hotel for work meeting", None, 2, None)
        else:
            return None

    mocker.patch("dao.reimb_dao.ReimbDao.get_reimb_by_status", mock_get_reimb_by_status)
    reimb_service = ReimbService()
    actual = reimb_service.get_reimb_by_status(2, "pending")
    assert actual == {
            "id": 1,
            "amount": 1000,
            "submitted": 10,
            "resolved": None,
            "status": "pending",
            "reimb_type_id": "Lodging",
            "description": "Hotel for work meeting",
            "receipt": None,
            "employee_id": 2,
            "resolver": None,
        }

def test_get_reimb_by_status_positive_approved(mocker):
    def mock_get_reimb_by_status(self, employee_id, status):
        if status == "approved" and employee_id == 2:
            return Reimbursement(1, 1000, 10, None, "approved", "Lodging", "Hotel for work meeting", None, 2, None)
        else:
            return None

    mocker.patch("dao.reimb_dao.ReimbDao.get_reimb_by_status", mock_get_reimb_by_status)
    reimb_service = ReimbService()
    actual = reimb_service.get_reimb_by_status(2, "approved")
    assert actual == {
            "id": 1,
            "amount": 1000,
            "submitted": 10,
            "resolved": None,
            "status": "approved",
            "reimb_type_id": "Lodging",
            "description": "Hotel for work meeting",
            "receipt": None,
            "employee_id": 2,
            "resolver": None,
        }

def test_get_reimb_by_status_positive_approved_multiple(mocker):
    def mock_get_reimb_by_status(self, employee_id, status):
        if status == "approved" and employee_id == 2:
            return [Reimbursement(1, 1000, 10, 20, "approved", "Lodging", "Hotel for work meeting", None, 2, 3),
                    Reimbursement(2, 1500, 11, 21, "approved", "Travel", "Gas", None, 2, 3)]
        else:
            return None

    mocker.patch("dao.reimb_dao.ReimbDao.get_reimb_by_status", mock_get_reimb_by_status)
    reimb_service = ReimbService()
    actual = reimb_service.get_reimb_by_status(2, "approved")
    assert actual == [
        {
            "id": 1,
            "amount": 1000,
            "submitted": 10,
            "resolved": 20,
            "status": "approved",
            "reimb_type_id": "Lodging",
            "description": "Hotel for work meeting",
            "receipt": None,
            "employee_id": 2,
            "resolver": 3,
        },
        {
            "id": 2,
            "amount": 1500,
            "submitted": 11,
            "resolved": 21,
            "status": "approved",
            "reimb_type_id": "Travel",
            "description": "Gas",
            "receipt": None,
            "employee_id": 2,
            "resolver": 3,
        }
    ]

def test_get_reimb_by_status_positive_denied(mocker):
    def mock_get_reimb_by_status(self, employee_id, status):
        if status == "denied" and employee_id == 2:
            return Reimbursement(1, 1000, 10, None, "denied", "Lodging", "Hotel for work meeting", None, 2, None)
        else:
            return None

    mocker.patch("dao.reimb_dao.ReimbDao.get_reimb_by_status", mock_get_reimb_by_status)
    reimb_service = ReimbService()
    actual = reimb_service.get_reimb_by_status(2, "denied")
    assert actual == {
            "id": 1,
            "amount": 1000,
            "submitted": 10,
            "resolved": None,
            "status": "denied",
            "reimb_type_id": "Lodging",
            "description": "Hotel for work meeting",
            "receipt": None,
            "employee_id": 2,
            "resolver": None,
        }

def test_get_reimb_by_status_negative(mocker):
    def mock_get_reimb_by_status(self, employee_id, status):
        if status == "pending" and employee_id == 2:
            return Reimbursement(1, 1000, 10, 20, "denied", "Lodging", "Hotel for work meeting", None, 2, 3)
        else:
            return None

    mocker.patch("dao.reimb_dao.ReimbDao.get_reimb_by_status", mock_get_reimb_by_status)
    reimb_service = ReimbService()
    with pytest.raises(ReimbNotFound) as excinfo:
        reimb_service.get_reimb_by_status(1, "pending")
    assert str(excinfo.value) == "No reimbursement(s) with pending status"

def test_add_reimb_to_employee_positive(mocker):
    def mock_add_reimb_to_employee(amount, submitted, resolved, status, reimb_type_id,
                                        description, receipt, employee_id, resolver_id):
        if amount == 1000 and submitted == 10 and resolved is None and status == "pending" and \
            reimb_type_id == "Travel" and description == "gas" and receipt is None and employee_id == 2 and \
                resolver_id is None:
            return None
    mocker.patch("dao.reimb_dao.ReimbDao.add_reimb_to_employee", mock_add_reimb_to_employee)
    reimb_object_to_add = Reimbursement(None, 1000, 10, None, "pending", "Travel", "gas", None, 2, None)

    def mock_add_reimb_to_employee(self, reimb_object):
        if reimb_object == reimb_object_to_add:
            return Reimbursement(1, 1000, 10, None, "pending", "Travel", "gas", None, 2, None)
        else:
            return None

    mocker.patch("dao.reimb_dao.ReimbDao.add_reimb_to_employee", mock_add_reimb_to_employee)
    reimb_service = ReimbService()
    actual = reimb_service.add_reimb_to_employee(reimb_object_to_add)
    assert actual == {
        "id": 1,
        "amount": 1000,
        "submitted": 10,
        "resolved": None,
        "status": "pending",
        "reimb_type_id": "Travel",
        "description": "gas",
        "receipt": None,
        "employee_id": 2,
        "resolver_id": None
    }

def test_add_reimb_to_employee_negative_amount(mocker):
    reimb_object_to_add = Reimbursement(None, -1000, 10, None, "pending", "Travel", "gas", None, 2, None)

    def mock_add_reimb_to_employee(self, employee_id, amount):
        if amount <= 0:
            return Reimbursement(None, -1000, 10, None, "pending", "Travel", "gas", None, 2, None)
    mocker.patch("dao.reimb_dao.ReimbDao.add_reimb_to_employee", mock_add_reimb_to_employee)
    reimb_service = ReimbService()
    with pytest.raises(ReimbNegativeError) as excinfo:
        reimb_service.add_reimb_to_employee(reimb_object_to_add)
    assert str(excinfo.value) == "Cannot have a negative amount!"
