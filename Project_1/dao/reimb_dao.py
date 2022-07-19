import psycopg

from model.reimbursement import Reimbursement
class ReimbDao:

    def get_all_reimb_by_employee_id(self, employee_id):
        with psycopg.connect(host="127.0.0.1", port="5432", user='postgres',
                             dbname="postgres", password="J1a0c2k5", options=f'-c search_path=project1') as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM project1.reimbursements WHERE author = %s", (employee_id,))

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
                            "ON e.id = reimb.author WHERE e.id = %s AND reimb.status = %s",
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
                    author = reimbs[8]
                    resolver = reimbs[9]

                    my_reimb_object = Reimbursement(id, amount, submitted, resolved, status, reimb_type_id,
                                                    description, receipt, author, resolver)
                    list_reimbs.append(my_reimb_object)
                return list_reimbs
