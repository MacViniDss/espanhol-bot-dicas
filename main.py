import os
import sqlite3
import requests
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

DB_PATH = os.getenv("DB_PATH", "database.db")
# Telegram's API key
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# Configurar autenticação do Gemini
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Funçoes Logicas com o banco de dados
def get_users():
    # usa a variável de ambiente
    chat_id_env = os.getenv("CHAT_ID")
    if chat_id_env:
        return [int(chat_id_env)]

    # Caso contrário, busca no banco local
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT chat_id FROM users')
            return [row[0] for row in cursor.fetchall()]
    except sqlite3.Error as e:
        print(f"Erro ao acessar o banco de dados: {e}")
        return []

def generate_spanish_tip():
 
    # Prompt padronizado e rigoroso para evitar saídas ruins
    prompt = """
    Você é um professor nativo de espanhol ensinando estudantes brasileiros.
    Crie UMA dica diária de vocabulário ou gramática.
    
    Responda EXATAMENTE neste formato, sem introduções ou conclusões:
    
    🇪🇸 Frase: [Uma frase em espanhol]
    🇧🇷 Tradução: [A tradução correta para o português]
    💡 Explicação: [Uma explicação curta de até 2 linhas sobre a regra ou palavra chave]
    📝 Exemplo extra: [Mais um exemplo rápido usando o mesmo conceito]
    """
    
    # Configuração de geração: baixa criatividade (temperature) para focar na precisão e estrutura
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
        config=types.GenerateContentConfig(temperature=0.2),
    )
    return response.text

def send_telegram_message(chat_id, text):
    """Envia mensagem usando a biblioteca requests (Passo 3)"""
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": str(chat_id),
        "text": text
    }
    
    # Fazemos a chamada HTTP POST direta, ideal para scripts rápidos em CI/CD
    response = requests.post(url, json=payload, timeout=10)
    return response.json()

# Funçoes Gerais
def main():
    print("Iniciando broadcast diário...")
    
    # 1. Gerar Conteúdo
    try:
        print("Gerando dica com Gemini...")
        tip_text = generate_spanish_tip()
        print(tip_text)
    except Exception as e:
        print(f"Erro crítico ao gerar a dica: {e}")
        return

    # 2. Buscar Usuários
    users = get_users()
    if not users:
        print("Nenhum usuário encontrado no banco de dados.")
        return

    # 3. Disparar Mensagens
    print(f"Enviando dica para {len(users)} usuário(s)...")
    for chat_id in users:
        try:
            result = send_telegram_message(chat_id, tip_text)
            if result.get("ok"):
                print(f"✅ Mensagem enviada com sucesso para: {chat_id}")
            else:
                print(f"❌ Falha ao enviar para {chat_id}: {result}")
        except Exception as e:
            print(f"❌ Erro de conexão ao enviar para {chat_id}: {e}")

if __name__ == "__main__":
    # Verifica se as variáveis de ambiente existem antes de rodar
    if not TELEGRAM_TOKEN or not os.getenv("GEMINI_API_KEY"):
        print("ERRO: TELEGRAM_TOKEN ou GEMINI_API_KEY não encontrados.")
        exit(1)
        
    main()
