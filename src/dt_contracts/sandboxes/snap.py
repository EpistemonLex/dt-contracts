"""Snap! block-based coding contracts."""

from pydantic import ConfigDict, Field

from dt_contracts.base import DeepthoughtBaseModel


class SnapBlock(DeepthoughtBaseModel):
    """Representation of a single coding block in Snap!."""

    model_config = ConfigDict(slots=True)

    id: str
    selector: str = Field(..., description="The primitive name (e.g. 'forward', 'say')")
    inputs: list[object] = Field(default_factory=list) # architectural: allowed-object (Nested block inputs)

class SnapSprite(DeepthoughtBaseModel):
    """The state of a single sprite in the Snap! stage."""

    model_config = ConfigDict(slots=True)

    name: str
    x: float
    y: float
    direction: float
    scripts_count: int

class SnapState(DeepthoughtBaseModel):
    """The overall state of the Snap! project."""

    model_config = ConfigDict(slots=True)

    project_name: str
    sprites: list[SnapSprite]
    variables: dict[str, object] = Field(default_factory=dict) # architectural: allowed-object (Dynamic block variables)
    is_running: bool = False
