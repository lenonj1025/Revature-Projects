import psycopg
from modelcu.customer import Customer


class CustomerDao:
    def get_all_customers(self):
        with psycopg.connect(host="127.0.0.1", port="5432", user='postgres',
                             dbname="postgres", password="J1a0c2k5", options=f'-c search_path=project0') as conn:

            with conn.cursor() as cur:
                cur.execute("SELECT * FROM project0.customers")

                list_customers = []

                for customers in cur:
                    customer_id = customers[0]
                    first_name = customers[1]
                    last_name = customers[2]

                    my_customers_object = Customer(customer_id, first_name, last_name)
                    list_customers.append(my_customers_object)

                return list_customers

    def get_customer_by_name(self, first_name, last_name):
        with psycopg.connect(host="127.0.0.1", port="5432", user='postgres',
                             dbname="postgres", password="J1a0c2k5", options=f'-c search_path=project0') as conn:

            with conn.cursor() as cur:
                cur.execute("SELECT * FROM project0.customers WHERE first_name = %s "
                            "AND last_name = %s", (first_name, last_name))

                customer_row = cur.fetchone()
                if not customer_row:
                    return None

                customer_id = customer_row[0]
                first_name = customer_row[1]
                last_name = customer_row[2]

                return Customer(customer_id, first_name, last_name)

    def get_customer_by_first_name(self, first_name):
        with psycopg.connect(host="127.0.0.1", port="5432", user='postgres',
                             dbname="postgres", password="J1a0c2k5", options=f'-c search_path=project0') as conn:

            with conn.cursor() as cur:
                cur.execute("SELECT * FROM project0.customers WHERE first_name = %s", (first_name,))
                list_customers = []

                for customers in cur:
                    customer_id = customers[0]
                    first_name = customers[1]
                    last_name = customers[2]

                    my_customers_object = Customer(customer_id, first_name, last_name)
                    list_customers.append(my_customers_object)

                return list_customers

    def get_customer_by_last_name(self, last_name):
        with psycopg.connect(host="127.0.0.1", port="5432", user='postgres',
                             dbname="postgres", password="J1a0c2k5", options='-c search_path=project0') as conn:

            with conn.cursor() as cur:
                cur.execute("SELECT * FROM project0.customers WHERE last_name = %s", (last_name,))
                list_customers = []

                for customers in cur:
                    customer_id = customers[0]
                    first_name = customers[1]
                    last_name = customers[2]

                    my_customers_object = Customer(customer_id, first_name, last_name)
                    list_customers.append(my_customers_object)

                return list_customers

    def get_customer_by_id(self, customer_id):
        with psycopg.connect(host="127.0.0.1", port="5432", user='postgres',
                             dbname="postgres", password="J1a0c2k5", options='-c search_path=project0') as conn:

            with conn.cursor() as cur:
                cur.execute("SELECT * FROM project0.customers WHERE id = %s", (customer_id,))

                customer_row = cur.fetchone()
                if not customer_row:
                    return None

                customer_id = customer_row[0]
                first_name = customer_row[1]
                last_name = customer_row[2]

                return Customer(customer_id, first_name, last_name)

    def add_customer(self, customer_object):
        print(customer_object)
        first_name_to_add = customer_object.first_name
        last_name_to_add = customer_object.last_name

        with psycopg.connect(host="127.0.0.1", port="5432", user="postgres",
                             dbname="postgres", password="J1a0c2k5", options='-c search_path=project0') as conn:

            # Automatically close the cursor
            with conn.cursor() as cur:
                cur.execute("INSERT INTO project0.customers (first_name, last_name) VALUES (%s, %s) RETURNING *",
                            (first_name_to_add, last_name_to_add))

                customer_row_inserted = cur.fetchone()
                conn.commit()

                return Customer(customer_row_inserted[0], customer_row_inserted[1], customer_row_inserted[2])

    def update_customer_by_id(self, customer_object):
        # print(customer_object)
        with psycopg.connect(host="127.0.0.1", port="5432", user="postgres",
                             dbname="postgres", password="J1a0c2k5", options='-c search_path=project0') as conn:

            # Automatically close the cursor
            with conn.cursor() as cur:
                cur.execute("UPDATE project0.customers SET first_name = %s, last_name = %s WHERE id = %s RETURNING *",
                            (customer_object.first_name, customer_object.last_name, customer_object.id))

                conn. commit()

                customer_row_updated = cur.fetchone()
                if customer_row_updated is None:
                    return None

                return Customer(customer_row_updated[0], customer_row_updated[1], customer_row_updated[2])

    def delete_customer_by_id(self, customer_id):
        with psycopg.connect(host="127.0.0.1", port="5432", user="postgres",
                             dbname="postgres", password="J1a0c2k5", options='-c search_path=project0') as conn:

            # Automatically close the cursor
            with conn.cursor() as cur:
                cur.execute('DELETE FROM project0.customers WHERE id = %s', (customer_id,))

                # Check number of rows that are deleted
                rows_deleted = cur.rowcount

                if rows_deleted != 1:
                    return False
                else:
                    conn.commit()
                    return True
