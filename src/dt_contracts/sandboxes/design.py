"""Contracts for Design, Art, and Visual Thinking sandboxes."""

from pydantic import ConfigDict, Field

from dt_contracts.base import DeepthoughtBaseModel


class CanvasShape(DeepthoughtBaseModel):
    """A shape or sketch on a canvas."""

    model_config = ConfigDict(slots=True)

    id: str
    type: str = Field(..., description="e.g. 'arrow', 'box', 'scribble'")
    bounds_x: float
    bounds_y: float
    text: str | None = None

class DesignState(DeepthoughtBaseModel):
    """The state of a visual thinking canvas (tldraw)."""

    model_config = ConfigDict(slots=True)

    shapes: list[CanvasShape]
    active_tool: str
    camera_zoom: float = 1.0
