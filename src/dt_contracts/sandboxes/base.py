"""Base schemas for the Ed-OS Sandbox Ecosystem."""

from datetime import UTC, datetime
from enum import StrEnum

from pydantic import ConfigDict, Field

from dt_contracts.base import DeepthoughtBaseModel


class SandboxType(StrEnum):
    """Supported sandbox engines."""

    KAPLAY = "kaplay"
    PHET = "phet"
    SNAP = "snap"
    SANDBOXELS = "sandboxels"
    BEEPBOX = "beepbox"
    TLDRAW = "tldraw"
    CAD = "cad"
    MINETEST = "minetest"

class TelemetryLevel(StrEnum):
    """Severity of the telemetry event."""

    INFO = "info"
    SUCCESS = "success"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"

class SandboxTelemetry(DeepthoughtBaseModel):
    """The root contract for all events flowing FROM a sandbox TO the Backpack."""

    # Memory Sovereignty
    model_config = ConfigDict(slots=True)

    sandbox_id: str = Field(..., description="Unique UUID for the sandbox session")
    sandbox_type: SandboxType
    event_name: str = Field(..., description="Machine-readable event slug (e.g. 'object_collision')")
    level: TelemetryLevel = TelemetryLevel.INFO
    timestamp: datetime = Field(default_factory=lambda: datetime.now(UTC))

    # Flexible payload for engine-specific data
    # Tagged as object to allow heterogeneous engine data with a marker
    payload: dict[str, object] = Field(default_factory=dict) # architectural: allowed-object (Engine Telemetry)

class SandboxAction(DeepthoughtBaseModel):
    """The root contract for all commands flowing FROM the Backpack TO a sandbox."""

    model_config = ConfigDict(slots=True)

    action_id: str = Field(..., description="Unique UUID for tracking the command")
    cmd: str = Field(..., description="The command slug (e.g. 'pause', 'highlight_code')")
    params: dict[str, object] = Field(default_factory=dict) # architectural: allowed-object (Engine Parameters)
