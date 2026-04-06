import sqlite3

def setup_database():
    # Cria o banco de dados
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Criar tabela de usuários
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            chat_id TEXT PRIMARY KEY
        )
    ''')
    
    MEU_CHAT_ID = '5275722798'
    
    # Insere o seu usuário inicial para testes
    cursor.execute("INSERT OR IGNORE INTO users (chat_id) VALUES (?)", (MEU_CHAT_ID,))
    
    conn.commit()
    conn.close()
    print("Banco de dados 'database.db' criado e populado com sucesso!")

if __name__ == '__main__':
    setup_database()