"""The Sync and Aggregation contracts for Edge telemetry batching."""

from __future__ import annotations

from pydantic import Field

from .base import DeepthoughtBaseModel
from .telemetry import TelemetryLog


class TelemetryPayload(DeepthoughtBaseModel):
    """A batch of telemetry logs for synchronization."""

    backpack_id: str
    logs: list[TelemetryLog]
    metadata: dict[str, str] = Field(default_factory=dict)
