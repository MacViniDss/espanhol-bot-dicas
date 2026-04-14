# 🇪🇸 SpanishBot — Aprenda Espanhol no Telegram


## Status Atual: V1.0

Durante a fase **Beta**:

O bot é capaz de:
- 🤖 Gerar dicas únicas de vocabulário e gramática com Inteligência Artificial (Gemini 2.5 Flash)
- 📬 Enviar as dicas diretamente no Telegram para os usuários cadastrados
- 🗃️ Gerenciar usuários via banco de dados SQLite

O script é executado **manualmente** nesta fase, servindo como prova de conceito para validar toda a pipeline: IA → banco de dados → Telegram.

---


**Pré-requisito:** O usuário precisa ter enviado `/start` para o bot no Telegram antes de receber mensagens.

---

## 🗺️ Roadmap

### ✅ Beta
- [x] Integração com Google Gemini AI
- [x] Envio de mensagens via Telegram Bot API
- [x] Banco de dados SQLite com lista de usuários
- [x] Execução manual do script

---

### 🔜 Versão 1.0 — Automação com GitHub Actions

A **grande evolução** da V1 é a automação completa via **GitHub Actions**.

Em vez de rodar o script manualmente, o próprio GitHub dispara o bot **todos os dias, automaticamente e de graça** — sem precisar de servidor, sem custo de infraestrutura.

**Como vai funcionar:**

```
⏰ Todo dia às 8h (horário configurável)
        ↓
  GitHub Actions acorda
        ↓
  Executa o main.py
        ↓
  Gemini gera a dica do dia
        ↓
  Todos os usuários recebem no Telegram ✅
```

**O que foi na V1:**
- [x] Workflow `.github/workflows/daily_tip.yml` com `schedule: cron`
- [x] `TELEGRAM_TOKEN` e `GEMINI_API_KEY` armazenados como **GitHub Secrets** (seguro)
- [x] Logs de execução visíveis direto no painel do GitHub
- [x] Zero custo — GitHub Actions oferece 2.000 minutos/mês gratuitos para repositórios públicos

---

### Problema encontrado: 
Em uma manhã não recebi a dica diária do meu Agente IA de Aulas de Espanhol, pelo que eu vi ele encontrou o primeiro problema real: erro 503 UNAVAILABLE no Gemini 2.5 Flash às 08:00 em ponto.
Em outras palavras, a maioria dos workflows de automação é configurada nos horarios de picos. Quando milhares de bots acordam todos ao mesmo tempo (08:00:00), os clusters de processamento sofrem um pico de estresse.
Solução rápida: mudei o cron para 09:12 UTC, que conrresponde às 06:12 no horário de brasília. 

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Uso |
|---|---|
| Python 3 | Linguagem principal |
| Google Gemini 2.5 Flash | Geração das dicas com IA |
| Telegram Bot API | Envio das mensagens |
| SQLite | Armazenamento dos usuários |
| python-dotenv | Gerenciamento de variáveis de ambiente |
| GitHub Actions *(V1)* | Automação e agendamento diário |

---

## 📄 Licença

MIT License — sinta-se livre para usar, modificar e distribuir.
