import psycopg
from modelcu.customer import Customer


class CustomerDao:
    def get_all_customers(self):
        with psycopg.connect(host="127.0.0.1", port="5432", user='postgres',
                             dbname="customers", password="J1a0c2k5") as conn:

            with conn.cursor() as cur:
                cur.execute("SELECT * FROM customers")

                list_customers = []

                for customers in cur:
                    customer_id = customers[0]
                    first_name = customers[1]
                    last_name = customers[2]
                    checking_account = customers[3]
                    savings_account = customers[4]

                    my_customers_object = Customer(customer_id, first_name, last_name,
                                                   checking_account, savings_account)
                    list_customers.append(my_customers_object)

                return list_customers

    def get_customer_by_name(self, first_name, last_name):
        with psycopg.connect(host="127.0.0.1", port="5432", user='postgres',
                             dbname="customers", password="J1a0c2k5") as conn:

            with conn.cursor() as cur:
                cur.execute("SELECT * FROM customers WHERE first_name = %s "
                            "AND last_name = %s", (first_name, last_name))

                customer_row = cur.fetchone()
                if not customer_row:
                    return None

                customer_id = customer_row[0]
                first_name = customer_row[1]
                last_name = customer_row[2]
                checking_account = customer_row[3]
                savings_account = customer_row[4]

                return Customer(customer_id, first_name, last_name, checking_account, savings_account)

    def get_customer_by_first_name(self, first_name):
        with psycopg.connect(host="127.0.0.1", port="5432", user='postgres',
                             dbname="customers", password="J1a0c2k5") as conn:

            with conn.cursor() as cur:
                cur.execute("SELECT * FROM customers WHERE first_name = %s", (first_name,))

                customer_row = cur.fetchall()
                if not customer_row:
                    return None

                customer_id = customer_row[0]
                first_name = customer_row[1]
                last_name = customer_row[2]
                checking_account = customer_row[3]
                savings_account = customer_row[4]

                return Customer(customer_id, first_name, last_name, checking_account, savings_account)

    def get_customer_by_last_name(self, last_name):
        with psycopg.connect(host="127.0.0.1", port="5432", user='postgres',
                             dbname="customers", password="J1a0c2k5") as conn:

            with conn.cursor() as cur:
                cur.execute("SELECT * FROM customers WHERE last_name = %s", (last_name,))

                customer_row = cur.fetchall()
                if not customer_row:
                    return None
                print(customer_row)
                for c_row in customer_row:
                    customer_id = c_row[0]
                    print("customer_id = ", c_row[0])
                    first_name = c_row[1]
                    print("first_name = ", c_row[1])
                    last_name = c_row[2]
                    print("last_name = ", c_row[2])
                    checking_account = c_row[3]
                    print("checking_account = ", c_row[3])
                    savings_account = c_row[4]
                    print("savings_account = ", c_row[4], "\n")

                return Customer(customer_id, first_name, last_name, checking_account, savings_account)

    def get_customer_by_id(self, customer_id):
        with psycopg.connect(host="127.0.0.1", port="5432", user='postgres',
                             dbname="customers", password="J1a0c2k5") as conn:

            with conn.cursor() as cur:
                cur.execute("SELECT * FROM customers WHERE id = %s", (customer_id,))

                customer_row = cur.fetchone()
                if not customer_row:
                    return None

                customer_id = customer_row[0]
                first_name = customer_row[1]
                last_name = customer_row[2]
                checking_account = customer_row[3]
                savings_account = customer_row[4]

                return Customer(customer_id, first_name, last_name, checking_account, savings_account)
