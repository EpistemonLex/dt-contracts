"""Tests for the Deepthought sync and aggregation schemas."""

import pytest
from pydantic import ValidationError

from dt_contracts.sync import TelemetryPayload
from dt_contracts.telemetry import ActionType, TelemetryLog


def test_telemetry_payload_creation() -> None:
    """Test standard creation of a TelemetryPayload batch."""
    log = TelemetryLog(
        student_id="stu-123",
        action_type=ActionType.VIDEO_PAUSE,
        timestamp="2026-03-06T15:00:00Z",
    )
    payload = TelemetryPayload(
        device_id="chromebook-001",
        session_id="sess-999",
        logs=[log],
        sent_at="2026-03-06T15:05:00Z",
    )
    assert payload.device_id == "chromebook-001"
    assert len(payload.logs) == 1
    assert payload.logs[0].action_type == ActionType.VIDEO_PAUSE


def test_telemetry_payload_empty_logs() -> None:
    """Verify that a payload can be created with an empty log list (heartbeat)."""
    payload = TelemetryPayload(
        device_id="chromebook-001",
        session_id="sess-999",
        logs=[],
        sent_at="2026-03-06T15:10:00Z",
    )
    assert payload.logs == []


def test_sync_memory_sovereignty() -> None:
    """Verify that sync models are frozen."""
    payload = TelemetryPayload(
        device_id="dev-1",
        session_id="sess-1",
        logs=[],
        sent_at="now",
    )

    assert payload.model_config.get("frozen") is True

    with pytest.raises(ValidationError):
        payload.__setattr__("device_id", "dev-2")
