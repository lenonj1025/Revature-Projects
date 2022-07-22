import psycopg

from model.employee import Employee

class EmployeeDao:

    # def get_employee_by_id(self, employee_id):
    #     with psycopg.connect(host="127.0.0.1", port="5432", user='postgres',
    #                          dbname="postgres", password="J1a0c2k5", options='-c search_path=project1') as conn:
    #
    #         with conn.cursor() as cur:
    #             cur.execute("SELECT * FROM project1.employees WHERE id = %s", (employee_id,))
    #
    #             employee_row = cur.fetchone()
    #             if not employee_row:
    #                 return None
    #
    #             employee_id = employee_row[0]
    #             username = employee_row[1]
    #             password = employee_row[2]
    #             first_name = employee_row[3]
    #             last_name = employee_row[4]
    #             gender = employee_row[5]
    #             phone_number = employee_row[6]
    #             email_address = employee_row[7]
    #             role_employee = employee_row[8]
    #
    #             return Employee(employee_id, username, password, first_name, last_name, gender, phone_number,
    #                             email_address, role_employee)
    #
    # # def get_all_employees(self):
    # #     with psycopg.connect(host="127.0.0.1", port="5432", user='postgres',
    # #                          dbname="postgres", password="J1a0c2k5", options='-c search_path=project1') as conn:
    # #
    # #         with conn.cursor() as cur:
    # #             cur.execute("SELECT * FROM project1.employees")
    # #
    # #             list_employees = []
    # #
    # #             for employees in cur:
    # #                 employee_id = employees[0]
    # #                 username = employees[1]
    # #                 password = employees[2]
    # #                 first_name = employees[3]
    # #                 last_name = employees[4]
    # #                 gender = employees[5]
    # #                 phone_number = employees[6]
    # #                 email_address = employees[7]
    # #                 role_employee = employees[8]
    # #
    # #                 my_employee_object = Employee(employee_id, username, password, first_name, last_name, gender,
    # #                                               phone_number, email_address, role_employee)
    # #                 list_employees.append(my_employee_object)
    # #
    # #             return list_employees
    #
    def get_employee_by_username_and_password(self, username, password):
        with psycopg.connect(host="127.0.0.1", port="5432", user='postgres',
                             dbname="postgres", password="J1a0c2k5", options='-c search_path=project1') as conn:
            with conn.cursor() as cur:
                cur.execute("Select * from project1.employees WHERE username = %s and pwd = %s",
                            (username, password))

                employee_info = cur.fetchone()

                if employee_info is None:
                    return None

                employee_id = employee_info[0]
                username = employee_info[1]
                password = employee_info[2]
                first_name = employee_info[3]
                last_name = employee_info[4]
                gender = employee_info[5]
                phone_number = employee_info[6]
                email_address = employee_info[7]
                role_employee = employee_info[8]

                return Employee(employee_id, username, password, first_name, last_name, gender,
                                phone_number, email_address, role_employee)

    def get_employee_by_email(self, email):
        with psycopg.connect(host="127.0.0.1", port="5432", user='postgres',
                             dbname="postgres", password="J1a0c2k5", options='-c search_path=project1') as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * from project1.employees WHERE email_address = %s", (email,))

                employee_info = cur.fetchone()

                if employee_info is None:
                    return None

                employee_id = employee_info[0]
                username = employee_info[1]
                password = employee_info[2]
                first_name = employee_info[3]
                last_name = employee_info[4]
                gender = employee_info[5]
                phone_number = employee_info[6]
                email_address = employee_info[7]
                role_employee = employee_info[8]

                return Employee(employee_id, username, password, first_name, last_name, gender,
                                phone_number, email_address, role_employee)

    def get_employee_by_username(self, username):
        with psycopg.connect(host="127.0.0.1", port="5432", user='postgres',
                             dbname="postgres", password="J1a0c2k5", options='-c search_path=project1') as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM project1.employees WHERE username = %s", (username,))

                employee_info = cur.fetchone()

                if employee_info is None:
                    return None

                employee_id = employee_info[0]
                username = employee_info[1]
                password = employee_info[2]
                first_name = employee_info[3]
                last_name = employee_info[4]
                gender = employee_info[5]
                phone_number = employee_info[6]
                email_address = employee_info[7]
                role_employee = employee_info[8]

                return Employee(employee_id, username, password, first_name, last_name, gender,
                                phone_number, email_address, role_employee)

    def add_employee(self, employee_obj):
        with psycopg.connect(host="127.0.0.1", port="5432", user='postgres',
                             dbname="postgres", password="J1a0c2k5", options='-c search_path=project1') as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO project1.employees (username, pwd, first_name, last_name, gender,"
                            "phone_number, email_address, role_employee) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) "
                            "RETURNING *",
                            (employee_obj.username, employee_obj.password, employee_obj.first_name,
                             employee_obj.last_name, employee_obj.gender, employee_obj.phone_number,
                             employee_obj.email_address, employee_obj.role_employee))

                employee_that_was_inserted = cur.fetchone()
                conn.commit()

                return Employee(employee_that_was_inserted[0], employee_that_was_inserted[1],
                                employee_that_was_inserted[2], employee_that_was_inserted[3],
                                employee_that_was_inserted[4], employee_that_was_inserted[5],
                                employee_that_was_inserted[6], employee_that_was_inserted[7],
                                employee_that_was_inserted[8])

    def update_employee_by_id(self, employee_object):
        with psycopg.connect(host="127.0.0.1", port="5432", user="postgres",
                             dbname="postgres", password="J1a0c2k5", options='-c search_path=project1') as conn:

            with conn.cursor() as cur:
                cur.execute("UPDATE project1.employees SET username = %s, pwd = %s, first_name = %s, "
                            "last_name = %s, gender = %s, phone_number = %s, email_address = %s, "
                            "role_employee = %s WHERE id = %s RETURNING *",
                            (employee_object.username, employee_object.password, employee_object.first_name,
                             employee_object.last_name, employee_object.gender, employee_object.phone_number,
                             employee_object.email_address, employee_object.role_employee, employee_object.id))

                conn. commit()

                employee_row_updated = cur.fetchone()
                if employee_row_updated is None:
                    return None

                return Employee(employee_row_updated[0], employee_row_updated[1], employee_row_updated[2],
                                employee_row_updated[3], employee_row_updated[4], employee_row_updated[5],
                                employee_row_updated[6], employee_row_updated[7], employee_row_updated[8])
