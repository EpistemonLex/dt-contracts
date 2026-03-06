"""Architectural tests to enforce Sovereign Schema Mandates."""

import re
from pathlib import Path

import pytest

ANY_PATTERN = r"\bAny\b"
OBJECT_PATTERN = r': object\b|-> object\b|cast\("?object"?,'
ALLOWED_MARKER = "# architectural: allowed-object"


def check_file_typing(path: Path) -> list[str]:
    """Verify that a file complies with typing constraints."""
    errors = []
    content = path.read_text(encoding="utf-8")
    for i, line in enumerate(content.splitlines(), 1):
        if (
            re.search(ANY_PATTERN, line)
            and not line.strip().startswith(("import ", "from ", "#"))
            and "# type: ignore" not in line
        ):
            errors.append(f"Line {i}: Illegal 'Any' usage.")
        if re.search(OBJECT_PATTERN, line) and ALLOWED_MARKER not in line:
            errors.append(f"Line {i}: Illegal 'object' usage without marker.")
    return errors


def check_file_sovereignty(path: Path) -> list[str]:
    """Check that models inherit from DeepthoughtBaseModel, not BaseModel directly."""
    errors = []
    content = path.read_text(encoding="utf-8")
    if "from pydantic import BaseModel" in content or "import BaseModel" in content:
        errors.append(
            "Illegal direct import of 'BaseModel'. Must inherit from 'DeepthoughtBaseModel' to ensure memory sovereignty.",
        )
    return errors


@pytest.mark.parametrize("folder", ["src", "tests"])
def test_typing_standards(folder: str) -> None:
    """Ensure Zero-Any Vacuum and Object Sovereignty."""
    root = Path(folder)
    all_errors = []
    for p in root.rglob("*.py"):
        if p.name == "test_architecture.py":
            continue
        errors = check_file_typing(p)
        if errors:
            all_errors.append(f"\n{p}: " + " ".join(errors))
    if all_errors:
        pytest.fail("".join(all_errors))


def test_model_sovereignty_ratchet() -> None:
    """Ensure no one bypasses DeepthoughtBaseModel in the contracts."""
    root = Path("src/dt_contracts")
    all_errors = []
    for p in root.rglob("*.py"):
        if p.name == "base.py":
            continue  # Allowed to import BaseModel here
        errors = check_file_sovereignty(p)
        if errors:
            all_errors.append(f"\n{p}: " + " ".join(errors))
    if all_errors:
        pytest.fail("".join(all_errors))
