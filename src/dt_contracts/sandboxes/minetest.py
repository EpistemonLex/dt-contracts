"""Contracts for the Minetest Voxel Sandbox."""

from pydantic import ConfigDict, Field

from dt_contracts.base import DeepthoughtBaseModel


class VoxelPosition(DeepthoughtBaseModel):
    """A 3D coordinate in the Minetest world."""

    model_config = ConfigDict(slots=True)
    x: float
    y: float
    z: float

class BlockEvent(DeepthoughtBaseModel):
    """Telemetry for block placement or destruction."""

    model_config = ConfigDict(slots=True)

    pos: VoxelPosition
    block_name: str = Field(..., description="e.g. 'default:dirt', 'mesecons:wire'")
    action: str = Field(..., description="'place' or 'dig'")

class MinetestState(DeepthoughtBaseModel):
    """Snapshot of the player and surrounding world."""

    model_config = ConfigDict(slots=True)

    player_pos: VoxelPosition
    player_hp: int
    inventory_count: int
    active_mod_version: str
