import mysql.connector

try:
  conn_gooly = mysql.connector.connect(host="localhost", user="root", password="1234", database="Gooly")
  cursor = conn_gooly.cursor()
  cursor.execute(f'select * from sadnaot')
  cursor.execute(f'select sadna_id, name, description, duration from sadnaot')
  ans = cursor.fetchall()

  cursor.rowcount # row count of the answer...use only after fetchall method
  cursor.column_names # columns names of the query
  cursor.statement # the full query

  print(ans)

  for _ in ans:
    print(_)

except mysql.connector.Error as err:
  print('Error: \t' + err)
