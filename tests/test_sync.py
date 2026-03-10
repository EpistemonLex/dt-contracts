"""Tests for the Deepthought sync and aggregation schemas."""

from __future__ import annotations

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
        backpack_id="backpack-001",
        logs=[log],
    )
    assert payload.backpack_id == "backpack-001"
    assert len(payload.logs) == 1
    assert payload.logs[0].action_type == ActionType.VIDEO_PAUSE


def test_telemetry_payload_empty_logs() -> None:
    """Verify that a payload can be created with an empty log list (heartbeat)."""
    payload = TelemetryPayload(
        backpack_id="backpack-001",
        logs=[],
    )
    assert payload.logs == []


def test_sync_memory_sovereignty() -> None:
    """Verify that sync models are frozen."""
    payload = TelemetryPayload(
        backpack_id="dev-1",
        logs=[],
    )

    assert payload.model_config.get("frozen") is True

    with pytest.raises(ValidationError):
        payload.__setattr__("backpack_id", "dev-2")
