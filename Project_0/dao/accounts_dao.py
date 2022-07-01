import psycopg
from modelcu.accounts import Accounts

class AccountsDao:

    def get_all_accounts_by_customer_id(self, customer_id):
        with psycopg.connect(host="127.0.0.1", port="5432", user='postgres',
                             dbname="postgres", password="J1a0c2k5", options=f'-c search_path=project0') as conn:

            with conn.cursor() as cur:
                cur.execute("SELECT * FROM project0.accounts WHERE customer_id = %s", (customer_id,))

                list_accounts = []

                for row in cur:
                    list_accounts.append(Accounts(row[0], row[1], row[2], row[3]))

                return list_accounts

    def get_account_balance(self, customer_id, balance_gt, balance_lt):
        with psycopg.connect(host="127.0.0.1", port="5432", user='postgres',
                             dbname="postgres", password="J1a0c2k5", options='-c search_path=project0') as conn:

            with conn.cursor() as cur:
                cur.execute("SELECT act.* "
                            "FROM accounts act JOIN project0.customers c  ON c.id = act.customer_id "
                            "WHERE customer_id = %s AND act.balance > %s AND act.balance < %s",
                            (customer_id, balance_gt, balance_lt))
                list_accounts = []

                for accounts in cur:
                    id = accounts[0]
                    balance = accounts[1]
                    customer_id = accounts[2]
                    account_type_id = accounts[3]

                    my_account_object = Accounts(id, balance, customer_id, account_type_id)
                    list_accounts.append(my_account_object)

                return list_accounts
