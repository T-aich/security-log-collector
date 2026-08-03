# Mini-SIEM — Security Log Monitoring System

A collector agent reads Linux host logs, ships structured security events to a FastAPI backend, and a detection engine flags suspicious activity. Grafana renders it.

**Status:** project setup done. Postgres runs locally via `docker compose`, `api/` has a minimal FastAPI skeleton (`/health` only), lint/type/audit tooling is enforced in CI. No persistence, auth, or detection logic yet.

## Shape

```
Monitored Debian host              VPS (docker compose)
  collector agent  ──HTTPS──▶  proxy ──▶ API ──▶ Postgres
                                 ▲        ▲
                              operator  Grafana
```

The agent authenticates to the API with a write-scoped API key. Grafana never touches the API — it reads Postgres directly through a read-only DB role. No browser talks to the API; the only human login is Grafana's.

## Stack

Python 3.14.6+ · FastAPI · Pydantic v2 · PostgreSQL · SQLAlchemy 2.0 (async) + Alembic · Docker · Grafana

## Getting started

```bash
source .venv/Scripts/activate            # .venv\Scripts\activate on PowerShell
pip install -r requirements.txt -r requirements-dev.txt
docker compose up -d postgres
uvicorn api.main:app --reload            # http://127.0.0.1:8000/health
```

Checks, all enforced in CI:

```bash
ruff check . && ruff format --check .
mypy .
pip-audit -r requirements.txt -r requirements-dev.txt
```

## Why things are the way they are

[`DECISIONS.md`](./DECISIONS.md) — append-only log of decisions and their reasoning.
