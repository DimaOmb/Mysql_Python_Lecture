import mysql.connector


def select_from_customers_where_city(cur, city_name):
    """
        injection possible
    :param cur:
    :param city_name:
    :return:
    """
    try:
        q = f"select * from customers where city = '{city_name}';"
        cur.execute(q)
        print(cur.statement)
        return cur.fetchall()
    except mysql.connector.Error as err:
        print('Error: \t' + err.msg)
        print(cur.statement)

def select_from_customers_where_city_NO_INJECTION(cur, city_name):
    """
        injection NOT possible
    :param cur:
    :param city_name:
    :return:
    """
    q = f"select * from customers where city = %s;"
    try:
        cur.execute(q, city_name)
        print(cur.statement)
        return cur.fetchall()

    except mysql.connector.Error as err:
        print('Error: \t' + err.msg)
        print(cur.statement)

conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="Gooly")
cursor = conn.cursor()

ans = select_from_customers_where_city(cursor, 'רמת גן')
print(ans)
for _ in ans:
    print(_)

# ans = select_from_customers_where_city(cursor, "';  DROP DATABASE gooly;'") # with sql injection
ans = select_from_customers_where_city_NO_INJECTION(cursor, "';  DROP DATABASE gooly;'") # with sql injection

ans_no_injection = select_from_customers_where_city_NO_INJECTION(cursor, ['רמת גן'])


for _ in ans_no_injection:
    print(_)