import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def conectar():
    host = os.getenv("DB_HOST")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    database = os.getenv("DB_DATABASE")
    
    try:
        conexao = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        return conexao
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar no banco de dados: {erro}")
        return None
