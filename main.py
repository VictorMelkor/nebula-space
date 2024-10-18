import pymysql
import os
import dotenv

# Carregar variáveis de ambiente do arquivo .env
dotenv.load_dotenv()

timeout = 10

# Estabelecer a conexão com o banco de dados
connection = pymysql.connect(
    charset="utf8mb4",
    connect_timeout=timeout,
    cursorclass=pymysql.cursors.DictCursor,
    db=os.getenv('DB_NAME'),
    host=os.getenv('MAIN_HOST'),
    password=os.getenv('MAIN_PASS'),
    read_timeout=timeout,
    port=int(os.getenv('DB_PORT', 3306)),  # Certifique-se de que a porta é um inteiro
    user=os.getenv('DB_USER'),
    write_timeout=timeout,
)

try:
    with connection.cursor() as cursor:
        # Criar tabela se não existir
        cursor.execute("CREATE TABLE IF NOT EXISTS mytest (id INTEGER PRIMARY KEY)")
        
        # Inserir dados
        cursor.execute("INSERT INTO mytest (id) VALUES (1), (2)")
        
        # Selecionar e imprimir os dados
        cursor.execute("SELECT * FROM mytest")
        print(cursor.fetchall())

    # Commit as alterações
    connection.commit()
finally:
    connection.close()
