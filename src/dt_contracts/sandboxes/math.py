"""Contracts for Mathematical and Geometrical sandboxes."""

from pydantic import ConfigDict, Field

from dt_contracts.base import DeepthoughtBaseModel


class MathEntity(DeepthoughtBaseModel):
    """A mathematical object (point, line, tile)."""

    model_config = ConfigDict(slots=True)

    id: str
    kind: str = Field(..., description="e.g. 'point', 'fraction_tile', 'polygon'")
    definition: str = Field(..., description="Algebraic definition or value")

class MathState(DeepthoughtBaseModel):
    """The state of a math playground (Mathigon/GeoGebra)."""

    model_config = ConfigDict(slots=True)

    entities: list[MathEntity]
    last_equation: str | None = None
    is_balanced: bool | None = None  # For algebra scales
