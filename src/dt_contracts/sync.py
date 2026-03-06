"""The Sync and Aggregation contracts for Edge telemetry batching."""

from pydantic import Field

from .base import DeepthoughtBaseModel
from .telemetry import TelemetryLog


class TelemetryPayload(DeepthoughtBaseModel):
    """A batch container for Edge telemetry synchronization."""

    device_id: str = Field(..., description="Unique identifier for the edge hardware")
    session_id: str = Field(..., description="The student session identifier")
    logs: list[TelemetryLog] = Field(
        default_factory=list, description="A batch of individual telemetry entries",
    )
    sent_at: str = Field(..., description="ISO 8601 timestamp of when the payload was sent")
    metadata: dict[str, str] = Field(
        default_factory=dict, description="Additional context for the sync event",
    )
