import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

timeout = 10000
conn = pymysql.connect(
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor,
    host="localhost",
    user="root",
    password=os.getenv("LocalPassword"),
    database="test1",
    port=3306
)

def update_data(table_name, set_values, key_column, key_value, conn=conn):
    cursor = conn.cursor()

    # columns = ', '.join(data.keys())
    # placeholders = ', '.join(['%s'] * len(data))
    # values = tuple(data.values())
    set_clause = ', '.join([f"{col}=%s" for col in set_values.keys()])

    insert_query = f"UPDATE {table_name} SET {set_clause} WHERE {key_column} = %s"
    print("insert query")
    print(insert_query.format())
    print(set_values.values())
    cursor.execute(insert_query, list(set_values.values()) + [key_value])
    conn.commit()
    cursor.close()

def update_data_multiple_columns(table_name, set_values, key_columns, key_values, conn=conn):
    cursor = conn.cursor()
    set_clause = ', '.join([f"{col}=%s" for col in set_values.keys()])
    equals_arr = []
    for i in range(len(key_columns)):
        equals_arr.append(f"{key_columns[i]} = %s ")
    where_clause = f"WHERE " + 'AND '.join(equals_arr)
    insert_query = f"UPDATE {table_name} SET {set_clause} {where_clause}"
    print("insert query")
    print(insert_query.format())
    print(set_values.values())
    cursor.execute(insert_query, list(set_values.values()) + key_values)
    conn.commit()
    cursor.close()

# set_value = {
#     'password': 'new_new_password'
# }
# update_data('User', set_value, 'username', 'Test')