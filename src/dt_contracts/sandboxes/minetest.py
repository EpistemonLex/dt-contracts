"""Contracts for the Minetest Voxel Sandbox."""

from __future__ import annotations

from pydantic import Field

from dt_contracts.base import DeepthoughtBaseModel


class VoxelPosition(DeepthoughtBaseModel):
    """A 3D coordinate in the Minetest world."""

    x: float
    y: float
    z: float


class MinetestEvent(DeepthoughtBaseModel):
    """A world event captured by the Luanti mod."""

    event_name: str = Field(..., description="e.g. 'node_placed', 'item_crafted'")
    player_name: str
    pos: VoxelPosition | None = None
    node_type: str | None = None


class MinetestState(DeepthoughtBaseModel):
    """Snapshot of the player and surrounding world."""

    player_pos: VoxelPosition
    player_hp: int
    inventory_count: int
    active_mod_version: str
