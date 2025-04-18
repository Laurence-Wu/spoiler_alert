import pymysql
from datetime import datetime
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
# timeout = 10000
# conn = pymysql.connect(
#   charset="utf8mb4",
#   connect_timeout=timeout,
#   cursorclass=pymysql.cursors.DictCursor,
#   db="defaultdb",
#   host="spoiler-alert-spoileralert.d.aivencloud.com",
#   read_timeout=timeout,
#   port=24887,
#   user="avnadmin",
#   password= os.getenv("AIVEN_PASS"),
#   write_timeout=timeout,
# )


def insert_data(table_name, data, conn=conn):
    cursor = conn.cursor()

    columns = ', '.join(data.keys())
    placeholders = ', '.join(['%s'] * len(data))
    values = tuple(data.values())

    insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    print("insert query")
    print(insert_query)
    cursor.execute(insert_query, values)
    conn.commit()
    print("Values")
    print(values)
    try:
        return cursor.lastrowid
    except Exception as e:
        raise(e)
    finally:
      cursor.close()
        

# user_data = {
#     'username': 'Test',
#     'password': 'Test123',
#     'fridgeIDs': ','.join([]),
#     'createdAt': datetime.today().strftime('%Y-%m-%d %H:%M:%S')
# }
# insert_data('User', user_data)