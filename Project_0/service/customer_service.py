from dao.customer_dao import CustomerDao
from exceptions.customer_not_found import CustomerNotFound

class CustomerService:

    def __init__(self):
        self.customer_dao = CustomerDao()

    def get_all_customers(self):
        list_of_customers = self.customer_dao.get_all_customers()

        return list(map(lambda y: y.to_dict(), list_of_customers))

    def get_customer_by_name(self, first_name, last_name):
        customer_object = self.customer_dao.get_customer_by_name(first_name, last_name)
        if not customer_object:
            raise CustomerNotFound(f"User with name {first_name} {last_name} was not found")

        return customer_object.to_dict()

    def get_customer_by_first_name(self, first_name):
        customer_object = self.customer_dao.get_customer_by_first_name(first_name)
        if not customer_object:
            raise CustomerNotFound(f"User with the first name {first_name} was not found")

        return customer_object.to_dict()

    def get_customer_by_last_name(self, last_name):
        customer_object = self.customer_dao.get_customer_by_last_name(last_name)
        if not customer_object:
            raise CustomerNotFound(f"User with the last name {last_name} was not found")

        return customer_object.to_dict()

    def get_customer_by_id(self, customer_id):
        customer_object = self.customer_dao.get_customer_by_id(customer_id)
        if not customer_object:
            raise CustomerNotFound(f"User with the id {customer_id} was not found")

        return customer_object.to_dict()
