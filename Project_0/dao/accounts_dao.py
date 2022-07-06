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

    def get_account_balance(self, customer_id, amount_greater_than, amount_less_than):
        with psycopg.connect(host="127.0.0.1", port="5432", user='postgres',
                             dbname="postgres", password="J1a0c2k5", options='-c search_path=project0') as conn:

            with conn.cursor() as cur:
                cur.execute("SELECT act.* "
                            "FROM accounts act JOIN project0.customers c  ON c.id = act.customer_id "
                            "WHERE customer_id = %s AND act.balance > %s AND act.balance < %s",
                            (customer_id, amount_greater_than, amount_less_than,))
                list_accounts = []

                for accounts in cur:
                    id = accounts[0]
                    balance = accounts[1]
                    customer_id = accounts[2]
                    account_type_id = accounts[3]

                    my_account_object = Accounts(id, balance, customer_id, account_type_id)
                    list_accounts.append(my_account_object)
                return list_accounts

    def get_account_by_greater_than(self, customer_id, amount_greater_than):
        with psycopg.connect(host="127.0.0.1", port="5432", user='postgres',
                             dbname="postgres", password="J1a0c2k5", options='-c search_path=project0') as conn:

            with conn.cursor() as cur:
                cur.execute("SELECT act.* "
                            "FROM accounts act JOIN project0.customers c ON c.id = act.customer_id "
                            "WHERE customer_id = %s AND act.balance > %s",
                            (customer_id, amount_greater_than,))
                list_accounts = []

                for accounts in cur:
                    id = accounts[0]
                    balance = accounts[1]
                    customer_id = accounts[2]
                    account_type_id = accounts[3]

                    my_account_object = Accounts(id, balance, customer_id, account_type_id)
                    list_accounts.append(my_account_object)
                return list_accounts

    def get_account_by_less_than(self, customer_id, amount_less_than):
        with psycopg.connect(host="127.0.0.1", port="5432", user='postgres',
                             dbname="postgres", password="J1a0c2k5", options='-c search_path=project0') as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT act.* "
                            "FROM accounts act JOIN project0.customers c  ON c.id = act.customer_id "
                            "WHERE customer_id = %s AND act.balance < %s",
                            (customer_id, amount_less_than,))
                list_accounts = []

                for accounts in cur:
                    id = accounts[0]
                    balance = accounts[1]
                    customer_id = accounts[2]
                    account_type_id = accounts[3]

                    my_account_object = Accounts(id, balance, customer_id, account_type_id)
                    list_accounts.append(my_account_object)
                return list_accounts

    def get_account_by_customer_and_account_id(self, customer_id, account_id):
        with psycopg.connect(host="127.0.0.1", port="5432", user='postgres',
                             dbname="postgres", password="J1a0c2k5", options='-c search_path=project0') as conn:

            with conn.cursor() as cur:
                cur.execute("SELECT act.* "
                            "FROM accounts act JOIN project0.customers c  ON c.id = act.customer_id "
                            "WHERE customer_id = %s AND act.id = %s",
                            (customer_id, account_id,))

                list_accounts = []

                for row in cur:
                    list_accounts.append(Accounts(row[0], row[1], row[2], row[3]))
                print(list_accounts)
                return list_accounts

    def add_account_to_customer(self, account_object):
        balance_to_add = account_object.balance
        customer_id_to_add = account_object.customer_id
        account_type_id_to_add = account_object.account_type_id

        with psycopg.connect(host="127.0.0.1", port="5432", user="postgres",
                             dbname="postgres", password="J1a0c2k5", options='-c search_path=project0') as conn:

            # Automatically close the cursor
            with conn.cursor() as cur:
                cur.execute("INSERT INTO project0.accounts (balance, customer_id, account_type_id) "
                            "VALUES (%s, %s, %s) RETURNING *",
                            (balance_to_add, customer_id_to_add, account_type_id_to_add))

                account_row_inserted = cur.fetchone()
                conn.commit()

                return Accounts(account_row_inserted[0], account_row_inserted[1],
                                account_row_inserted[2], account_row_inserted[3])

    def update_acct_by_cust_and_acct_id(self, account_object):
        with psycopg.connect(host="127.0.0.1", port="5432", user="postgres",
                             dbname="postgres", password="J1a0c2k5", options='-c search_path=project0') as conn:

            with conn.cursor() as cur:
                cur.execute("UPDATE project0.accounts SET balance = %s WHERE customer_id = %s "
                            "AND account_type_id = %s RETURNING *",
                            (account_object.balance, account_object.customer_id, account_object.account_type_id))

                conn. commit()

                account_row_updated = cur.fetchone()
                if account_row_updated is None:
                    return None

                return Accounts(account_row_updated[0], account_row_updated[1],
                                account_row_updated[2], account_row_updated[3])

    def delete_account_by_account_id(self, customer_id, account_id):
        with psycopg.connect(host="127.0.0.1", port="5432", user="postgres",
                             dbname="postgres", password="J1a0c2k5", options='-c search_path=project0') as conn:

            with conn.cursor() as cur:
                cur.execute("DELETE FROM project0.accounts WHERE customer_id = %s AND id = %s",
                            (customer_id, account_id,))

                rows_deleted = cur.rowcount

                if rows_deleted != 1:
                    return False
                else:
                    conn.commit()
                    return True
