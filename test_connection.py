
import os
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    if connection.is_connected():
        print("Conexão bem-sucedida ao banco de dados")
except Error as e:
    print(f"Erro de conexão: {e}")
finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()