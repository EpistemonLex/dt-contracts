"""Kaplay.js specific sandbox contracts."""

from __future__ import annotations

from pydantic import Field

from dt_contracts.base import DeepthoughtBaseModel


class Vector2(DeepthoughtBaseModel):
    """Simple 2D coordinate."""

    x: float
    y: float


class KaplaySprite(DeepthoughtBaseModel):
    """A sprite instance in the game world."""

    id: str
    tags: list[str] = Field(default_factory=list)
    pos: Vector2
    hp: int | None = None


class KaplayState(DeepthoughtBaseModel):
    """The full state of a Kaplay.js game."""

    sprites: list[KaplaySprite]
    score: int = 0
    time_elapsed: float = 0.0


class KaplayEvent(DeepthoughtBaseModel):
    """A high-frequency event from the Kaplay harvester."""

    event_type: str = Field(..., description="e.g. 'collision', 'input', 'death'")
    actor_id: str
    target_id: str | None = None
    payload: dict[str, object] = Field(default_factory=dict) # architectural: allowed-object (Engine Event)
