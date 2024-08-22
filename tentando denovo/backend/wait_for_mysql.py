import time
import mysql.connector
from mysql.connector import Error

# Configurações do banco de dados
db_config = {
    'host': 'mysql_database',
    'user': 'root',
    'password': 'root',
    'database': 'catalogo'
}

def wait_for_mysql(config, max_retries=30, delay=5):
    retries = 0
    while retries < max_retries:
        try:
            connection = mysql.connector.connect(**config)
            if connection.is_connected():
                print("Conectado ao MySQL com sucesso!")
                connection.close()
                return True
        except Error as e:
            print(f"Não foi possível conectar ao MySQL: {e}")
        time.sleep(delay)
        retries += 1
    return False

if __name__ == "__main__":
    success = wait_for_mysql(db_config)
    if not success:
        print("Não foi possível conectar ao MySQL após várias tentativas.")
        exit(1)