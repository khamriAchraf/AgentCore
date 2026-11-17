# AgentCore

AgentCore is a Python platform for configuring, executing, and evaluating LLM agents. It is being delivered in small phases; the current Phase 1 slice is a minimal FastAPI application with validated settings and health endpoints.

## Requirements

- Python 3.11 or newer

Phase 1 does not connect to Neon, Upstash, or Gemini. No database, Redis server, Docker, or cloud credentials are required to run the API or tests.

## Local setup (Windows PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn agentcore.main:app --reload
```

The root `.env` is optional. `.env.example` documents the current application settings; inspect it and add settings to an existing `.env` rather than overwriting local credentials.

Check the health endpoints:

- `http://127.0.0.1:8000/health/live`
- `http://127.0.0.1:8000/health/ready`

## Checks

```powershell
.\.venv\Scripts\python.exe -m ruff check .
.\.venv\Scripts\python.exe -m ruff format --check .
.\.venv\Scripts\python.exe -m mypy src tests
.\.venv\Scripts\python.exe -m pytest
.\.venv\Scripts\python.exe -m build
```

The test suite uses in-process API tests and does not make network calls. GitHub Actions runs the same quality checks on Python 3.11, 3.12, and 3.13.

## Current limitations

- Agent registration, execution, persistence, authentication, and provider integrations are planned for later phases and are not implemented yet.
- Readiness currently checks application startup only because Phase 1 has no external dependencies.
