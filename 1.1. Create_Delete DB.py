import mysql.connector

try:
    conn = mysql.connector.connect(host="localhost", user="root", password="1234")
except mysql.connector.Error as err:
    print(f"Something went wrong: \n\t{err}")

#! 1. SHOW SCHEMAS
cursor = conn.cursor()
cursor.execute("SHOW SCHEMAS")
print("Before test_DB Creation")
ans = cursor.fetchall()
for x in ans:
    print(f'\t{x}')

#! 2. create DB\schema
cursor.execute("CREATE SCHEMA test_DB")
cursor.execute("SHOW SCHEMAS")
print("After test_DB Creation")
ans = cursor.fetchall()
for x in ans:
    print(f'\t{x}')

#! 3. delete DB
print("After test_DB Deletion")
cursor.execute("DROP SCHEMA test_DB")
cursor.execute("SHOW SCHEMAS")
ans = cursor.fetchall()
for x in ans:
    print(f'\t{x}')

