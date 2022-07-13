import psycopg

from model.employee import Employee

class EmployeeDao:

    def get_all_employees(self):
        with psycopg.connect(host="127.0.0.1", port="5432", user='postgres',
                             dbname="postgres", password="J1a0c2k5", options='-c search_path=project1') as conn:

            with conn.cursor() as cur:
                cur.execute("SELECT * FROM project1.employees")

                list_employees = []

                for employees in cur:
                    username = employees[0]
                    password = employees[1]
                    first_name = employees[2]
                    last_name = employees[3]
                    phone_number = employees[4]
                    email_address = employees[5]

                    my_employee_object = Employee(username, password, first_name, last_name, phone_number, email_address)
                    list_employees.append(my_employee_object)

                return list_employees

    def get_employee_by_email(self, email):
        with psycopg.connect(host="127.0.0.1", port="5432", user='postgres',
                             dbname="postgres", password="J1a0c2k5", options='-c search_path=project1') as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * from project1.employees WHERE email_address = %s", (email,))

                employee_info = cur.fetchone()

                if employee_info is None:
                    return None

                username = employee_info[0]
                password = employee_info[1]
                first_name = employee_info[2]
                last_name = employee_info[3]
                phone_number = employee_info[4]
                email_address = employee_info[5]

                return Employee(username, password, first_name, last_name, phone_number, email_address)

    def get_employee_by_username(self, username):
        with psycopg.connect(host="127.0.0.1", port="5432", user='postgres',
                             dbname="postgres", password="J1a0c2k5", options='-c search_path=project1') as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM project1.employees WHERE username = %s", (username,))

                employee_info = cur.fetchone()

                if employee_info is None:
                    return None

                username = employee_info[0]
                password = employee_info[1]
                first_name = employee_info[2]
                last_name = employee_info[3]
                phone_number = employee_info[4]
                email_address = employee_info[5]

                return Employee(username, password, first_name, last_name, phone_number, email_address)

    def add_employee(self, employee_obj):
        with psycopg.connect(host="127.0.0.1", port="5432", user='postgres',
                             dbname="postgres", password="J1a0c2k5", options='-c search_path=project1') as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO project1.employees VALUES (%s, %s, %s, %s, %s, %s) RETURNING *",
                            (employee_obj.username,
                             employee_obj.password,
                             employee_obj.first_name,
                             employee_obj.last_name,
                             employee_obj.phone_number,
                             employee_obj.email_address))

                employee_that_was_inserted = cur.fetchone()
                conn.commit()

                return Employee(employee_that_was_inserted[0], employee_that_was_inserted[1],
                                employee_that_was_inserted[2], employee_that_was_inserted[3],
                                employee_that_was_inserted[4], employee_that_was_inserted[5])
