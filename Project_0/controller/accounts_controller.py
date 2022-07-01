from flask import Blueprint, request
from service.accounts_service import AccountsService
from exceptions.invalid_customer_name import InvalidCustomerName
import controller.customer_controller
from modelcu.accounts import Accounts
from exceptions.customer_not_found import CustomerNotFound

acc_control = Blueprint('accounts_controller', __name__)
account_service = AccountsService()
# GET /customer/<customer_id>/account: get all accounts for customer(id:x) *DONE*
# GET /customer/<customer_id>/account/<account_id>?amountLessThan=1000&amountGreaterThan=300:
# get all accounts for customer(id:x)
# GET /customer/<customer_id>/account/<account_id>: get account(id:y) belonging to customer(id:x)
# PUT /customer/<customer_id>/account/<account_id>: update account(id:y) belonging to customer(id:x)
# DELETE /customer/<customer_id>/account/<account_id>: delete account(id:y) belonging to customer(id:x)

@acc_control.route('/customers/<customer_id>/accounts', methods=['GET'])
def get_all_accounts_by_customer_id(customer_id):
    try:
        return {
            "customers": account_service.get_all_accounts_by_customer_id(customer_id)
        }
    except CustomerNotFound as e:
        return {
            "message": str(e)
        }, 404

@acc_control.route('/customers/<customer_id>/accounts', methods=['GET'])
def get_account_balance(customer_id):
    balance_gt = request.args.get('amountGreaterThan')
    balance_lt = request.args.get('amountLessThan')
    try:
        return {
            "Accounts": account_service.get_account_balance(customer_id, balance_gt, balance_lt)
        }
    except CustomerNotFound as e:
        return{
            "message": str(e)
        }, 404

# @acc_control.route('/customers/<customer_id>/accounts/<account_id>', methods=['PUT'])
# def update_acct_by_cust_and_acct_id(customer_id, account_id):
#     try:
#         get_customer_by_id(customer_id)
#         accounts_json_dictionary = request.get_json()
#         return account_service.update_acct_by_cust_and_acct_id(Accounts(account_id, accounts_json_dictionary['balance'],
#                                                              accounts_json_dictionary['customer_id'],
#                                                              accounts_json_dictionary['account_type_id']))
#     except CustomerNotFound as e:
#         return{
#             "message": str(e)
#         }, 404