"""Contracts for Electronics and Digital Logic sandboxes."""

from __future__ import annotations

from pydantic import Field

from dt_contracts.base import DeepthoughtBaseModel


class CircuitComponent(DeepthoughtBaseModel):
    """A single component in a simulated circuit (CircuitJS)."""

    id: str
    type: str = Field(..., description="e.g. 'resistor', 'led', 'battery'")
    value: float | str
    connections: list[str] = Field(default_factory=list)


class ElectronicsState(DeepthoughtBaseModel):
    """The state of a circuit simulation."""

    components: list[CircuitComponent]
    is_simulating: bool = False
    v_source: float = 0.0
