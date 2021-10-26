import mysql.connector
mysql.connector.__version__

#! 1. connect
conn_NO_DB = mysql.connector.connect(host="localhost",
                                     user="root",
                                     password="1234")

#! 2. cursor
cursor = conn_NO_DB.cursor()

#! 3. Execute Python SQL query
cursor.execute("SHOW SCHEMAS")

#! 4. show results
ans = cursor.fetchall()
for x in ans:
    print(f'\t{x}')

#! 5. Errors
try:
  pass

except mysql.connector.Error as err:
  print(err) # full text error
  print(err.errno) # error num
  print(err.msg) # error msg
  print(err.sqlstate) # SQL state

