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
    read_timeout=timeout,
    write_timeout=timeout,
    port=3306
)

def delete_data(table_name, key, key_column, conn=conn):
    cursor = conn.cursor()

    # key_column = list(key.keys())[0]
    # key_value = key[key_column]

    delete_query = f"DELETE FROM {table_name} WHERE {key_column} = %s"
    print("delete query")
    print(delete_query)

    cursor.execute(delete_query, (key,))
    conn.commit()

    print(f"Deleted rows with {key_column} = {key}")
    cursor.close()

def delete_data_multiple_columns(table_name, keys, key_columns, conn=conn):
    cursor = conn.cursor()
    equals_arr = []
    for i in range(len(key_columns)):
        equals_arr.append(f"{key_columns[i]} = %s ")
    where_clause = f"WHERE " + 'AND '.join(equals_arr)
    delete_query = f"DELETE FROM {table_name} {where_clause}"
    print(delete_query)
    cursor.execute(delete_query, keys)
    conn.commit()
    cursor.close()