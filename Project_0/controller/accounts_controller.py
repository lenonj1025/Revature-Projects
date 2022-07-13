from flask import Blueprint, request
from modelcu.accounts import Accounts
import exceptions.customer_exceptions as ce
import exceptions.accounts_exceptions as ae
from service.accounts_service import AccountsService

acc_control = Blueprint('accounts_controller', __name__)
account_service = AccountsService()

@acc_control.route('/customers/<customer_id>/accounts', methods=['GET'])
def get_accounts(customer_id):
    amount_greater_than = request.args.get('amountGreaterThan')
    amount_less_than = request.args.get('amountLessThan')

    if amount_greater_than is not None and amount_less_than is not None:
        try:
            return {
                "accounts": account_service.get_account_balance(customer_id, amount_greater_than, amount_less_than)
            }
        except ce.CustomerNotFound as e:
            return {
                       "message": str(e)
                   }, 404
        except ae.AccountNotFound as e:
            return {
                       "message": str(e)
                   }, 404
    elif amount_greater_than is not None and amount_less_than is None:
        try:
            return {
                "accounts": account_service.get_account_by_greater_than(customer_id, amount_greater_than)
            }
        except ce.CustomerNotFound as e:
            return {
                       "message": str(e)
                   }, 404
        except ae.AccountNotFound as e:
            return {
                        "message": str(e)
                   }, 404
    elif amount_greater_than is None and amount_less_than is not None:
        try:
            return{
                "accounts": account_service.get_account_by_less_than(customer_id, amount_less_than)
            }
        except ce.CustomerNotFound as e:
            return {
                       "message": str(e)
                   }, 404
        except ae.AccountNotFound as e:
            return {
                        "message": str(e)
                   }, 404
    else:
        try:
            return {
                "customers": account_service.get_all_accounts_by_customer_id(customer_id)
            }
        except ce.CustomerNotFound as e:
            return {
                       "message": str(e)
                   }, 404

@acc_control.route('/customers/<customer_id>/accounts/<account_id>', methods=['GET'])
def get_account_by_customer_and_account_id(customer_id, account_id):
    try:
        return {
           "accounts": account_service.get_account_by_customer_and_account_id(customer_id, account_id)
        }
    except ce.CustomerNotFound as e:
        return {
            "message": str(e)
        }, 404
    except ae.AccountNotFound as e:
        return {
            "message": str(e)
        }, 404

@acc_control.route('/customers/<customer_id>/accounts', methods=['POST'])
def add_account_to_customer(customer_id):
    accounts_json_dictionary = request.get_json()
    account_object = Accounts(None, accounts_json_dictionary['balance'], customer_id,
                              accounts_json_dictionary['account_type_id'])
    try:
        return account_service.add_account_to_customer(account_object), 201
    except ce.CustomerNotFound as e:
        return{
            "message": str(e)
        }, 404
    except ae.AccountTypeError as e:
        return{
            "message": str(e)
        }, 404


@acc_control.route('/customers/<customer_id>/accounts/<account_id>', methods=['PUT'])
def update_acct_by_cust_and_acct_id(customer_id, account_id):
    try:
        accounts_json_dictionary = request.get_json()
        return account_service.update_acct_by_cust_and_acct_id(Accounts(account_id,
                                                                        accounts_json_dictionary['balance'],
                                                                        customer_id,
                                                                        accounts_json_dictionary['account_type_id']))
    except ce.CustomerNotFound as e:
        return {
            "message": str(e)
        }, 404
    except ae.AccountNotFound as e:
        return {
            "message": str(e)
        }, 404
    except ae.AccountTypeError as e:
        return{
            "message": str(e)
        }, 404

@acc_control.route('/customers/<customer_id>/accounts/<account_id>', methods=['DELETE'])
def delete_account_by_account_id(customer_id, account_id):
    try:
        account_service.delete_account_by_account_id(customer_id, account_id)

        return {
            "message": f"Customer with id {customer_id} was found. Account with id {account_id} deleted successfully"
        }
    except ce.CustomerNotFound as e:
        return {
            "message": str(e)
        }, 404
    except ae.AccountNotFound as e:
        return {
            "message": str(e)
        }, 404
