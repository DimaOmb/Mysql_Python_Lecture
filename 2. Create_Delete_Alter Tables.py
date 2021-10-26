from mailcap import show

import mysql.connector

def show_tables(cur):
    cur.execute("SHOW TABLES")
    result = cur.fetchall()
    print(result)


def create_table(cur, table_name="test_table"):
    cur.execute(f"CREATE TABLE {table_name} (name VARCHAR(255), address VARCHAR(255));")


def drop_table(cur, table_name="test_table"):
    cur.execute(f"drop TABLE {table_name};")


def alter_table(cur, table_name="test_table", add_column_name='id'):
    cur.execute(f"ALTER TABLE {table_name} ADD COLUMN {add_column_name} INT")

try:
    conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="gooly")
    cursor = conn.cursor()

    print("before create")
    show_tables(cursor)
    create_table(cursor, table_name="test_table")
    print("after create")
    show_tables(cursor)
    drop_table(cursor)
    alter_table(cursor, add_column_name='another_coll1')

except mysql.connector.Error as err:
    print(f"Error: \n\t{err}")
