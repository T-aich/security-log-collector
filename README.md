# Mini-SIEM — Security Log Monitoring System

A collector agent reads Linux host logs, ships structured security events to a FastAPI backend, and a detection engine flags suspicious activity. Grafana renders it.

**Status:** empty repo, nothing built yet.

## Shape

```
Monitored Debian host              VPS (docker compose)
  collector agent  ──HTTPS──▶  proxy ──▶ API ──▶ Postgres
                                 ▲        ▲
                              operator  Grafana
```

Agent authenticates with a write-scoped API key, Grafana with a read-scoped one. No browser talks to the API; the only human login is Grafana's.

## Stack

Python 3.14.6+ · FastAPI · Pydantic v2 · PostgreSQL · SQLAlchemy 2.0 (async) + Alembic · Docker · Grafana

## Getting started

Nothing to run yet.

## Why things are the way they are

[`DECISIONS.md`](./DECISIONS.md) — append-only log of decisions and their reasoning.
