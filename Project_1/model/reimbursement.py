class Reimbursement:
    def __init__(self, id, amount, submitted, resolved, status, reimb_type_id, description, receipt, author, resolver):
        self.id = id
        self.amount = amount
        self.submitted = submitted
        self.resolved = resolved
        self.status = status
        self.reimb_type_id = reimb_type_id
        self.description = description
        self.receipt = receipt
        self.author = author
        self.resolver = resolver

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
            "author": self.author,
            "resolver": self.resolver
        }