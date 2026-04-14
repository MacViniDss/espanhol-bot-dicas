# 🇪🇸 SpanishBot — Learn Spanish on Telegram

## Current Status: V1.0

During the **Beta** phase:

The bot is capable of:
- 🤖 Generating unique vocabulary and grammar tips using Artificial Intelligence (Gemini 2.5 Flash)
- 📬 Sending tips directly on Telegram to registered users
- 🗃️ Managing users via an SQLite database

The script is executed **manually** at this stage, serving as a proof of concept to validate the entire pipeline: AI → database → Telegram.

---

**Prerequisite:** The user must have sent `/start` to the bot on Telegram before receiving messages.

---

## 🗺️ Roadmap

### ✅ Beta
- [x] Integration with Google Gemini AI
- [x] Message delivery via Telegram Bot API
- [x] SQLite database with user list
- [x] Manual script execution

---

### 🔜 Version 1.0 — Automation with GitHub Actions

The **major upgrade** in V1 is full automation via **GitHub Actions**.

Instead of running the script manually, GitHub itself triggers the bot **every day, automatically and for free** — no server required, no infrastructure cost.

**How it works:**
⏰ Every day at 6:00 AM - 7:00 AM (configurable time)
↓
GitHub Actions wakes up
↓
Runs main.py
↓
Gemini generates the daily tip
↓
All users receive it on Telegram ✅

**What was implemented in V1:**
- [x] `.github/workflows/daily_tip.yml` workflow with `schedule: cron`
- [x] `TELEGRAM_TOKEN` and `GEMINI_API_KEY` stored as **GitHub Secrets** (secure)
- [x] Execution logs available directly in the GitHub dashboard
- [x] Zero cost — GitHub Actions provides 2,000 free minutes/month for public repositories

---

### Issue encountered:
One morning I didn’t receive the daily tip from my Spanish Learning AI Agent. After investigating, I found the first real issue: a 503 UNAVAILABLE error from Gemini 2.5 Flash at exactly 08:00.

In other words, most automation workflows are scheduled at peak times. When thousands of bots wake up simultaneously (08:00:00), processing clusters experience a spike in load.

**Quick fix:** I changed the cron schedule to 09:12 UTC, which corresponds to 06:12 AM (Brasília time).

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Main programming language |
| Google Gemini 2.5 Flash | AI-powered tip generation |
| Telegram Bot API | Message delivery |
| SQLite | User storage |
| python-dotenv | Environment variable management |
| GitHub Actions *(V1)* | Automation and daily scheduling |

---

## 📄 License

MIT License — feel free to use, modify, and distribute.
