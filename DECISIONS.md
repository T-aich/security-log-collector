# Decisions

Append-only log of decisions and their reasoning. Add a new entry per decision; don't edit or delete old ones — if a decision changes, add a new entry that supersedes it.

## 2026-08-03 — Two-VPS split with scoped API keys

Collector agent (VPS1) and API/DB/Grafana (VPS2) are separate hosts. The agent authenticates with a write-scoped API key; Grafana connects to Postgres with a read-only role. No browser talks to the API directly — the only human-facing login is Grafana.

**Why:** limits blast radius if either host or key is compromised — a leaked agent key can't read data or touch Grafana, and Grafana can't write to the DB.

## 2026-08-03 — Stack choice

Python 3.14.6+, FastAPI, Pydantic v2, PostgreSQL, SQLAlchemy 2.0 (async) + Alembic, Docker, Grafana.

**Why:** chosen to learn backend/devops/security fundamentals in Python — async web framework, typed validation, real migrations, and containerized multi-host deployment.
