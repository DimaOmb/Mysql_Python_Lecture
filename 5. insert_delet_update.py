import mysql.connector

conn_gooly = mysql.connector.connect(host="localhost", user="root", password="1234", database="Gooly")
conn_gooly.autocommit = True  # automatically save the changes to the table, otherwise no changes are made to the table.
cur = conn_gooly.cursor()

# 1. insert
insert_sql = "insert into payments (cust_id, payment_date, payment_sum) values (%s, %s, %s);"
# val = (5, '2021-08-01', 2000)
# wrong_val = ('hello', '2021-08-01', 2000)
# cur.execute(insert_sql, val)
# cur.execute(insert_sql, wrong_val)
cur.statement
cur.lastrowid

# 1.1. insert many
val_list = [(5, '2021-08-01', 2000), (3, '2021-9-01', 100), (5, '2021-10-01', 500), (4, '2021-10-10', 300)]
cur.executemany(insert_sql, val_list)
cur.lastrowid
cur.statement

# 1.2. update
update_sql = """update payments set payment_sum = 5000 where cust_id = (select cust_id from customers where customers.name = %s) 
                                                            and payment_date = %s;"""
update_val = (u"בית ספר דגלים", '2020-08-01')
cur.execute(update_sql, update_val)
cur.statement
print(cur.rowcount, "record(s) affected")

# 1.3. delete
delete_sql = """DELETE FROM orders where cust_id in (select customers.cust_id from customers WHERE city = %s)"""
# del_val = tuple(["פתח תקווה"])
del_val = ["פתח תקווה"]
type(del_val)
# del_val = ("0566665803", u"פתח תקווה")
cur.execute(delete_sql, del_val)
cur.statement

print(cur.rowcount, "record deleted.")

conn_gooly.close()
