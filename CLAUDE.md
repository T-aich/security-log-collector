# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project status

Empty repo — nothing built yet. No build/lint/test tooling exists. Once code is added, update this file with the actual commands (do not invent them in the meantime).

## What this is

A mini-SIEM: a collector agent reads Linux host logs (via `journalctl`), ships structured security events over HTTPS to a FastAPI backend, and a detection engine flags suspicious activity (e.g. repeated failed logins → brute-force alert). Grafana visualizes alerts.

## Architecture

Two-host split, not a single deployable unit:

```
Monitored Debian host              VPS (docker compose)
  collector agent  ──HTTPS──▶  proxy ──▶ API ──▶ Postgres
                                 ▲        ▲
                              operator  Grafana
```

- **Collector agent** (VPS1 / monitored host): reads `journalctl`, parses events, POSTs them to the API. Authenticates with a write-scoped API key.
- **API** (VPS2): FastAPI + Pydantic v2, validates and stores events, runs detection logic, writes alerts.
- **Postgres**: event and alert storage, accessed via SQLAlchemy 2.0 (async) + Alembic migrations.
- **Grafana**: reads alerts/events directly from Postgres via a read-only DB role — it does not go through the API.
- No browser talks to the API directly. The only human-facing login in the system is Grafana's.

This scoped-key, no-shared-trust boundary between agent/API/Grafana is a deliberate security design choice (see DECISIONS.md) — preserve it when adding features rather than introducing a shared credential or a browser-facing API endpoint.

## Stack

Python 3.14.6+ · FastAPI · Pydantic v2 · PostgreSQL · SQLAlchemy 2.0 (async) + Alembic · Docker · Grafana

## Decision log

[`DECISIONS.md`](./DECISIONS.md) is an append-only log of past decisions and their reasoning. Check it before making architectural changes, and add a new entry (don't edit old ones) when you make one.
