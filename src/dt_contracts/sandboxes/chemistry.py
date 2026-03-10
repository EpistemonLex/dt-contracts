"""Contracts for Chemistry and Emergent Physics (Sandboxels)."""

from __future__ import annotations

from pydantic import Field

from dt_contracts.base import DeepthoughtBaseModel


class SandboxelsReaction(DeepthoughtBaseModel):
    """An emergent reaction detected in the Sandboxels grid."""

    element_a: str
    element_b: str
    result_element: str
    pos_x: int
    pos_y: int


class ChemistryLabState(DeepthoughtBaseModel):
    """Standard chemistry lab state (e.g. ChemCollective)."""

    beakers: list[dict[str, object]] = Field(default_factory=list) # architectural: allowed-object (Lab State)
    total_volume_ml: float = 0.0
