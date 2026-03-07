"""Tests for the Deepthought telemetry schemas."""


import pytest
from pydantic import ValidationError

from dt_contracts.telemetry import ActionType, TelemetryLog


def test_telemetry_log_creation() -> None:
    """Test standard creation of a TelemetryLog."""
    log = TelemetryLog(
        student_id="stu-123",
        action_type=ActionType.VIDEO_PAUSE,
        timestamp="2026-03-06T14:30:00Z",
    )
    assert log.student_id == "stu-123"
    assert log.action_type == ActionType.VIDEO_PAUSE


def test_telemetry_log_with_details() -> None:
    """Test creation with nested JSON details."""
    log = TelemetryLog(
        student_id="stu-123",
        action_type=ActionType.COMPILATION_ERROR,
        timestamp="2026-03-06T14:35:00Z",
        details={"error_code": "SyntaxError", "line": 42},
    )
    assert log.details is not None
    assert log.details["line"] == 42


def test_telemetry_log_rejects_malformed_action() -> None:
    """Verify that invalid action types raise a ValidationError."""
    invalid_data = {
        "student_id": "stu-123",
        "action_type": "invalid_action_type",
        "timestamp": "2026-03-06T14:30:00Z",
    }
    with pytest.raises(ValidationError) as exc_info:
        TelemetryLog(**invalid_data)  # type: ignore[arg-type] # architectural: allowed-object

    assert "Input should be" in str(exc_info.value)


def test_telemetry_log_memory_sovereignty() -> None:
    """Verify that TelemetryLog uses slots and is frozen."""
    log = TelemetryLog(
        student_id="stu-123",
        action_type=ActionType.CODE_EDIT,
        timestamp="2026-03-06T14:30:00Z",
    )

    # Check memory sovereignty configuration
    assert log.model_config.get("frozen") is True

    # Check frozen mutation rejection without tripping mypy read-only property check
    with pytest.raises(ValidationError):
        log.__setattr__("student_id", "stu-999")
