class Reimbursement:
    def __init__(self, id, amount, submitted, resolved, status, reimb_type_id, description, receipt, employee_id,
                 resolver_id):
        self.id = id
        self.amount = amount
        self.submitted = submitted
        self.resolved = resolved
        self.status = status
        self.reimb_type_id = reimb_type_id
        self.description = description
        self.receipt = receipt
        self.employee_id = employee_id
        self.resolver_id = resolver_id

    def to_dict(self):
        return {
            "id": self.id,
            "amount": self.amount,
            "submitted": self.submitted,
            "resolved": self.resolved,
            "status": self.status,
            "reimb_type_id": self.reimb_type_id,
            "description": self.description,
            "receipt": self.receipt,
            "employee_id": self.employee_id,
            "resolver_id": self.resolver_id
        }