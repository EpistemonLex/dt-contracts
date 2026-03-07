"""High-fidelity Action contracts for specific sandbox interventions."""

from pydantic import ConfigDict, Field

from dt_contracts.base import DeepthoughtBaseModel


class KaplayAction(DeepthoughtBaseModel):
    """Actions the AI Tutor can perform in Kaplay."""

    model_config = ConfigDict(slots=True)

    action_type: str = Field(..., description="e.g. 'pause', 'spawn', 'highlight_code'")
    target_id: str | int | None = None
    params: dict[str, object] = Field(default_factory=dict) # architectural: allowed-object

class PhETAction(DeepthoughtBaseModel):
    """Actions the AI Tutor can perform in PhET."""

    model_config = ConfigDict(slots=True)

    action_type: str = Field(..., description="e.g. 'set_variable', 'reset', 'pause'")
    variable_name: str | None = None
    value: float | str | bool | None = None

class SnapAction(DeepthoughtBaseModel):
    """Actions the AI Tutor can perform in Snap!."""

    model_config = ConfigDict(slots=True)

    action_type: str = Field(..., description="e.g. 'say', 'glow_block', 'move_sprite'")
    sprite_name: str | None = None
    block_id: str | None = None
    message: str | None = None
