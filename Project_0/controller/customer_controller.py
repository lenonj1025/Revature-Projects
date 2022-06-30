from flask import Blueprint, request
from service.customer_service import CustomerService
from exceptions.invalid_customer_name import InvalidCustomerName
from exceptions.customer_not_found import CustomerNotFound
from modelcu.customer import Customer

cust_control = Blueprint('customer_controller', __name__)
customer_service = CustomerService()
# GET /customers: get all customers
# GET /customer/<customer_id>: get customers by id
# PUT /customers: create new customer
# PUT /customer/<customer_id>: Update customer by id
# DELETE /customer/<customer_id>: Delete customer by id

@cust_control.route('/customers', methods=['GET'])
def get_all_customers():
    return {
        "customers": customer_service.get_all_customers()
    }

# @cust_control.route('/customers/users', methods=['GET'])
# def get_customers_by_specifics():
#     first_name = request.args.get('firstname')
#     last_name = request.args.get('lastname')
#
#     if None not in (first_name, last_name):
#         try:
#             return customer_service.get_customer_by_name(first_name, last_name)
#         except CustomerNotFound as e:
#             return {
#                        "message": str(e)
#                    }, 404
#     elif first_name is not None:
#         try:
#             return {
#                 "customers": customer_service.get_customer_by_first_name(first_name)
#             }
#         except CustomerNotFound as e:
#             return {
#                        "message": str(e)
#                    }, 404
#     elif last_name is not None:
#         try:
#             return {
#                 "customers": customer_service.get_customer_by_last_name(last_name)
#             }
#         except CustomerNotFound as e:
#             return {
#                        "message": str(e)
#                    }, 404
#     elif first_name is None and last_name is None:
#         return{
#             CustomerNotFound
#         }, 404

@cust_control.route('/customers/<first_name>_<last_name>', methods=['GET'])
def get_customer_by_name(first_name, last_name):
    try:
        return customer_service.get_customer_by_name(first_name, last_name)
    except CustomerNotFound as e:
        return{
            "message": str(e)
        }, 404

@cust_control.route('/customers/usersf', methods=['GET'])
def get_customer_by_first_name():
    first_name = request.args.get('firstname')
    try:
        return {
            "customers": customer_service.get_customer_by_first_name(first_name)
        }
    except CustomerNotFound as e:
        return{
            "message": str(e)
        }, 404

@cust_control.route('/customers/usersl', methods=['GET'])
def get_customer_by_last_name():
    last_name = request.args.get('lastname')
    try:
        return {
            "customers": customer_service.get_customer_by_last_name(last_name)
        }
    except CustomerNotFound as e:
        return{
            "message": str(e)
        }, 404

@cust_control.route('/customers/<customer_id>', methods=['GET'])
def get_customer_by_id(customer_id):
    try:
        return customer_service.get_customer_by_id(customer_id)
    except CustomerNotFound as e:
        return{
            "message": str(e)
        }, 404

@cust_control.route('/customers', methods=['POST'])
def add_customer():
    customer_json_dictionary = request.get_json()
    customer_object = Customer(None, customer_json_dictionary['first_name'],
                               customer_json_dictionary['last_name'], None)
    try:
        return customer_service.add_customer(customer_object), 201
    except InvalidCustomerName as e:
        return{
            "message": str(e)
        }, 400
