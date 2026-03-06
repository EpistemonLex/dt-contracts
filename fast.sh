#!/bin/bash
set -e
echo "--- Syncing Environment ---"
uv sync --all-extras
echo "--- Linting (Ruff) ---"
uv run ruff check . --fix
echo "--- Zero-Any Vacuum Check ---"
if grep -r "Any" src/ | grep -v "ANY" | grep -v "#"; then
    echo "ERROR: Literal 'Any' detected in src/"
    exit 1
fi
echo "--- Typing (Mypy) ---"
uv run mypy . --strict
echo "--- Testing (Pytest) ---"
uv run pytest --cov=src --cov-report=term-missing
