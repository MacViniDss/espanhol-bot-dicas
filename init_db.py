import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

def setup_database():
    chat_id = os.getenv("CHAT_ID")
    
    if not chat_id:
        print("ERRO: CHAT_ID não encontrado no .env")
        return

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            chat_id TEXT PRIMARY KEY
        )
    ''')
    
    cursor.execute("INSERT OR IGNORE INTO users (chat_id) VALUES (?)", (chat_id,))
    conn.commit()
    conn.close()
    print("Banco de dados criado e populado com sucesso!")

if __name__ == '__main__':
    setup_database()
