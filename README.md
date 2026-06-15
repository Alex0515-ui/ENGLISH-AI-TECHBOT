# 🤖 ENGLISH-AI-TECHBOT — Telegram Bot for Learning English with AI

A Python-based Telegram bot built as a personal tool for learning English — featuring AI-powered dialogue, a level system, and multiple learning modes. Runs via webhook and is deployed with Docker Compose.

---

## 📋 Table of Contents

- [About](#about)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Quick Start](#quick-start)
- [Webhook Setup (ngrok)](#webhook-setup-ngrok)
- [Management Commands](#management-commands)
- [Seeding the Database](#seeding-the-database)
- [Testing](#testing)
- [Environment Variables](#environment-variables)

---

## About

This project was built to solve a personal problem: most English learning services are either paid or don't fit real developer workflows.

The bot was created for:

- practicing English through live dialogue
- learning vocabulary in context
- understanding technical documentation

> 👉 **Core idea:** learn English through real use and AI interaction.

### Key Features

- **AI Dialogue** — conversational practice powered by Groq API (LLM)
- **Word Dictionary** — a database of words auto-populated via Gemini API (`seed_words.py`)
- **Translation Practice** — user translates sentences; AI checks and analyzes the response
- **Level System** — 6 difficulty levels (from basic to advanced)
- **Learning Modes:**
  - `general` — everyday English (casual speech)
  - `tech` — technical English (documentation reading and development)
- **Telegram Webhook** — processes updates over HTTP (no polling)
- **REST API** — handles business logic and data management
- **PostgreSQL** — stores words, progress, and states
- **Redis** — temporary data and session storage
- **Celery** — background tasks (e.g. word generation)
- **Tests** — coverage via pytest

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Primary language |
| Webhook (Telegram Bot API) | Receiving updates |
| SQLAlchemy / Alembic | ORM and migrations |
| PostgreSQL | Primary database |
| Redis | Temporary data storage |
| Celery | Background task queue |
| Groq API | AI dialogue and answer checking |
| Gemini API | Word generation |
| Docker & Docker Compose | Containerization |
| pytest | Testing |

---

## Project Structure

```
TG_BOT/
└── bot/
    ├── docker-compose.yml      # Services (db, redis, web, worker)
    ├── Dockerfile              # Application image
    ├── tasks.py                # Celery tasks
    ├── telegram.py             # Telegram webhook handler
    ├── main.py                 # Entry point
    ├── seed_words.py           # Word generation via Gemini
    ├── alembic/                # Migrations
    ├── app/
    │   ├── handlers/           # Message handlers
    │   ├── AI/                 # Groq/Gemini integration
    │   ├── db/                 # Database configuration
    │   ├── entities/           # ORM models
    │   └── services/           # Business logic
    └── tests/                  # Tests
```

---

## Quick Start

### Requirements

- Docker and Docker Compose
- Telegram Bot Token
- API keys:
  - Groq (dialogue)
  - Gemini (word generation)

### 1. Clone the Repository

```bash
git clone https://github.com/Alex0515-ui/TG_BOT.git
cd TG_BOT
```

### 2. Configure Environment Variables

```bash
cd bot
cp .env.example .env
```

### 3. Run

```bash
docker-compose up --build
```

---

## 🌐 Webhook Setup (ngrok)

Since Telegram requires a public HTTPS URL for webhooks, ngrok is used during local development.

### Requirements

- [ngrok](https://ngrok.com/)
- ngrok account and authtoken

### 1. Install ngrok

Download and unpack ngrok.

### 2. Get Your Authtoken

- [Sign up](https://dashboard.ngrok.com/signup)
- [Get your token](https://dashboard.ngrok.com/get-started/your-authtoken)

### 3. Add the Token

```bash
ngrok config add-authtoken YOUR_TOKEN_HERE
```

### 4. Start ngrok

```bash
ngrok http 8000
```

You'll receive a URL like: `https://xxxx.ngrok-free.app`

### 5. Set the Webhook

Add to `.env`:

```env
WEBHOOK_URL=https://xxxx.ngrok-free.app/webhook
```

Restart the project:

```bash
docker-compose down
docker-compose up
```

> ⚠️ **Note:** The URL changes on every ngrok restart — update `WEBHOOK_URL` accordingly. For local development only.

> ❌ **ERR_NGROK_4018** — authtoken not added. Fix: `ngrok config add-authtoken YOUR_TOKEN_HERE`

---

## Management Commands

| Command | Description |
|---|---|
| `docker-compose up --build` | Build and start |
| `docker-compose up -d` | Start in background |
| `docker-compose down` | Stop all services |
| `docker-compose logs -f` | Stream logs |
| `docker-compose ps` | Check service status |

---

## Seeding the Database

```bash
docker-compose exec web python seed_words.py
```

Uses the Gemini API to generate and populate words.

---

## Testing

```bash
python -m pytest
```

Inside Docker:

```bash
docker-compose exec web python -m pytest
```

---

## Environment Variables

```env
POSTGRES_DB=...
POSTGRES_USER=...
POSTGRES_PASSWORD=...
DATABASE_URL=...

REDIS_HOST=redis
REDIS_PORT=6379

BOT_TOKEN=...

GROQ_API_KEY=...
GEMINI_API_KEY=...
WEBHOOK_URL=...
```

---

## Summary

This project demonstrates:

- Backend development with multiple interconnected services
- Webhook-based update handling instead of polling
- Integration with multiple AI APIs
- Task queue management with Celery
- Redis and PostgreSQL in production-like setup
- Full containerization with Docker
- Test coverage with pytest

> 👉 **Main focus:** automating English learning through AI and backend engineering.

---

## License

MIT License
