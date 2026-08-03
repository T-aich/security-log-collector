# Decisions

Append-only log of decisions and their reasoning. Add a new entry per decision; don't edit or delete old ones — if a decision changes, add a new entry that supersedes it.

## 2026-08-03 — Two-VPS split with scoped API keys

Collector agent (VPS1) and API/DB/Grafana (VPS2) are separate hosts. The agent authenticates with a write-scoped API key; Grafana connects to Postgres with a read-only role. No browser talks to the API directly — the only human-facing login is Grafana.

**Why:** limits blast radius if either host or key is compromised — a leaked agent key can't read data or touch Grafana, and Grafana can't write to the DB.

## 2026-08-03 — Stack choice

Python 3.14.6+, FastAPI, Pydantic v2, PostgreSQL, SQLAlchemy 2.0 (async) + Alembic, Docker, Grafana.

**Why:** chosen to learn backend/devops/security fundamentals in Python — async web framework, typed validation, real migrations, and containerized multi-host deployment.

## 2026-08-03 — Pin direct dependencies with `==`

`requirements.txt` and `requirements-dev.txt` pin every direct dependency to an exact version. Transitive dependencies are deliberately left unpinned — no lockfile, no hashes.

**Why:** the files were originally unpinned, so CI resolved fresh versions on every run and the `pip-audit` gate said nothing about what was actually installed on either host. Exact pins on direct deps make the collector host and the API host agree on the versions that matter, and make upgrades an explicit, reviewable diff.

**Known limitation:** transitive deps (`starlette`, `anyio`, `h11`, `greenlet`, …) still float, so builds are not fully reproducible and a compromised transitive release can still land silently. A compiled, hash-pinned lockfile (`pip-compile --generate-hashes` or `uv pip compile`) was considered and deferred as more setup than the project needs at this stage — revisit before anything is deployed to a real VPS.
