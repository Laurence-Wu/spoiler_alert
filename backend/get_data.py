import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

timeout = 10000
dataBaseName = "test1"
def view_data(table_name, conn= None,dataBase=dataBaseName,):
    if conn is None:     
      conn = pymysql.connect(
          charset="utf8mb4",
          cursorclass=pymysql.cursors.DictCursor,
          host="localhost",
          user="root",
          password=os.getenv("LocalPassword"),
          database=dataBase,
          port=3306
      )
    conn.autocommit = True
    cursor = conn.cursor()

    select_query = f"SELECT * FROM {table_name}"

    cursor.execute(select_query)

    rows = cursor.fetchall()

    column_names = [i[0] for i in cursor.description]

    # print(f"\nData from {table_name}:")
    # print(column_names)
    # for row in rows:
    #     print(row)

    cursor.close()
    # print("=====rows=====")
    # print(rows)
    # print()
    return rows

# view_data('User')
# view_data('Fridge')
# view_data('FridgeContent')
# view_data('Recipe')
# view_data('FridgeAccess')
# view_data('Wishlist')
# view_data('WishlistItems')