from flask import Blueprint, request
from service.customer_service import CustomerService
from exceptions.customer_not_found import CustomerNotFound

cust_control = Blueprint('customer_controller', __name__)
customer_service = CustomerService()
# GET /customers: get all customers
# GET /customer/<customer_id>: get customers by id
# PUT /customers: create new customer
# PUT /customer/<customer_id>: Update customer by id
# DELETE /customer/<customer_id>: Delete customer by id

@cust_control.route('/customers')
def get_all_customers():
    return {
        "customers": customer_service.get_all_customers()
    }

@cust_control.route('/customers/<first_name>_<last_name>')
def get_customer_by_name(first_name, last_name):
    try:
        return customer_service.get_customer_by_name(first_name, last_name)
    except CustomerNotFound as e:
        return{
            "message": str(e)
        }, 404

@cust_control.route('/customers/firstname_<first_name>')
def get_customer_by_first_name(first_name):
    try:
        return customer_service.get_customer_by_first_name(first_name)
    except CustomerNotFound as e:
        return{
            "message": str(e)
        }, 404

@cust_control.route('/customers/lastname_<last_name>')
def get_customer_by_last_name(last_name):
    try:
        return customer_service.get_customer_by_last_name(last_name)
    except CustomerNotFound as e:
        return{
            "message": str(e)
        }, 404

@cust_control.route('/customers/<customer_id>')
def get_customer_by_id(customer_id):
    try:
        return customer_service.get_customer_by_id(customer_id)
    except CustomerNotFound as e:
        return{
            "message": str(e)
        }, 404
