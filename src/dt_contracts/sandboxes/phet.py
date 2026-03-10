"""Contracts for PhET Interactive Simulations."""

from __future__ import annotations

from dt_contracts.base import DeepthoughtBaseModel


class PhetVariable(DeepthoughtBaseModel):
    """A granular variable from a PhET simulation state."""

    name: str
    value: float | str | bool
    units: str | None = None


class PhetState(DeepthoughtBaseModel):
    """Snapshot of a PhET simulation."""

    sim_id: str
    variables: list[PhetVariable]
    screen_id: str | None = None
