"""High-fidelity Action contracts for specific sandbox interventions."""

from __future__ import annotations

from pydantic import Field

from dt_contracts.base import DeepthoughtBaseModel


class KaplayAction(DeepthoughtBaseModel):
    """Action to manipulate the Kaplay.js scene."""

    action_type: str = Field(..., description="e.g. 'spawn_sprite', 'destroy_sprite', 'shake_camera'")
    entity_id: str | None = None
    properties: dict[str, object] = Field(default_factory=dict) # architectural: allowed-object (Engine Properties)


class MinetestAction(DeepthoughtBaseModel):
    """Action to manipulate the Minetest world via Lua API."""

    action_type: str = Field(..., description="e.g. 'set_node', 'give_item', 'teleport'")
    pos: list[int] | None = None
    item_string: str | None = None


class SnapAction(DeepthoughtBaseModel):
    """Action to manipulate the Snap! block environment."""

    action_type: str = Field(..., description="e.g. 'say', 'glow_block', 'move_sprite'")
    sprite_name: str | None = None
    block_id: str | None = None
    message: str | None = None
