"""Base schemas for the Ed-OS Sandbox Ecosystem."""

from __future__ import annotations

from datetime import UTC, datetime
from enum import StrEnum

from pydantic import Field

from dt_contracts.base import DeepthoughtBaseModel


class SandboxType(StrEnum):
    """Supported sandbox engines."""

    # Game Dev
    KAPLAY = "kaplay"

    # Science & Simulations
    PHET = "phet"
    MOLWORKBENCH = "molworkbench"
    NETLOGO = "netlogo"
    SANDBOXELS = "sandboxels"

    # CS & Logic
    SNAP = "snap"
    MAKECODE = "makecode"
    TURBOWARP = "turbowarp"

    # Narrative
    RENPY = "renpy"

    # Design & Art
    TLDRAW = "tldraw"
    PISKEL = "piskel"
    CAD = "cad" # BlocksCAD & OpenJSCAD

    # Math
    MATHIGON = "mathigon"
    GEOGEBRA = "geogebra"

    # Music
    BEEPBOX = "beepbox"
    STRUDEL = "strudel"
    SONIC_PI = "sonic_pi"
    AUDIOMASS = "audiomass"

    # Electronics
    CIRCUITJS = "circuitjs"
    QJS = "qjs"

    # Spatial
    MINETEST = "minetest"

    # Data & Literate
    STARBOARD = "starboard"

    # Wild Curiosity
    BROWSER = "browser"

class TelemetryLevel(StrEnum):
    """Severity of the telemetry event."""

    INFO = "info"
    SUCCESS = "success"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"

class SandboxTelemetry(DeepthoughtBaseModel):
    """The root contract for all events flowing FROM a sandbox TO the Backpack."""

    # Note: sandbox_id is optional to accommodate simple harvesters
    sandbox_id: str | None = Field(None, description="Unique UUID for the sandbox session")
    sandbox_type: SandboxType
    event_name: str = Field(..., description="Machine-readable event slug (e.g. 'object_collision')")
    level: TelemetryLevel = TelemetryLevel.INFO
    timestamp: datetime = Field(default_factory=lambda: datetime.now(UTC))

    # Flexible payload for engine-specific data
    # Tagged as object to allow heterogeneous engine data with a marker
    payload: dict[str, object] = Field(default_factory=dict) # architectural: allowed-object (Engine Telemetry)

class SandboxAction(DeepthoughtBaseModel):
    """The root contract for all commands flowing FROM the Backpack TO a sandbox."""

    action_id: str = Field(..., description="Unique UUID for tracking the command")
    cmd: str = Field(..., description="The command slug (e.g. 'pause', 'highlight_code')")
    params: dict[str, object] = Field(default_factory=dict) # architectural: allowed-object (Engine Parameters)
