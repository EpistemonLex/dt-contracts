"""Snap! block-based coding contracts."""

from __future__ import annotations

from pydantic import Field

from dt_contracts.base import DeepthoughtBaseModel


class SnapBlock(DeepthoughtBaseModel):
    """Representation of a single coding block."""

    id: str
    selector: str
    parameters: list[object] = Field(default_factory=list) # architectural: allowed-object (Block Params)


class SnapSprite(DeepthoughtBaseModel):
    """The state of a sprite in Snap!."""

    name: str
    scripts_count: int
    costume_name: str
    pos_x: float
    pos_y: float


class SnapState(DeepthoughtBaseModel):
    """The full project state of a Snap! environment."""

    project_name: str
    sprites: list[SnapSprite]
    variables: dict[str, object] = Field(default_factory=dict) # architectural: allowed-object (Dynamic block variables)
    is_running: bool = False
