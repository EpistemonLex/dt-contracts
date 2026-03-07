"""Contracts for Chemistry and Thermodynamics sandboxes."""

from pydantic import ConfigDict, Field

from dt_contracts.base import DeepthoughtBaseModel


class ReactionEvent(DeepthoughtBaseModel):
    """Telemetry for a chemical reaction event."""

    model_config = ConfigDict(slots=True)

    element_a: str
    element_b: str
    result: str
    pos_x: int
    pos_y: int

class ChemistryState(DeepthoughtBaseModel):
    """The state of a grid-based chemistry simulation (e.g. Sandboxels)."""

    model_config = ConfigDict(slots=True)

    temperature_avg: float
    active_elements: list[str] = Field(..., description="Unique elements currently in the grid")
    element_counts: dict[str, int] = Field(default_factory=dict) # architectural: allowed-object (Dynamic counts)
