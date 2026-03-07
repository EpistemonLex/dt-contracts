"""Contracts for Electronics and Digital Logic sandboxes."""

from pydantic import ConfigDict, Field

from dt_contracts.base import DeepthoughtBaseModel


class CircuitComponent(DeepthoughtBaseModel):
    """A single component in a circuit (resistor, gate, etc.)."""

    model_config = ConfigDict(slots=True)

    id: str
    type: str = Field(..., description="e.g. 'resistor', 'nand_gate'")
    voltage: float | None = None
    current: float | None = None
    state: str | None = None  # e.g. 'on', 'off' for gates

class ElectronicsState(DeepthoughtBaseModel):
    """The full state of a circuit simulation."""

    model_config = ConfigDict(slots=True)

    components: list[CircuitComponent]
    has_short_circuit: bool = False
    simulation_time: float
