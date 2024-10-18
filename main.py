import pymysql
import os
import dotenv

dotenv.load_dotenv()

timeout = 10
connection = pymysql.connect(
  charset="utf8mb4",
  connect_timeout=timeout,
  cursorclass=pymysql.cursors.DictCursor,
  db=os.getenv('DB_NAME'),
  host=os.getenv('MAIN_HOST'),
  password=os.getenv('MAIN_PASS'),
  read_timeout=timeout,
  port=os.getenv('DB_PORT'),
  user=os.getenv('DB_USER'),
  write_timeout=timeout,
)
  
try:
  cursor = connection.cursor()
  cursor.execute("CREATE TABLE mytest (id INTEGER PRIMARY KEY)")
  cursor.execute("INSERT INTO mytest (id) VALUES (1), (2)")
  cursor.execute("SELECT * FROM mytest")
  print(cursor.fetchall())
finally:
  connection.close()