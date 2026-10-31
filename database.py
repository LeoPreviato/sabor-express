import sqlite3

ARQUIVO_BANCO = "sabor_express.db"

def conectar():
    try:
        conexao = sqlite3.connect(ARQUIVO_BANCO)
        conexao.execute("PRAGMA foreign_keys = ON")
        return conexao
    except sqlite3.Error as erro:
        print(f"Erro ao conectar ao banco de dados: {erro}")
        return None
    
def criar_tabela():
    conexao = conectar()
    if conexao is None:
        return
    cursor = conexao.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS restaurantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT UNIQUE NOT NULL,
            categoria TEXT NOT NULL,
            ativo INTEGER DEFAULT 0
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pratos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            restaurante_id INTEGER NOT NULL,
            nome  TEXT NOT NULL,
            preco REAL NOT NULL,
            descricao TEXT,
            FOREIGN KEY (restaurante_id) REFERENCES restaurantes(id) ON DELETE CASCADE
        )
    """)
    
    conexao.commit()
    cursor.close()
    conexao.close()