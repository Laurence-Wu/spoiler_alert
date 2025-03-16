import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

try:
    conn = pymysql.connect(
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
        host="localhost",
        user="root",
        password=os.getenv("LocalPassword"),
        database="test1",
        port=3306
    )
    print("✅ Connected successfully!")
    with conn.cursor() as cursor:
        cursor.execute("SELECT * from testTable where age == 22;")
        print(cursor.fetchone())
    conn.close()
except Exception as e:
    print(f"❌ Connection failed: {e}")