from flask import Blueprint, request
from service.customer_service import CustomerService
from exceptions.invalid_customer_name import InvalidCustomerName
from exceptions.customer_not_found import CustomerNotFound
from modelcu.customer import Customer

cust_control = Blueprint('customer_controller', __name__)
customer_service = CustomerService()
# GET /customers: get all customers *DONE*
# GET /customer/<customer_id>: get customers by id *DONE*
# POST /customers: create new customer *DONE*
# PUT /customer/<customer_id>: Update customer by id
# DELETE /customer/<customer_id>: Delete customer by id *DONE*

# @cust_control.route('/customers', methods=['GET'])
# def get_all_customers():
#     return {
#         "customers": customer_service.get_all_customers()
#     }

@cust_control.route('/customers', methods=['GET'])
def get_customers():
    first_name = request.args.get('firstname')
    last_name = request.args.get('lastname')

    if first_name is not None and last_name is not None:
        try:
            return customer_service.get_customer_by_name(first_name, last_name)
        except CustomerNotFound as e:
            return {
                       "message": str(e)
                   }, 404
    elif first_name is not None:
        try:
            return {
                "customers": customer_service.get_customer_by_first_name(first_name)
            }
        except CustomerNotFound as e:
            return {
                       "message": str(e)
                   }, 404
    elif last_name is not None:
        try:
            return {
                "customers": customer_service.get_customer_by_last_name(last_name)
            }
        except CustomerNotFound as e:
            return {
                       "message": str(e)
                   }, 404
    else:
        return {
            "customers": customer_service.get_all_customers()
        }

# @cust_control.route('/customers/<first_name>_<last_name>', methods=['GET'])
# def get_customer_by_name(first_name, last_name):
#     try:
#         return customer_service.get_customer_by_name(first_name, last_name)
#     except CustomerNotFound as e:
#         return{
#             "message": str(e)
#         }, 404
#
# @cust_control.route('/customers/users', methods=['GET'])
# def get_customer_by_first_name():
#     first_name = request.args.get('firstname')
#     try:
#         return {
#             "customers": customer_service.get_customer_by_first_name(first_name)
#         }
#     except CustomerNotFound as e:
#         return{
#             "message": str(e)
#         }, 404
#
# @cust_control.route('/customers/users', methods=['GET'])
# def get_customer_by_last_name():
#     last_name = request.args.get('lastname')
#     try:
#         return {
#             "customers": customer_service.get_customer_by_last_name(last_name)
#         }
#     except CustomerNotFound as e:
#         return{
#             "message": str(e)
#         }, 404

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
                               customer_json_dictionary['last_name'])
    try:
        return customer_service.add_customer(customer_object), 201
    except InvalidCustomerName as e:
        return{
            "message": str(e)
        }, 400

@cust_control.route('/customers/<customer_id>', methods=['PUT'])
def update_customer_by_id(customer_id):
    try:
        customer_json_dictionary = request.get_json()
        return customer_service.update_customer_by_id(Customer(customer_id, customer_json_dictionary['first_name'],
                                                               customer_json_dictionary['last_name']))
    except CustomerNotFound as e:
        return{
            "message": str(e)
        }, 404

@cust_control.route('/customers/<customer_id>', methods=['DELETE'])
def delete_user_by_id(customer_id):
    try:
        customer_service.delete_customer_by_id(customer_id)

        return {
            "message": f"Customer with id {customer_id} deleted successfully"
        }
    except CustomerNotFound as e:
        return {
            "message": str(e)
        }, 404
