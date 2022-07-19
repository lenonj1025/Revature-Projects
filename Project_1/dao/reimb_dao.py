import psycopg

from model.reimbursement import Reimbursement
class ReimbDao:

    def get_all_reimb_by_employee_id(self, employee_id):
        with psycopg.connect(host="127.0.0.1", port="5432", user='postgres',
                             dbname="postgres", password="J1a0c2k5", options=f'-c search_path=project1') as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM project1.reimbursements WHERE employee_id = %s", (employee_id,))

                list_reimbs = []

                for row in cur:
                    list_reimbs.append(Reimbursement(row[0], row[1], row[2], row[3], row[4], row[5], row[6],
                                                     row[7], row[8], row[9]))

                return list_reimbs

    def get_reimbs_by_status(self, employee_id, status):
        with psycopg.connect(host="127.0.0.1", port="5432", user='postgres',
                             dbname="postgres", password="J1a0c2k5", options='-c search_path=project1') as conn:

            with conn.cursor() as cur:
                cur.execute("SELECT reimb.* FROM reimbursements reimb JOIN project1.employees e "
                            "ON e.id = reimb.employee_id WHERE e.id = %s AND reimb.status = %s",
                            (employee_id, status))
                list_reimbs = []

                for reimbs in cur:
                    id = reimbs[0]
                    amount = reimbs[1]
                    submitted = reimbs[2]
                    resolved = reimbs[3]
                    status = reimbs[4]
                    reimb_type_id = reimbs[5]
                    description = reimbs[6]
                    receipt = reimbs[7]
                    employee_id = reimbs[8]
                    resolver_id = reimbs[9]

                    my_reimb_object = Reimbursement(id, amount, submitted, resolved, status, reimb_type_id,
                                                    description, receipt, employee_id, resolver_id)
                    list_reimbs.append(my_reimb_object)
                return list_reimbs

    def add_reimb_to_employee(self, reimb_object):
        amount_to_add = reimb_object.amount
        status_to_add = reimb_object.status
        reimb_type_id_to_add = reimb_object.reimb_type_id
        description_to_add = reimb_object.description
        employee_to_add = reimb_object.employee_id

        with psycopg.connect(host="127.0.0.1", port="5432", user="postgres",
                             dbname="postgres", password="J1a0c2k5", options='-c search_path=project1') as conn:

            # Automatically close the cursor
            with conn.cursor() as cur:
                cur.execute("INSERT INTO project1.reimbursements (amount, status, reimb_type_id, description, "
                            "employee_id) VALUES (%s, %s, %s, %s, %s) "
                            "RETURNING *",
                            (amount_to_add, status_to_add, reimb_type_id_to_add,
                             description_to_add, employee_to_add))

                reimb_row_inserted = cur.fetchone()
                conn.commit()

                return Reimbursement(reimb_row_inserted[0], reimb_row_inserted[1], reimb_row_inserted[2],
                                     reimb_row_inserted[3], reimb_row_inserted[4], reimb_row_inserted[5],
                                     reimb_row_inserted[6], reimb_row_inserted[7], reimb_row_inserted[8],
                                     reimb_row_inserted[9])

    def update_reimb_by_ids(self, reimb_object):
        with psycopg.connect(host="127.0.0.1", port="5432", user="postgres",
                             dbname="postgres", password="J1a0c2k5", options='-c search_path=project1') as conn:

            with conn.cursor() as cur:
                cur.execute("UPDATE project1.reimbursements SET status = %s, resolved = (SELECT CURRENT_TIMESTAMP), "
                            "resolver_id = %s WHERE employee_id = %s AND id = %s RETURNING *",
                            (reimb_object.status, reimb_object.resolver_id, reimb_object.employee_id,
                             reimb_object.id))

                conn. commit()

                reimb_row_updated = cur.fetchone()
                if reimb_row_updated is None:
                    return None

                return Reimbursement(reimb_row_updated[0], reimb_row_updated[1], reimb_row_updated[2],
                                     reimb_row_updated[3], reimb_row_updated[4], reimb_row_updated[5],
                                     reimb_row_updated[6], reimb_row_updated[7], reimb_row_updated[8],
                                     reimb_row_updated[9])
