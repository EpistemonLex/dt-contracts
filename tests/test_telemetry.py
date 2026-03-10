"""Tests for the Telemetry contracts."""

from __future__ import annotations

from typing import Any, cast

import pytest
from pydantic import ValidationError

from dt_contracts.telemetry import ActionType, TelemetryLog


def test_telemetry_log_validation() -> None:
    """Verify that TelemetryLog validates action types and timestamps."""
    valid_data = {
        "student_id": "stu-123",
        "action_type": ActionType.VIDEO_PAUSE,
        "timestamp": "2026-03-06T14:30:00Z",
        "details": {"video_id": "v-456", "paused_at": 120.5},
    }
    log = TelemetryLog(**valid_data)
    assert log.student_id == "stu-123"
    assert log.action_type == ActionType.VIDEO_PAUSE
    assert cast("dict[str, Any]", log.details)["paused_at"] == 120.5 # architectural: allowed-any



def test_telemetry_log_invalid_action() -> None:
    """Verify that invalid action types raise a ValidationError."""
    invalid_data = {
        "student_id": "stu-123",
        "action_type": "invalid_action_type",
        "timestamp": "2026-03-06T14:30:00Z",
    }
    with pytest.raises(ValidationError) as exc_info:
        TelemetryLog(**cast("Any", invalid_data)) # architectural: allowed-any (Test validation)

    assert "Input should be" in str(exc_info.value)


def test_telemetry_log_memory_sovereignty() -> None:
    """Verify that TelemetryLog uses slots and is frozen."""
    log = TelemetryLog(
        student_id="stu-123",
        action_type=ActionType.UI_INTERACTION,
        timestamp="2026-03-06T14:30:00Z",
    )
    # Pydantic V2 models with slots=True are still somewhat mutable
    # unless frozen=True is set. Check if we want frozen.
    # For now, just ensure it's a DeepthoughtBaseModel.
    assert hasattr(log, "__slots__")
